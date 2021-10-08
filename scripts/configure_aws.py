import subprocess

from jinja2 import Environment, PackageLoader, select_autoescape


def run_piped_commands(command, encoding='utf-8'):
    command_parts = command.split('|')
    subprocesses = list()
    for i, c in enumerate(command_parts):
        if len(subprocesses) > 0:
            stdin = subprocess[i - 1]
        else:
            stdin = subprocess.PIPE
        commands = c.split(' ')
        result = subprocess.run(commands,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=stdin)
        subprocesses.append(result)
    result_lines = subprocesses[:-1].stdout.decode(encoding).split('\n')[:-1]
    error_lines = subprocesses[:-1].stderr.decode(encoding).split('\n')[:-1]
    return result_lines, error_lines


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


def get_buckets(bucket_name=None):
    command = f'aws s3 ls'  # | grep "{bucket_name}"'
    commands = command.split(' ')
    results, errors = run_commands(commands)
    if bucket_name is not None:
        results = [x for x in results if bucket_name in x]
    display_results(results, errors)


def create_bucket(**kwargs):
    project_slug = kwargs['project_slug']
    environment = kwargs.get('environment', 'staging')
    dry_run = kwargs.get('dry_run', False)

    bucket_name = f"{project_slug.replace('_', '-')}-{environment}-bucket"
    command = f'aws s3 mb s3://{bucket_name}'
    print(command)
    if not dry_run:
        commands = command.split(' ')
        results, errors = run_commands(commands)
        display_results(results, errors)
    return bucket_name


def display_results(results, errors):
    print('-' * 80)
    for i, result in enumerate(results):
        print(f'{i + 1} {result}')
    print('-' * 80)
    print(errors)


def create_aws_group(project_slug, environment='staging', **kwargs):
    """aws iam create-group --group-name {{ aws_staging_group }}"""
    verbose = kwargs.get('verbose', False)
    group = f"{project_slug.replace('_', '-')}-{environment}-group"
    commands = f'aws iam create-group --group-name {group}'.split(' ')
    results, errors = run_commands(commands)
    if verbose:
        display_results(results, errors)
    return group


def create_policy_file(filename, bucket_name, **kwargs):
    verbose = kwargs.get('verbose', False)
    env = Environment(
        loader=PackageLoader("scripts"),
        autoescape=select_autoescape()
    )

    template = env.get_template("s3_policy.json.j2")
    content = template.render(aws_staging_bucket=bucket_name)
    if verbose:
        print(content)
    with open(filename, 'w') as json_file:
        json_file.write(content)
    return content

def create_policy(bucket_name, filename, **kwargs):
    """
   "aws iam create-policy --policy-name {{ aws_staging_bucket }}-policy --policy-document file://./output/{{ aws_staging_bucket }}_policy.json"
    :return: 
    """
    verbose = kwargs.get('verbose', False)
    commands = f"aws iam create-policy --policy-name {bucket_name}-policy" \
              f" --policy-document file://{filename}".split(' ')
    results, errors = run_commands(commands)
    if verbose:
        display_results(results, errors)



if __name__ == '__main__':
    slug = 'home_automation'
    # create_bucket(project_slug=slug, dry_run=True)
    bucket_pattern = slug.replace('_', '-')
    get_buckets(bucket_pattern)
    # group_name = create_aws_group(slug, verbose=True)
    bucket_name = f"{slug.replace('_', '-')}-staging-bucket"
    filename = f'../output/{bucket_name}-s3-policy.json'
    create_policy_file(filename, bucket_name)
    create_policy(bucket_name, filename, verbose=True)



