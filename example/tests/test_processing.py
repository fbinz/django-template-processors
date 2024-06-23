import pytest
from django.template.response import TemplateResponse


def pre_processor(_contents: str) -> str:
    return "CALLED"


def post_processor(response: TemplateResponse) -> TemplateResponse:
    response.content = "CALLED"
    return response


def view(request):
    return TemplateResponse(request, "example/index.html", {})


def test_default_settings(settings):
    assert settings.TEMPLATE_PRE_PROCESSORS == []
    assert settings.TEMPLATE_POST_PROCESSORS == []


def test_pre_processor_called(settings):
    settings.TEMPLATE_PRE_PROCESSORS = ["example.tests.test_processing.pre_processor"]

    from django.template.loader import get_template

    template = get_template("example/index.html")
    result = template.render(context={})

    assert result == "CALLED"


def test_post_processor_called(settings, client):
    settings.TEMPLATE_POST_PROCESSORS = ["example.tests.test_processing.post_processor"]

    # Note: we need to go through the middleware-chain to trigger
    # the post-processor.
    response = client.get("/")

    assert response.content == b"CALLED"
