def new_list():
    return {
        'first': None,
        'last': None,
        'size': 0
    }

def is_empty(my_list):
    return my_list["size"] == 0

def size(my_list):
    return my_list["size"]

def add_first(my_list, element):
    new_node = {
        "info": element,
        "next": my_list["first"]
    }
    my_list["first"] = new_node
    if my_list["last"] is None:
        my_list["last"] = new_node
    my_list["size"] += 1

def add_last(my_list, element):
    new_node = {
        "info": element,
        "next": None
    }
    if my_list["first"] is None:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node 
        my_list["last"] = new_node
    my_list["size"] += 1
    
def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["first"]["info"]
    
def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]["info"]
    
def get_element(my_list, pos):
    if pos < 1 or pos > my_list["size"]:
        raise Exception('IndexError: list index out of range')

    searchpos = 1
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]
    
def delete_element(my_list, pos):
    if pos < 1 or pos > my_list["size"]:
        raise IndexError("list index out of range")

    if pos == 1:
        my_list["first"] = my_list["first"]["next"]
        if my_list["first"] is None:
            my_list["last"] = None
    else:
        searchpos = 1
        node = my_list["first"]
        while searchpos < pos - 1:
            node = node["next"]
            searchpos += 1

        if node["next"] == my_list["last"]:
            my_list["last"] = node
        
        node["next"] = node["next"]["next"]

    my_list["size"] -= 1
    return my_list

    
def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    first = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    if my_list["first"] is None:
        my_list["last"] = None
    my_list["size"] -= 1
    return first

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    last = my_list["last"]["info"]
    if my_list["first"] == my_list["last"]:
        my_list["first"] = None
        my_list["last"] = None
    else:
        temp = my_list["first"]
        while temp["next"] != my_list["last"]:
            temp = temp["next"]
        my_list["last"] = temp
        my_list["last"]["next"] = None
    my_list["size"] -= 1
    return last

def insert_element(my_list, pos, element):
    if pos < 1 or pos > my_list["size"] + 1:
        raise Exception('IndexError: list index out of range')
    
    new_node = {
        "info": element,
        "next": None
    }
    
    if pos == 1:
        add_first(my_list, element)
    elif pos == my_list["size"] + 1:
        add_last(my_list, element)
    else:
        searchpos = 1
        node = my_list["first"]
        while searchpos < pos - 1:
            node = node["next"]
            searchpos += 1

        new_node["next"] = node["next"]
        node["next"] = new_node

    my_list["size"] += 1
    return my_list


def is_present(my_list, element, cmp_function):
    temp = my_list["first"]
    count = 1
    while temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            return count
        temp = temp["next"]
        count += 1
    return -1

def change_info(my_list, pos, element):
    if pos < 1 or pos > my_list["size"]:
        raise Exception('IndexError: list index out of range')

    node = my_list["first"]
    for _ in range(pos - 1):
        node = node["next"]

    node["info"] = element 
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 1 or pos1 > my_list["size"] or pos2 < 1 or pos2 > my_list["size"]:
        raise Exception('IndexError: list index out of range')

    if pos1 == pos2:
        return my_list
    
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1

    node1 = my_list["first"]
    node2 = my_list["first"]

    for i in range(1, max(pos1, pos2) + 1):
        if i == pos1:
            node1 = node2
        if i == pos2:
            break
        node2 = node2["next"]

    node1["info"], node2["info"] = node2["info"], node1["info"]

    return my_list

def sub_list(my_list, start_index, length):
    if start_index < 1 or start_index > my_list["size"] or start_index + length - 1 > my_list["size"]:
        raise IndexError("list index out of range")

    sub_list = new_list()
    temp = my_list["first"]

    for _ in range(start_index - 1):
        temp = temp["next"]

    for _ in range(length):
        add_last(sub_list, temp["info"])
        temp = temp["next"]

    return sub_list