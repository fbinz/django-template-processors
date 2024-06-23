## Installation

- Install the package via pip:

  `pip install {{ package_name }}`

  or via pipenv:

  `pipenv install {{ package_name }}`

- Add module to `INSTALLED_APPS` within the main django `settings.py`:

    ```python
    INSTALLED_APPS = (
        ...
        '{{ module_name }}',
    )
     ```

- Extend the `TEMPLATE_PRE_PROCESSORS` and `TEMPLATE_POST_PROCESSORS` settings with your own processors:

    ```python
    TEMPLATE_PRE_PROCESSORS = [
        'my_app.processors.my_pre_processor',
    ]

    TEMPLATE_POST_PROCESSORS = [
        'my_app.processors.my_post_processor',
    ]
     ```

- Adjust the template loaders to use the new template processors. As an example, the
  following configuration assumse that you had the built-in `filesystem` and `app_directories`
  loaders configured. You need to wrap each loader with the `{{ module_name }}.loader.Loader`
  class:

    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            ...,
            'OPTIONS': {
                ...,
                'loaders': [
                    (
                        '{{ module_name }}.loader.Loader',
                        'django.template.loaders.filesystem.Loader',
                    ),
                    (
                        '{{ module_name }}.loader.Loader',
                        'django.template.loaders.app_directories.Loader',
                    ),
                ],
            },
        },
    ]
     ```
