
def new_list():
    new_list = {
        'size': 0, 
        'elements': []
    }
    return new_list

def is_empty(my_list):
    return my_list["size"] == 0

def size(my_list):
    return my_list["size"]

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return get_element(my_list, 0)

def last_element(my_list): 
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return get_element(my_list, size(my_list) - 1)

def get_element(my_list, index):
    if index >= 1 or index <= my_list["size"]:
        return my_list["elements"][index - 1]
    else:
        raise Exception('IndexError: list index out of range')

def delete_element(my_list, index):
    if index >= 1 and index <= my_list["size"]:
        my_list["elements"].pop(index - 1)
        my_list["size"] -= 1
    else:
        raise Exception('IndexError: list index out of range')
    return my_list

def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        first = my_list["elements"].pop(0)
        return first
    
def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        last = my_list["elements"].pop()
        return last

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def insert_element(my_list, index, element):
    if index >= 1 and index <= my_list["size"] + 1:
        my_list["elements"].insert(index - 1, element)
        my_list["size"] += 1
    else:
        raise Exception('IndexError: list index out of range')
    return my_list

def change_info(my_list, index, new_info):
    if index >= 1 and index <= my_list["size"]:
        my_list["elements"][index - 1] = new_info
    else:
        raise Exception('IndexError: list index out of range')
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 >= 1 and pos1 <= my_list["size"] and pos2 >= 1 and pos2 <= my_list["size"]:
        temp = my_list["elements"][pos1 - 1]
        my_list["elements"][pos1 - 1] = my_list["elements"][pos2 - 1]
        my_list["elements"][pos2 - 1] = temp
    else:
        raise Exception('IndexError: list index out of range')
    return my_list

def sub_list(my_list, start_index, lenght):
    if start_index >= 1 and start_index <= my_list["size"] and start_index + lenght - 1 <= my_list["size"]:
        sub_list = new_list()
        for i in range(start_index, start_index + lenght):
            add_last(sub_list, my_list["elements"][i - 1])
    else:
        raise Exception('IndexError: list index out of range')
    return sub_list
