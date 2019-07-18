import requests
from hashlib import sha3_512
from functools import partial
import json
import ssl
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import keys

# ========================================================================================
# Selenium functions

def webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    driver = webdriver.Chrome(options=options)
    return driver


def screenshot_string_return(configured_driver_input, website):
    configured_driver_input.get(website)
    result = configured_driver_input.get_screenshot_as_base64()
    return result

def configured_screen_shot_func(website):
    screenshot_func = partial(screenshot_string_return, configured_driver_input=webdriver())
    return screenshot_func(website)

def screenshot(website_input):
    return configured_screen_shot_func(website_input)


# ========================================================================================
# Use these functions to check the website screenshot.

def hash_to_check(file_name_import):
    json_file = open(file_name_import, "r+")
    loaded_dict = json.load(json_file)
    return loaded_dict['website_hash']

#good
def digest_returner(object_input):
    hash_object = sha3_512(str.encode(object_input))
    return hash_object.hexdigest()

def checker(hash_one, hash_two):
    if hash_one == hash_two:
        return False
    else:
        return True



def website_checker(config_file_dict):
    result = digest_returner(screenshot(config_file_dict['website']))
    hash_object = config_file_dict['website_hash']
    hash_check_partial = partial(checker, hash_two=hash_object)
    if hash_check_partial(result):
        return config_file_dict['website']
    else:
        return None



def none_type_try_catch(check_input, function):
    if type(check_input) == None:
        return None
    else:
        function(check_input)


def fold(func_list, input_object):
    variable_holder = str()
    for i in func_list:
        variable_holder = i(input_object)
    return variable_holder








def config_grabber(file_name_import):
    json_file = open(file_name_import, "r+")
    loaded_dict = json.load(json_file)
    return loaded_dict
# ========================================================================================

# Catches a None Type that might be returned from the above


# ========================================================================================
# Server creation and SMTP message generation


#good
def server_context(address):
    context = ssl.create_default_context()
    return smtplib.SMTP_SSL(address['address'], address['port'], context=context)

#good
def login(server_input, creds):
    return server_input.login(creds['username'], creds['password'])

def message(server_input, mail_message):
    server_input.sendmail(mail_message)
    print('success!')
    return mail_message

def message_creator(url_input):
    return '{url_input} has changed. Please visit the page'


# ========================================================================================
# Full message creation function
def send_message(config_input, mail_message_input):
    login_with_creds = partial(login, creds=config_input)
    pre_filled_message = partial(message, mail_message=message_creator(mail_message_input))
    return message(login(server_context(config_input)))

# ========================================================================================
# main()
def main(email_config, web_config):
    configured_smtp = partial(send_message, config_input=config_grabber(email_config))
    function_list = [config_grabber, website_checker]
    none_type_try_catch(fold(function_list, web_config), message_creator)
    

if __name__=="__main__":
    main('email.json', 'config.json')
