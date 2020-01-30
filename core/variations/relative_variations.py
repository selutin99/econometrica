import core.average_params as avg
import core.base_functions as base
import core.checker as ch
import core.variations.variations_indicators as vars


def oscillation_coefficient(data):
    """
    Calculate coefficient of oscillation
    :param data: list of int or float values
    :return: oscillation coefficient
    """
    if ch.check_list(data):
        R = base.range(data)
        x = avg.average(data)
        return R / x


def relative_linear_deviation(data):
    """
    Calculate linear deviation coefficient
    :param data: list of int or float values
    :return: relative linear deviation coefficient
    """
    if ch.check_list(data):
        d = vars.mean_linear_deviation(data)
        x = avg.average(data)
        return d / x


def coefficient_of_variation(data):
    """
    Calculate coefficient of variation
    :param data: list of int or float values
    :return: variation coefficient
    """
    if ch.check_list(data):
        b = vars.standard_deviation(data)
        x = avg.average(data)
        return b / x
