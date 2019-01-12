import core.checker as ch
import core.average_params as avg

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