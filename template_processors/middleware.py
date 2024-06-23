from asgiref.sync import async_to_sync, iscoroutinefunction
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils.decorators import sync_and_async_middleware

from .utils import import_by_path


@sync_and_async_middleware
def TemplatePostProcessorMiddleware(get_response):  # noqa: N802
    post_processors = [
        import_by_path(path)
        for path in getattr(settings, "TEMPLATE_POST_PROCESSORS", [])
    ]

    if iscoroutinefunction(get_response):

        async def middleware(request):
            response = await get_response(request)
            if not isinstance(response, TemplateResponse):
                return response

            for post_processor in post_processors:
                response.add_post_render_callback(post_processor)

            return response

    else:

        def middleware(request):
            response = get_response(request)
            if not isinstance(response, TemplateResponse):
                return response

            for post_processor in post_processors:
                response.add_post_render_callback(post_processor)

            return response

    return middleware
