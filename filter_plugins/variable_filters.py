import re


class FilterModule(object):
    def filters(self):
        return {'to_snake_case': self.to_snake_case,
                'to_dash_case': self.to_dash_case, }

    def to_snake_case(self, variable_name):
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', variable_name).lower()
        return name

    def to_dash_case(self, variable_name):
        name = re.sub(r'(?<!^)(?=[A-Z])', '-', variable_name).lower()
        return name
