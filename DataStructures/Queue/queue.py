import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataStructures.List import array_list as al

class EmptyStructureError(Exception):
    pass

def new_queue():
    return al.new_list()

def enqueue(my_queue, element):
    return al.add_last(my_queue, element)

def dequeue(my_queue):
    if is_empty(my_queue):
        raise EmptyStructureError("queue is empty")
    return al.remove_first(my_queue)

def peek(my_queue):
    if is_empty(my_queue):
        raise EmptyStructureError("queue is empty")
    return al.first_element(my_queue)

def is_empty(my_queue):
    return al.is_empty(my_queue)

def size(my_queue):
    return al.size(my_queue)