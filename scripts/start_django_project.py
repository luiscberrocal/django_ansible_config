import subprocess


def run_commands(commands, encoding='utf-8'):
    """
    :param commands: <list> The command and paraemters to run
    :param encoding: <str> Encoding for the shell
    :return: <tuple> Containing 2 lists. First one with results and the Second one with errors if any.
    """
    result = subprocess.run(commands,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    result_lines = result.stdout.decode(encoding).split('\n')[:-1]
    error_lines = result.stderr.decode(encoding).split('\n')[:-1]
    return result_lines, error_lines


def main(**kwargs):
    #print(f'kw: {kwargs}')
    extra_vars = {"django_project_slug": kwargs['project_slug'],
                  'do_local_tasks': kwargs['local'],
                  'do_cloud_tasks': kwargs['cloud'],
                  }  # , "do_local_tasks": "no"}'
    if kwargs['skip'] is not None:
        for skip_task in kwargs['skip']:
            extra_vars[f'skip_{skip_task}'] = True
    print(f'extra_vars: "{extra_vars}"')
    command = ['ansible-playbook', 'playbook.yml', '--extra-vars', f'{extra_vars}']
    res, error = run_commands(command)
    for line in res:
        print(line)
    print('<>' * 40)
    for line in error:
        print(line)


if __name__ == '__main__':
    """
    To run all local and cloud tasks
        $ python ./scripts/start_django_project.py -p rec_promoter_app -l -c 
        
    To run all local and cloud tasks except github tasks
        $ python ./scripts/start_django_project.py -p rec_promoter_app -l -c -s github
    """
    import argparse

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--project-slug", required=True,
                    help="Project slug")
    ap.add_argument("-l", "--local", required=False,
                    action="store_true",
                    help="Run local tasks")
    ap.add_argument("-c", "--cloud", required=False,
                    action="store_true",
                    help="Run cloud tasks")
    ap.add_argument('-s', '--skip', metavar='skip_list', type=str, nargs='+',
                    choices=['cookiecutter', 'git_setup', 'aws', 'heroku', 'github'],
                    help='Tasks to skip')
    args = vars(ap.parse_args())
    # print(type(args))
    print(args)
    main(**args)
