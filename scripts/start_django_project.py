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
    print(f'kw: {kwargs}')
    extra_vars = {"django_project_slug": kwargs['project_slug'],
                  'do_local_tasks': 'yes' if kwargs['local'] else 'no',
                  'do_cloud_tasks': 'yes' if kwargs['cloud'] else 'no',
                  }  # , "do_local_tasks": "no"}'

    command = ['ansible-playbook', 'playbook.yml', '--extra-vars', str(extra_vars)]
    res, error = run_commands(command)
    for line in res:
        print(line)
    print('<>'*40)
    for line in error:
        print(line)


if __name__ == '__main__':
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
    args = vars(ap.parse_args())
    #print(type(args))
    #print(args)
    main(**args)
