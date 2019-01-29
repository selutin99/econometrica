import numpy as np

import core.checker as ch
import core.variations.variations_indicators as vars
import core.average_params as avg

def pair_regression(x, y):
    """Find pair regression equation
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: dictionary with coefficients of regression 
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if(ch.check_equality(x,y) == True):
            x2 = 0
            for elem in x:
                x2 += elem*elem
            xy = 0
            for xelem, yelem in zip(x,y):
                xy += xelem*yelem
            a = np.array([[len(x), sum(x)],[sum(x), x2]])
            b = np.array([sum(y), xy])

            system = np.linalg.solve(a, b)
            result = system.tolist()
            return {'a': result[0], 'b': result[1]}

def covariation(x,y):
    """Find covariation coefficient
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of covariation coefficient
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if(ch.check_equality(x,y) == True):
            return avg.sample_average(x,y)-(avg.average(x)*avg.average(y))

def closure_coefficient(x,y):
    """Find closure indicator
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of closure indicator
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if(ch.check_equality(x,y) == True):
            numerator = avg.sample_average(x,y)-(avg.average(x)*avg.average(y))
            denumerator = vars.sample_deviation(x)*vars.sample_deviation(y)
            return numerator/denumerator
