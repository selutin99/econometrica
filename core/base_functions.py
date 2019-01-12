import core.checker as ch
import math

def range(data):
    """
    Find range of data list
    :param data: list of int or float values
    :return: max value of list minus min value of list
    """
    if (ch.check_list(data) == True):
        return max(data) - min(data)

def capacity(data):
    """
    Find length of list
    :param data: list of int or float values
    :return: list length
    """
    if (ch.check_list(data) == True):
        return len(data)

def mode(data):
    """
    Calculate most common use element in list
    :param data: list of int or float values
    :return: mode of list
    """
    if (ch.check_list(data) == True):
        most = max(list(map(data.count, data)))
        return list(set(filter(lambda x: data.count(x) == most, data)))

def median(data):
    """
    Calculate median of data list
    :param data: list of int or float values
    :return: median
    """
    if (ch.check_list(data) == True):
        data.sort()
        print(data)
        if(len(data)%2!=0):
            return data[len(data)//2]
        else:
            return (data[(len(data)//2)-1]+data[len(data)//2])/2

def frequency(data):
    """
    Find frequencies of list
    :param data: list of int or float values
    :return: list with dictionary of frequencies and sum of frequencies
    """
    if (ch.check_list(data) == True):
        return [{x: data.count(x) for x in data}, len(data)]