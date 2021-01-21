import re


class FilterModule(object):
    def filters(self):
        return {'to_snake_case': self.to_snake_case,
                'to_dash_case': self.to_dash_case,
                'to_camel_case': self.to_camel_case}

    def to_snake_case(self, variable_name):
        """
        Converts from TransactionType to transaction_type
        :param variable_name:
        :return:
        """
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', variable_name).lower()
        return name

    def to_dash_case(self, variable_name):
        """
        Converts from TransactionType to transaction-type
        :param variable_name:
        :return:
        """
        name = re.sub(r'(?<!^)(?=[A-Z])', '-', variable_name).lower()
        return name

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return ''.join(x.title() for x in components)
