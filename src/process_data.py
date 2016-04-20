
from read_input import read_orders
from read_input import read_tests
from write_excel import Excel_Template
import os


def map_to_orders(data):
    ret = dict()
    for x in range(0, data.__len__()):
        key = str(data[x]["order_number"])
        try:
            ret[key].append(data[x])
        except:
            ret[key] = list()
            ret[key].append(data[x])
    return ret


def compute_stats(data):

    ret = dict()
    for key in data.keys():
        ret[key] = dict()
        mean = float(data[key][0]["result"])
        max_value = data[key][0]["result"]
        min_value = data[key][0]["result"]
        for x in range(1, data[key].__len__()):
            val = float(data[key][x]["result"])
            mean += val
            if val > max_value:
                max_value = val
            if val < min_value:
                min_value = val

        mean = mean / data[key].__len__()
        ret[key]["mean"] = mean
        ret[key]["max"] = max_value
        ret[key]["min"] = min_value
    return ret


def order_cmp(a,b):
    return a["order_id"] < b["order_id"]


def handle_orders():
    orders = read_orders()
    # names = ["First Name", "Last Name", "Eye Color", "Balance", "Company"]
    # names += ["Email", "Latitude", "Longitude", "Phone", "Address", "Registered"]
    #
    # t = Excel_Template(names.__len__(), names, "test")

    dirname = "./results"

    try:
        os.stat(dirname)
    except:
        os.mkdir(dirname)

    names = ["Order", "Customer", "Placed On", "Notes"]
    keys = ["order_id", "customer", "placed_on", "notes"]
    t = Excel_Template(names.__len__(), names, "data")

    row = 2
    blank_row = ["", "", "", ""]

    # orders.data = orders.data.sort(order_cmp)
    #
    for x in orders.data:
        tmp = ["", "", "", ""]
        for key in x.keys():
            if key == keys[0]:
                tmp[0] = x[keys[0]]
            elif key == keys[1]:
                tmp[1] = x[keys[1]]
            elif key == keys[2]:
                tmp[2] = x[keys[2]]
            elif key == keys[3]:
                tmp[3] = x[keys[3]]
        t.write_row(row, tmp, "data")
        row += 1

    t.save(dirname+"/orders.xlsx")

    print "Wrote", orders.length, "rows"
    print "All Done"


def handle_tests():
    tests = read_tests()
    # names = ["First Name", "Last Name", "Eye Color", "Balance", "Company"]
    # names += ["Email", "Latitude", "Longitude", "Phone", "Address", "Registered"]
    #
    # t = Excel_Template(names.__len__(), names, "test")

    dirname = "./results"

    try:
        os.stat(dirname)
    except:
        os.mkdir(dirname)

    names = ["Order", "Test", "Completed", "Result", "Ran By", "Test Number", "Stage"]
    keys = ["order_id", "test_name", "completed", "result", "ran_by", "test_number", "stage"]
    t = Excel_Template(names.__len__(), names, "data")

    row = 2
    blank_row = [""] * keys.__len__()

    for x in tests.data:
        tmp = [""] * keys.__len__()
        for key in x.keys():
            for i in range(0, keys.__len__()):
                if key == keys[i]:
                    try:
                        tmp[i] = float(x[keys[i]])
                    except:
                        tmp[i] = x[keys[i]]
                    break

        t.write_row(row, tmp, "data")
        row += 1

    t.save(dirname+"/tests.xlsx")

    print "Wrote", tests.length, "rows"
    print "All Done"


# handle_orders()
# handle_tests()