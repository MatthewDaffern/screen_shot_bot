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

def configured_screen_shot_func(driver_input):
    screenshot_func = partial(screenshot_string_return, website=website_from_config('config.json'))
    return screenshot_func(driver_input)

def screenshot():
    return configured_screen_shot_func(webdriver())


# ========================================================================================
# Use these functions to check the website screenshot.



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
# ========================================================================================

#good
def fold(func_list, input_object):
    variable_holder = str()
    for i in func_list:
        variable_holder = i(input_object)
    return variable_holder

# ========================================================================================
# config loading section



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
# ========================================================================================
# Checks the website for change
def checking_function(file_name_import):
    hash_check = partial(checker, hash_two=hash_to_check(file_name_import))
    #rewrite this to support selenium
    func_list = [website_text_getter, digest_returner, hash_check]
    website = website_from_config('config.json')
    is_changed = fold(func_list, website)
    if is_changed == True:
        return website
# Catches a None Type that might be returned from the above
def none_type_try_catch(check_input, function):
    if type(check_input) == None:
        return None
    else:
        function(check_input)

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
def main():
    configured_smtp = partial(send_message, config_input=config_grabber('email.json'))
    none_type_try_catch(checking_function('config.json'), message_creator)


if __name__=="__main__":
    main()
