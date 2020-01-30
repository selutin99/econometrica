import numpy as np

import core.average_params as avg
import core.checker as ch


def mean_linear_deviation(data):
    """
    Calculate simple linear deviation
    :param data: list of int or float values
    :return: linear deviation
    """
    if ch.check_list(data):
        mean = avg.average(data)
        n = len(data)
        d = 0
        for element in data:
            d += np.fabs(element - mean)
        return d / n


def dispersion(data):
    """
    Calculate dispersion 
    :param data: list of int or float values
    :return: (sigma^2)
    """
    if ch.check_list(data):
        mean = avg.average(data)
        n = len(data)
        d = 0
        for element in data:
            d += (element - mean) ** 2
        return d / n


def sample_dispersion(data):
    """
    Calculate sample dispersion 
    :param data: list of int or float values
    :return: S^2
    """
    if ch.check_list(data):
        n = len(data)
        d = 0
        for element in data:
            d += element ** 2
        return (d / n) - (avg.average(data) ** 2)


def unbiased_variance_estimate(data):
    """
    Calculate dispersion variance 
    :param data: list of int or float values
    :return: dict with variance estimate and sqrt of dispersion variance
    """
    if ch.check_list(data):
        mean = avg.average(data)
        n = len(data)
        d = 0
        for element in data:
            d += (element - mean) ** 2
        return {'S2': d / (n - 1), 's': np.sqrt(d / (n - 1))}


def standard_deviation(data):
    """
    Calculate simple standard deviation
    :param data: list of int or float values
    :return: standard deviation
    """
    if ch.check_list(data):
        return np.sqrt(dispersion(data))


def sample_deviation(data):
    """
    Calculate sample deviation
    :param data: list of int or float values
    :return: sample deviation
    """
    if ch.check_list(data):
        return np.sqrt(sample_dispersion(data))


def SEM(data):
    """
    Calculate standard error of the mean
    :param data: list of int or float values
    :return: standard error of the mean
    """
    if ch.check_list(data):
        return standard_deviation(data) / len(data)


def confidence_interval(data):
    """
    Calculate confidence interval for mean
    :param data: list of int or float values
    :return: list with confidence interval
    """
    if ch.check_list(data):
        return [avg.average(data) - (1.96 * SEM(data)), avg.average(data) + (1.96 * SEM(data))]
