import os
from cookiecutter.main import cookiecutter

from ansible.module_utils.basic import AnsibleModule


def run_cookiecutter(**kwargs):
    is_error = False
    has_changed = False
    package = kwargs.get('package',
                         'https://github.com/luiscberrocal/cookiecutter-django')
    checkout = kwargs.get('checkout', 'develop')

    try:

        config_file = kwargs['config_file']
        django_project_slug = kwargs['django_project_slug']

        res = cookiecutter(package,
                           no_input=True,
                           config_file=config_file,
                           checkout=checkout,
                           extra_context={'project_slug': django_project_slug},
                           output_dir=kwargs['target_folder'])
        has_changed = True

    except Exception as e:
        is_error = True
        res = str(e)

    return is_error, has_changed, res


def main():
    fields = {
        "config_file": {"required": True, "type": "str"},
        "django_project_slug": {"required": True, "type": "str"},
        "target_folder": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, result = run_cookiecutter(**module.params)
    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error creating Django project", meta=result)


if __name__ == '__main__':
    main()
