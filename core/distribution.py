import core.checker as ch
import core.average_params as avg
import core.variations.variations_indicators as vars

def moment_3(data):
    """
    Calculate central moment of the third order
    :param data: list of int or float values
    :return: value of central moment
    """
    if (ch.check_list(data) == True):
        mean = avg.average(data)
        M = 0
        for element in data:
            M+=(element-mean)**3
        return M/len(data)

def asymmetry_coefficient(data):
    """
    Calculate asymmetry coefficient
    :param data: list of int or float values
    :return: value of asymmetry coefficient
    """
    if (ch.check_list(data) == True):
        return moment_3(data)/(vars.standard_deviation(data)**3)