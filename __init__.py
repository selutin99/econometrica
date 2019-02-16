import core.regression.сorrelation as cor
import core.regression.pair_regression as regr

import core.range as rn

if __name__ == '__main__':
    x = [10, 12, 15, 17, 18, 19, 19, 20, 20, 21]
    y = [6, 6, 7, 7, 7, 8, 8, 9, 9, 10]
    z = [1,2,3,4,4,4,5,5,6,8]

    #x = [1,2,3,4,5,6]
    q = [0.2,0.1,0.4,0.1,0.1,0.1]

    print(regr.sost_dispersion(x, y))