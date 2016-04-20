
# reads in the json data, and builds it into an object

import json
import os
from config import config

class Data:
    def __init__(self):
        self.data = []
        self.length = 0
        self.current_id = 0

    def __str__(self):
        return "Data obj of length " + str(self.data.__len__())

    def update(self):
        self.length = self.data.__len__()

    def sort(self, cm):
        self.data = sorted(self.data, cm)

    def add(self, other_list):
        self.data += other_list
        self.update()

    def push(self, item, given_id):
        item["data_id"] = given_id
        self.data.append(item)
        self.update()

    def dump(self):
        for item in self.data:
            print item["data_id"]
        print self.data.__len__()


def read_orders():
    i = 0
    d = Data()
    for data_file in os.listdir(str(config["order_folder"])):
        name = str(config["order_folder"]) + "/" + data_file
        file_data = open(name).read()
        json_data = json.loads(file_data)
        for item in json_data:
            d.push(item, i)
            i += 1
    return d


def read_tests():
    i = 0
    d = Data()
    for data_file in os.listdir(str(config["test_folder"])):
        name = str(config["test_folder"]) + "/" + data_file
        file_data = open(name).read()
        json_data = json.loads(file_data)
        for item in json_data:
            d.push(item, i)
            i += 1
    return d


def test():
    from config import init_config
    init_config()
    read_tests()
    read_orders()



# test = read()
#
# print test