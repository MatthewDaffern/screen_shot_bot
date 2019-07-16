#good
import json

def password():
    return input('please enter your password \n')

def username():
    return input('please enter your username \n')

def server_name():
    return input('What is the name of the mail server? \n')

def port():
    return input('What port are you using? \n')


def dump_config(username_input, password_input, server_name_input, port_input):
    cred_dict =dict([('username_field', username_input), ('password_field', password_input), ('server_name', server_name_input), ('port', port_input)])
    email_config_json = open('email.json', "w+")
    json.dump(cred_dict, email_config_json)
    email_config_json.close()
    print("file created")

def main():
    dump_config(username(), password(), server_name(), port())


if __name__=="__main__":
    main()
