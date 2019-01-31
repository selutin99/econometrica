import core.checker as ch
import core.average_params as avg

import core.regression.pair_regression as regr
import core.variations.variations_indicators as vars

import math

def pearson_correltaion(x, y):
    """Finds the Pearson correlation coefficient.
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value with value of correlation coefficient
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if(ch.check_equality(x,y) == True):
            avg_x = avg.average(x)
            avg_y = avg.average(y)
            diffprod = 0
            xdiff2 = 0
            ydiff2 = 0
            for idx in range(len(x)):
                xdiff = x[idx] - avg_x
                ydiff = y[idx] - avg_y
                diffprod += xdiff * ydiff
                xdiff2 += xdiff * xdiff
                ydiff2 += ydiff * ydiff
            return diffprod / math.sqrt(xdiff2 * ydiff2)

def beta_coefficient(x, y):
    """
    Finds beta coefficient
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of beta coefficient
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if(ch.check_equality(x, y) == True):
            return regr.pair_regression(x, y)['b'] * (vars.sample_deviation(x)/vars.sample_deviation(y))

def determination_coefficient(x, y):
    """
    Finds determination coefficient
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of determination coefficient
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if (ch.check_equality(x, y) == True):
            return beta_coefficient(x, y)**2

def significance(x, y):
    """
    Finds significance of correlation coefficient
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of significance of correlation coefficient
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if(ch.check_equality(x, y) == True):
            b = beta_coefficient(x, y)
            n = len(x)
            numerator = b*math.sqrt(n-2)
            denumerator = math.sqrt(1-b*b)

            return numerator/denumerator

def elastic_coefficient(x, y):
    """
    Finds elastic coefficient
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of elastic coefficient
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if(ch.check_equality(x, y) == True):
            return regr.pair_regression(x, y)['b']*(avg.average(x)/avg.average(y))