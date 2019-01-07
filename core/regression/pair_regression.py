import numpy as np

import core.checker as ch

def pair_regression(x, y):
    """Find pair regression equation
    :param x: list of dependent variable
    :param y: list of independent variable
    :return: list with coefficients of regression 
             and string with regression equation 
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
            equation = "y = "+str(system[1])+" x + ("+str(system[0])+")"
            result = system.tolist()
            result.append(equation)
            return result