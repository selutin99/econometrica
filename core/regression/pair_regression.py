import numpy as np

import core.average_params as avg
import core.checker as ch
import core.variations.variations_indicators as vars


def pair_regression(x, y):
    """Find pair regression equation
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: dictionary with coefficients of regression 
    """
    if ch.check_list(x) and ch.check_list(y):
        if ch.check_equality(x, y):
            x2 = 0
            for elem in x:
                x2 += elem * elem
            xy = 0
            for xelem, yelem in zip(x, y):
                xy += xelem * yelem
            a = np.array([[len(x), sum(x)], [sum(x), x2]])
            b = np.array([sum(y), xy])

            system = np.linalg.solve(a, b)
            result = system.tolist()
            return {'a': result[0], 'b': result[1]}


def covariation(x, y):
    """Find covariation coefficient
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of covariation coefficient
    """
    if ch.check_list(x) and ch.check_list(y):
        if ch.check_equality(x, y):
            return avg.sample_average(x, y) - (avg.average(x) * avg.average(y))


def closure_coefficient(x, y):
    """Find closure indicator
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of closure indicator
    """
    if ch.check_list(x) and ch.check_list(y):
        if ch.check_equality(x, y):
            numerator = avg.sample_average(x, y) - (avg.average(x) * avg.average(y))
            denumerator = vars.sample_deviation(x) * vars.sample_deviation(y)
            return numerator / denumerator


def yx(x, y):
    """Auxiliary function for approximation error
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: list of regression values
    """
    if ch.check_list(x) and ch.check_list(y):
        if ch.check_equality(x, y):
            yxl = []
            a = pair_regression(x, y)['a']
            b = pair_regression(x, y)['b']

            for xi in x:
                yxl.append(b * xi + a)
            return yxl


def approximation_error(x, y):
    """Find approximation error
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value in percent of approximation error
    """
    if ch.check_list(x) and ch.check_list(y):
        if ch.check_equality(x, y):
            yxl = yx(x, y)
            a = 0
            for yi, yxli in zip(y, yxl):
                a += (np.fabs(yi - yxli)) / yi
            return 100 * (a / len(y))


def dispersion_error_equation(x, y, m):
    """
    Dispersion error equations
    :param x: list of dependent variable
    :param y: list of independent variable
    :param m: the number of influencing factors in the trend model
    :return: value of dispersion error
    """
    if ch.check_list(x) and ch.check_list(y):
        if ch.check_equality(x, y) and ch.check_number(m):
            numerator = 0
            yxl = yx(x, y)
            for yi, yxl in zip(y, yxl):
                numerator += (yi - yxl) ** 2
            return numerator / (len(y) - m - 1)


def durbin_watson(x, y):
    """
    Find value for Durbin-Watrson criteria
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of Durbin-Watrson criteria
    """
    if ch.check_list(x) and ch.check_list(y):
        if ch.check_equality(x, y):
            yx_list = yx(x, y)
            e = []
            for yi, yxi in zip(y, yx_list):
                e.append(yi - yxi)
            i = 0
            e_ei = []
            e_2 = []
            for ei in e:
                e_2.append(ei ** 2)
                if i == 0:
                    i += 1
                    continue
                else:
                    e_ei.append((e[i] - e[i - 1]) ** 2)
                i += 1
            return sum(e_ei) / sum(e_2)


def total_amount(x, y, p=2):
    """
    Find value total amount
    :param x: list of dependent variable
    :param y: list of independent variable
    :param p: number of factors
    :return: value of total amount
    """
    if ch.check_list(x) and ch.check_list(y):
        if ch.check_equality(x, y):
            x2 = []
            y2 = []
            xavg = avg.average(x)
            yavg = avg.average(y)

            xyavg = (xavg + yavg) / 2
            for xi, yi in zip(x, y):
                x2.append(xi * xi)
                y2.append(yi * yi)
            return sum(x2) + sum(y2) - len(x) * p * (xyavg * xyavg)


def sf(x, y, p=2):
    """
    Find value sum for factor dispersion
    :param x: list of dependent variable
    :param y: list of independent variable
    :param p: number of factors
    :return: value of sum for factor dispersion
    """
    if ch.check_list(x) and ch.check_list(y) :
        if ch.check_equality(x, y):
            xavg = avg.average(x)
            yavg = avg.average(y)
            xyavg = (xavg + yavg) / 2
            return len(x) * (xavg ** 2 + yavg ** 2 - p * (xyavg ** 2))


def sost(x, y):
    """
    Find value remains
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: value of remains
    """
    if ch.check_list(x) and ch.check_list(y):
        if ch.check_equality(x, y):
            return total_amount(x, y) - sf(x, y)


def factor_dispersion(x, y, p=2):
    """
    Find value of factor dispersion
    :param x: list of dependent variable
    :param y: list of independent variable
    :param p: number of factors
    :return: value of factor dispersion
    """
    if ch.check_list(x) and ch.check_list(y):
        if ch.check_equality(x, y):
            return sf(x, y) / (p - 1)


def sost_dispersion(x, y, p=2):
    """
    Find value of ost dispersion
    :param x: list of dependent variable
    :param y: list of independent variable
    :param p: number of factors
    :return: value of ost dispersion
    """
    if ch.check_list(x) and ch.check_list(y):
        if ch.check_equality(x, y):
            return sost(x, y) / (p * (len(x) - 1))
