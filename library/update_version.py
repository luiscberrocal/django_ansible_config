from ansible.module_utils.basic import AnsibleModule


def main():

	module = AnsibleModule(argument_spec={})
	response = {"hello": "world"}
	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()