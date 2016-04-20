
# config.py
# reads and stores the config values from config.json in the project root
#
# HISTORY:
#   created 2016-4-19 JMP

import json

config = dict()


def init_config():
    with open('../config.json') as json_data_file:
        data = json.load(json_data_file)
    for key in data.keys():
        config[key] = data[key]

    print "Config Ready!"


