from django.template.response import TemplateResponse


def pre_processor(x: str) -> str:
    print("pre_processor")
    return x


def post_processor(x: TemplateResponse) -> TemplateResponse:
    print("post_processor")
    return x
