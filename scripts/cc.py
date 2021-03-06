from cookiecutter.main import cookiecutter

if __name__ == '__main__':
    package = 'https://github.com/luiscberrocal/cookiecutter-django'
    config_file = '/home/luiscberrocal/PycharmProjects/django_ansible_config/cookiecutter/cookiecutter-config.yml'

    t = cookiecutter(package,
                     no_input=True,
                     config_file=config_file,
                     checkout='develop',
                     extra_context={'project_slug': 'tj_great'})
    print(t)
