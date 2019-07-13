#good
import json

def password():
    return input('please enter your password \n')

def username():
    return input('please enter your username \n')

def dump_config(username_input, password_input):
    cred_dict =dict([('username_field', username_input), ('password_field', password_input)])
    email_config_json = open('email.json', "w+")
    json.dump(cred_dict, email_config_json)
    email_config_json.close()
    print("file created")

def main():
    dump_config(username(), password())


if __name__=="__main__":
    main()
