"""asd"""
from glob import glob
from time import time
from datetime import datetime

def take(name, price, dict_):
    """asd"""
    if not name in dict_:
        dict_[name] = float(price)
    else:
        dict_[name] += float(price)
    print ("Taking order from " + name + " for " + str(price))

def status(dict_):
    """asd"""
    for key in dict_:
        print (key + " - " + str(dict_[key]))

def save(dict_):
    """asd"""
    tss = time()
    stamp = datetime.fromtimestamp(tss).strftime('%Y_%m_%d_%H_%M_%S')

    file_ = open("orders_"+stamp,"w")
    for key in dict_:
        file_.write(key + " - " + str(dict_[key]) + "\n")

def list1():
    """asd"""
    list_ = glob("orders_*")
    for i in range(len(list_)):
        print ("[" + str(i+1) + "] - " + list_[i])
    return list_

def load(number, list_, dict_):
    """asd"""
    file_name = list_[number - 1]
    file_ = open(file_name, "r")

    contents = file_.read()
    contents = contents.splitlines()

    dict_.clear()

    for item in contents:
        temp = item.split(" ")
        dict_[temp[0]] = float(temp[2])



def main():
    """madafaka"""
    is_running = True
    dict_ = {}
    is_changed_f = False
    is_changed_l = False
    list_ = []


    while is_running:
        command = input("Enter command>")
        command = command.split(" ")
        if command[0] == "take" and len(command) >= 3:
            take(command[1], float(command[2]), dict_)
            is_changed_f = True
            is_changed_l = True
        elif command[0] == "status":
            status(dict_)
        elif command[0] == "save":
            if len(dict_) > 0:
                save(dict_)
                is_changed_f = False
                is_changed_l = False

        elif command[0] == "list":
            list_ = list1()
        elif command[0] == "load":
            if len(list_) == 0:
                print ("Use list command before loading")
            elif is_changed_l == True:
                print ("You have not saved the current order." +
                    "If you wish to discard it, type load <number> again.")
                is_changed_l = False
            else:
                load(int(command[1]), list_, dict_)
        elif command[0] == "finish":
            if is_changed_f == False:
                is_running = False
        else:
            print ("Unknown command!")
if __name__ == '__main__':
    main()
