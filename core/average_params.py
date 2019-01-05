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

def harmonic_mean(data):
    """
    Calculate harmonic mean
    :param data: list of int or float values
    :return: harmonic mean of int or float list
    """
    if (ch.check_list(data) == True):
        sum = 0
        for elem in data:
            sum += 1/elem
        return len(data)/sum

def square_mean(data):
    """
    Calculate square mean
    :param data: list of int or float values
    :return: square mean of int or float list
    """
    if (ch.check_list(data) == True):
        sum = 0
        for elem in data:
            sum += elem*elem
        return (sum/len(data))**0.5