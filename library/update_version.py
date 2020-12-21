import os
import re

from ansible.module_utils.basic import AnsibleModule


# https://blog.toast38coza.me/custom-ansible-module-hello-world/
def update_version(data):
	filename = data['base_html']
	if not os.path.exists(filename):
		return True, False, {'msg': f'{filename} not found'}

	with open(filename, 'r') as html:
		content = html.read()

	regex = r"<a\s+class=\"navbar-brand\"\s+href=\"{%\s+url\s'home'\s%}\">([\w\s\-\+]+)</a>"
	subst = "<a class=\"navbar-brand\" href=\"{% url 'home' %}\">\\1 <span class=\"version\">0.1.0</span></a>"

	matches = re.findall(regex, content, re.MULTILINE)
	if len(matches) == 1:
		# You can manually specify the number of replacements by changing the 4th argument
		result = re.sub(regex, subst, content, 0, re.MULTILINE)

		if result:
			with open(filename, 'w') as html:
				html.write(result)
			return False, True, {'result': 'SUCCESS'}
		
	if len(matches) == 0:
		return True, False, {'msg': 'No match found for regexp'}

	return True, False, {'msg': 'Unexpected result'}


def main():
	fields = {
		"base_html": {"required": True, "type": "str"},
		"backup": {"default": False, "type": "bool"},
	}

	module = AnsibleModule(argument_spec=fields)

	is_error, has_changed, result = update_version(module.params)
	if not is_error:
		module.exit_json(changed=has_changed, meta=result)
	else:
		module.fail_json(msg="Error deleting repo", meta=result)


if __name__ == '__main__':
	main()
