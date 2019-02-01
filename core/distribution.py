import core.checker as ch
import core.average_params as avg
import core.variations.variations_indicators as vars

import numpy as np

def moment(data, degree):
    """
    Calculate central moments
    :param data: list of int or float values
    :return: value of central moment
    """
    if (ch.check_list(data) == True and ch.check_number(degree) == True):
        mean = avg.average(data)
        M = 0
        for element in data:
            M+=(element-mean)**degree
        return M/len(data)

def asymmetry_coefficient(data):
    """
    Calculate asymmetry coefficient
    :param data: list of int or float values
    :return: value of asymmetry coefficient
    """
    if (ch.check_list(data) == True):
        return moment(data, degree=3)/(vars.standard_deviation(data)**3)

def asymmetry_estimation(data):
    """
    Calculate value of assymetry estimation
    :param data: list of int or float values
    :return: value of assymetry estimation
    """
    if (ch.check_list(data) == True):
        n = len(data)

        numerator = 6*(n-2)
        denominator = (n+1)*(n+3)

        return np.sqrt(numerator/denominator)

def kurtosis(data):
    """
    Calculate rate of kurtosis
    :param data: list of int or float values
    :return: value of kurtosis
    """
    if (ch.check_list(data) == True):
        return (moment(data, degree=4)/vars.standard_deviation(data)**4)-3