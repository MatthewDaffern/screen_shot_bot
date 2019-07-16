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


#good
def config_grabber(file_name_import):
    json_file = open(file_name_import, "r+")
    loaded_dict = json.load(json_file)
    return loaded_dict

def checking_function(file_name_import):
    hash_check = partial(checker, hash_two=hash_to_check(file_name_import))
    func_list = [website_text_getter, digest_returner, hash_check]
    website = website_from_config('config.json')
    is_changed = fold(func_list, website)
    if is_changed == True:
        return website

def none_type_try_catch(check_input, function):
    if type(check_input) == None:
        return None
    else:
        function(check_input)


#good
def server_context(address):
    context = ssl.create_default_context()
    return smtplib.SMTP_SSL(address[address], address[port], context=context)

#good
def login(server_input, creds):
    return server_input.login(creds[username], creds[password])

def message(server_input, mail_message):
    server_input.sendmail(mail_message)
    print('success!')
    return mail_message

def message_creator(url_input):
    return '{url_input} has changed. Please visit the page'

def send_message(config_input, mail_message_input):
    login_with_creds = partial(login, creds=config_input)
    pre_filled_message = partial(message, mail_message=message_creator(mail_message_input))
    return message(login(server_context(config_input)))

def main():
    configured_smtp = partial(send_message, config_input=config_grabber('email.json'))
    none_type_try_catch(checking_function('config.json'), message_creator)

if __name__=="__main__":
    main()
