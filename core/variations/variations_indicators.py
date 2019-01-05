import core.checker as ch
import core.average_params as avg
import math

def mean_linear_deviation(data):
    """
    Calculate simple linear deviation
    :param data: list of int or float values
    :return: linear deviation
    """
    if(ch.check_list(data)==True):
        mean = avg.average(data)
        n = len(data)
        d = 0
        for element in data:
            d += math.fabs(element-mean)
        return d/n

def dispersion(data):
    """
    Calculate dispersion 
    :param data: list of int or float values
    :return: (sigma^2)
    """
    if (ch.check_list(data) == True):
        mean = avg.average(data)
        n = len(data)
        d = 0
        for element in data:
            d += (element - mean)**2
        return d / n

def standard_deviation(data):
    """
    Calculate simple standard deviation
    :param data: list of int or float values
    :return: standard deviation
    """
    if (ch.check_list(data) == True):
        return math.sqrt(dispersion(data))