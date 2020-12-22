import re


def get_variable(start_at, lines):
    variable_data = dict()
    regexp_start = re.compile(start_at)
    regexp_stop = re.compile(r'\]')
    regexp = regexp_start
    found = False
    line_num = 1
    switches = 0
    for line in lines:
        if switches < 2:
            match = regexp.match(line)
            if match:
                found = not found
                regexp = regexp_stop
                switches += 1
            if found or switches == 2:
                print(f'>{line_num} {line}')
                variable_data[line_num] = line
        line_num += 1
    return variable_data, list(variable_data.keys())[0], list(variable_data.keys())[-1]


def append_new_data(result, apps):
    last_line_num = list(result.keys())[-1]
    last_lne = result[last_line_num]
    for app in apps:
        for line_num, line in result.items():
            regexp = re.compile(app['regex'])
            match = regexp.match(line)
            if match:
                app['found'] = True

    for app in apps:
        if not app['found']:
            print(app['name'])
            result[last_line_num] = f"    '{app['name']}',"
            last_line_num += 1

    result[last_line_num] = last_lne

    for line_num, line in result.items():
        print(f'>>{line_num} {line}')
    return result


if __name__ == '__main__':
    with open('base.py', 'r') as py_file:
        lines = py_file.read().split('\n')

    results, start, end = get_variable(r'^THIRD_PARTY_APPS\s=\s\[?', lines)
    apps = [
        {'name': 'import_export', 'regex': r"\s+('|\")import_export('|\"),", 'found': False},
        {'name': 'allauth', 'regex': r"\s+('|\")allauth('|\"),", 'found': False},
        {'name': 'rolepermissions', 'regex': r"\s+('|\")rolepermissions('|\"),", 'found': False},
    ]

    clean_result = append_new_data(results, apps)
    wrote_results = False
    with open('base_d.py', 'w') as py_file:
        line_num = 1
        for line in lines:
            if line_num < start or line_num > end:
                py_file.write(line + '\n')
            else:
                if not wrote_results:
                    for key, new_line in clean_result.items():
                        py_file.write(new_line + '\n')
                    wrote_results = True
            line_num += 1


