#good
from change_tracker import *
import json
def config(website_input):
    return digest_returner(website_text_getter(website_input))


def website_recorder():
    return input('Please enter in your exact web_link you use for tracking \n')

def json_dumper(digest_input, website_input):
    result = dict([('website_hash', digest_input), ('website', website_input)])
    json_file = open("config.json","w+")
    json.dump(result, json_file)
    json_file.close()
    print("config_created")


def main():
    website_getter = website_recorder()
    return json_dumper(config(website_getter), website_getter)

if __name__=="__main__":
    main()







