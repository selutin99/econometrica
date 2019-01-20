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

def unbiased_variance_estimate(data):
    """
    Calculate dispersion variance 
    :param data: list of int or float values
    :return: dict with variance estimate and sqrt of dispersion variance
    """
    if (ch.check_list(data) == True):
        mean = avg.average(data)
        n = len(data)
        d = 0
        for element in data:
            d += (element - mean)**2
        return {'S2': d/(n-1), 's': math.sqrt(d/(n-1))}

def standard_deviation(data):
    """
    Calculate simple standard deviation
    :param data: list of int or float values
    :return: standard deviation
    """
    if (ch.check_list(data) == True):
        return math.sqrt(dispersion(data))

def SEM(data):
    """
    Calculate standard error of the mean
    :param data: list of int or float values
    :return: standard error of the mean
    """
    if (ch.check_list(data) == True):
        return standard_deviation(data)/len(data)

def confidence_interval(data):
    """
    Calculate confidence interval for mean
    :param data: list of int or float values
    :return: list with confidence interval
    """
    if (ch.check_list(data) == True):
        return [avg.average(data)-(1.96*SEM(data)), avg.average(data)+(1.96*SEM(data))]