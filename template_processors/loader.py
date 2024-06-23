from django.conf import settings
from django.template.loaders.base import Loader as BaseLoader

from .utils import import_by_path


class Loader(BaseLoader):
    """A template loader that runs pre-processors on the template contents."""

    def __init__(self, engine, loader):
        self.wrapped_loader = engine.find_template_loader(loader)

        self.preprocessors = None

        # Monkey-patch the loader to run our own get_contents method
        self.loader_get_contents = self.wrapped_loader.get_contents
        self.wrapped_loader.get_contents = self.get_contents

        super().__init__(engine)

    def get_contents(self, origin):
        contents = self.loader_get_contents(origin)

        if self.preprocessors is None:
            self.preprocessors = [
                import_by_path(path)
                for path in getattr(settings, "TEMPLATE_PRE_PROCESSORS", [])
            ]

        # Apply pre-processors
        for preprocessor in self.preprocessors:
            contents = preprocessor(contents)

        return contents

    # Forward all other methods to the wrapped loader
    def get_template(self, template_name, skip=None):
        template = self.wrapped_loader.get_template(template_name, skip)
        return template

    def get_template_sources(self, template_name):
        return self.wrapped_loader.get_template_sources(template_name)

    def reset(self):
        return self.wrapped_loader.reset()
