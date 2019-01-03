import core.checker as ch

def average(data):
    """
    Calculate average of list
    :param data: list of int or float values
    :return: average of list
    """
    if(ch.check_list(data)==True):
        return sum(data) / len(data)

def geometric_mean(data):
    """
    Calculate geometric mean
    :param data: list of int or float values
    :return: geometric mean of int or float list
    """
    if (ch.check_list(data) == True):
        multiplier = 1
        for elem in data:
            multiplier *= elem
        return multiplier**(1/len(data))

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

def frequency(data):
    """
    Find frequencies of list
    :param data: list of int or float values
    :return: list with dictionary of frequencies and sum of frequencies
    """
    if (ch.check_list(data) == True):
        return [{x: data.count(x) for x in data}, len(data)]