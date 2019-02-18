import core.checker as ch
import core.average_params as avg

import core.regression.pair_regression as regression
import core.variations.variations_indicators as vars

import numpy as np

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
            return diffprod / np.sqrt(xdiff2 * ydiff2)

def cheddock_scale(value):
    """
    Find Cheddock scale importance
    :param value: value of correlation
    :return: string value by Cheddock scale
    """
    if ch.check_probability_value(value):
        if 0.0 <= value < 0.3:
            return "Weak correlation"
        if 0.3 <= value < 0.5:
            return "Moderate correlation"
        if 0.5 <= value < 0.7:
            return "Noticeable correlation"
        if 0.7 <= value < 0.9:
            return "High correlation"
        if 0.9 <= value <= 0.99:
            return "Very high correlation"
        return "Is it probability?"

def tail_coefficient(x, y):
    """
    Find tail mismatch coefficient
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of tail mismatch coefficient
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if(ch.check_equality(x,y) == True):
            numerator = 0
            denumerator = 0
            yxl = regression.yx(x, y)
            for yi, yxl in zip(y, yxl):
                numerator += (yi-yxl)**2
                denumerator += yxl**2
            return numerator/denumerator

def beta_coefficient(x, y):
    """
    Finds beta coefficient
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of beta coefficient
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if(ch.check_equality(x, y) == True):
            return regression.pair_regression(x, y)['b'] * (vars.sample_deviation(x)/vars.sample_deviation(y))

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
            numerator = b*np.sqrt(n-2)
            denumerator = np.sqrt(1-b*b)

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
            return regression.pair_regression(x, y)['b']*(avg.average(x)/avg.average(y))

def fisher_criteria(x, y, m):
    """
    Value of fisher criteria
    :param x: list of dependent variable
    :param y: list of independent variable
    :param m: the number of influencing factors in the trend model
    :return: value of fisher criteria
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if (ch.check_equality(x, y) == True and ch.check_number(m) == True):
             numerator = determination_coefficient(x,y) * (len(x)-m-1)
             denumerator = (1-determination_coefficient(x,y))*m
             return numerator/denumerator

def fehner_coefficient(x, y):
    """
    Value of fehner coefficient
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of fehner coefficient
    """
    if (ch.check_list(x) == True and ch.check_list(y) == True):
        if(ch.check_equality(x, y) == True):
            xa = avg.average(x)
            ya = avg.average(y)

            xlist = []
            ylist = []
            resulter = []

            for xi in x:
                if xi <= xa:
                    xlist.append("-")
                else:
                    xlist.append("+")
            for yi in y:
                if yi <= ya:
                    ylist.append("-")
                else:
                    ylist.append("+")

            for xi, yi in zip(xlist, ylist):
                if xi==yi:
                    resulter.append("A")
                else:
                    resulter.append("B")
            return (resulter.count("A")-resulter.count("B"))/(resulter.count("A")+resulter.count("B"))