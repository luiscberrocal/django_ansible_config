# Django Tools

## Clone project
    git clone XXX

## Create credentials file

    ansible-playbook prep_secrets.yml --extra-vars "{'pwd': '_Wolverine0912'}"

## Start app
    ansible-playbook playbook.yml --extra-vars '{"django_project_slut": "rec_prom1"}'
    

## Creating secrets

## To create a django app
    $  ansible-playbook django_app.yml --extra-vars '{"django_app_name": "demo", "django_project_slug": "alpha_clinic"}'
    
    # ansible-playbook django_app.yml --extra-vars '{"django_app_name": "real_estate"}'

## To create test views
    $ ansible-playbook django_test_views.yml --extra-vars '{"namespace": "real-estate", "model_name": "Contract"}'
