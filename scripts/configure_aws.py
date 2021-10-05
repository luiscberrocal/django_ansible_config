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


def get_bucket(bucket_name):
    command = f'aws s3 ls' # | grep "{bucket_name}"'
    commands = command.split(' ')
    results, errors = run_commands(commands)
    display_results(results, errors)


def create_bucket(**kwargs):
    project_slug = kwargs['project_slug']
    environment = kwargs.get('environment', 'staging')
    dry_run = kwargs.get('dry_run', False)

    bucket_name = f"{project_slug.replace('_', '-')}-{environment}-bucket"
    command = f'aws s3 mb s3://{bucket_name}'
    if dry_run:
        print(command)
    commands = command.split(' ')
    results, errors = run_commands(commands)
    display_results(results, errors)


def display_results(results, errors):
    print('-' * 80)
    print(results)
    print('-' * 80)
    print(errors)


if __name__ == '__main__':
    slug = 'home_automation'
    # create_bucket(project_slug=slug, dry_run=True)
    bucket_pattern = slug.replace('_', '-')
    get_bucket(bucket_pattern)
