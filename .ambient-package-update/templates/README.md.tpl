{% include "snippets/badges.tpl" %}
{% include "snippets/tagline.tpl"%}
{% include "snippets/links.tpl" %}

Adds pre- and post-processing hooks to your Django project.
While this package does not provide any functionality itself, it is
configurable to add your own pre- and post-processing hooks.

{% include "snippets/installation.tpl" %}

## Usage

Configure pre- and post-processing hooks in your `settings.py`:

```python
TEMPLATE_PRE_PROCESSORS = [
    'my_app.processors.my_pre_processor',
]

TEMPLATE_POST_PROCESSORS = [
    'my_app.processors.my_post_processor',
]
```

Pre-processors are called before the template is rendered with the string contents of the template.
Post-processors are called after the template is rendered with the full `TemplateResponse` object.

Note that the post-processing only works, if the view returns a `TemplateResponse` object, i.e.
not if the view returns using djangos `render` function.

{% include "snippets/contribute.tpl" %}
{% include "snippets/publish.tpl" %}
{% include "snippets/maintenance.tpl" %}
