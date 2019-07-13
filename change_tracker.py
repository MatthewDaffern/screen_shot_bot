import requests
from hashlib import sha3_512
from functools import partial
import json
import ssl
import smtplib

#good
def digest_returner(object_input):
    hash_object = sha3_512(str.encode(object_input))
    return hash_object.hexdigest()
#good
def website_text_getter(str_input):
    website = requests.get(str_input)
    return website.text
#good
def checker(hash_one, hash_two):
    if hash_one == hash_two:
        return False
    else:
        return True
#good
def fold(func_list, input_object):
    variable_holder = str()
    for i in func_list:
        variable_holder = i(input_object)
    return variable_holder

#good
def website_from_config(file_name_import):
    json_file = open(file_name_import, "r+")
    loaded_dict = json.load(json_file)
    return loaded_dict['website']


#good
def hash_to_check(file_name_import):
    json_file = open(file_name_import, "r+")
    loaded_dict = json.load(json_file)
    return loaded_dict['website_hash']




def checking_function(file_name_import):
    hash_check = partial(checker, hash_two=hash_to_check(file_name_import))
    func_list = [website_text_getter, digest_returner, hash_check]
    is_changed = fold(func_list, website_from_config('config.json'))
    if is_changed == True:
        return True
    else:
        return False




#good
def server_context(port, address):
    context = ssl.create_default_context()
    return smtplib.SMTP_SSL(address, port, context=context)

def login(server_input, creds):
    return server_input.login(creds[username], creds[password])

def message(server_input, mail_message):
    server_input.sendmail(mail_message)
    print('success!')
    return mail_message


def send_message(port_input, address_input, creds_input, message_input):
    message_partial = partial(message, mail_message=message_input)
    login_partial = partial(login, creds=creds_input)
    server = login_partial(server_context(port_input, address_input))
    return message_partial(server)

def main():
# TODO the whole thing"


if __name__=="__main__":
    main()
