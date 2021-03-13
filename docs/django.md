# Django Tools

## Clone project
    git clone XXX

## Create credentials file

    ansible-playbook prep_secrets.yml --extra-vars "{'pwd': '_Wolverine0912'}"


## Creating secrets

## To create a django app
    $  ansible-playbook django_app.yml --extra-vars '{"django_app_name": "real_estate"}'
    
    # ansible-playbook django_app.yml --extra-vars '{"django_app_name": "real_estate"}'

## To create test views
    $ ansible-playbook django_test_views.yml --extra-vars '{"namespace": "real-estate", "model_name": "Contract"}'
