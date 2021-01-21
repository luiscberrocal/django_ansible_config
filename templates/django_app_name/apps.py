from django.apps import AppConfig


class {{django_app_name | to_camel_case}}Config(AppConfig):
    name = '{{django_project_slug}}.{{django_app_name}}'
