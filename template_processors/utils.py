import importlib

from django.core.exceptions import ImproperlyConfigured


def import_by_path(dotted_path):
    try:
        module, attr = dotted_path.rsplit(".", 1)
        mod = importlib.import_module(module)
        fn = getattr(mod, attr)

        assert callable(fn), f"Preprocessor{dotted_path:!r} must be callable"

        return fn
    except (ImportError, AttributeError, AssertionError) as e:
        raise ImproperlyConfigured(
            f"Could not import template preprocessor {dotted_path}: {e}"
        ) from e
