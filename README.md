# Django  project configuration using Ansible

Configuration of Django project using Ansible and Cookie cutter

To tun the playbook you need to have installed:

    1. Heroku CLI
    2. AWS CLI
    3. Github CLI
       To install:
        >  ansible-playbook ./packages/github_cli.yml -K


You need to be logged in each service for the playbook to run.



## Cookiecutter

Requires Python 3.x and cookiecutter (https://github.com/pydanny/cookiecutter-django) installed.

Goto PycharmProjects and run:

    $  cookiecutter --no-input https://github.com/pydanny/cookiecutter-django --config-file ./django_ansible_config/cookiecutter/cookiecutter-config.yml
    
Copy cookiecutter configuration to the project. In my example the 

    $ cp ~/.cookiecutter_replay/cookiecutter-django.json ./rec_promoter_app
    
## Github

Create a repo with the same name as your cookiecutter slug **rec_promoter_app** for our example


## How to use

Edit cookiecutter/cookiecutter-config.yml specifically the **project_name** and
**project_slug**.

The creation of the admin user for Django is based con the file ./.secrets/credentials.yml with the data in this file
Ansible will create a superuser for you.

Steps before running the main playbook. 

    1. Run:
        $ ansible-playbook prep_secrets.yml --extra-vars '{"pwd":"12333"}'

    2. Edit  the file named .secrets/credential.yml with the following below. This content will ber used to create your super user in Django:

        dev:
            username: your-username
            pwd: your-password
            email: your-email
        staging:
            username: your-username
            pwd: your-password
            email: your-email

Run:

    $ ansible-playbook playbook.yml




    
