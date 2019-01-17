import core.regression.сorrelation as cor
import core.variations.variations_indicators as vars
import core.base_functions as base

if __name__ == '__main__':
    x = [10, 12, 15, 17, 18, 19, 19, 20, 20, 21]
    y = [6, 6, 7, 7, 7, 8, 8, 9, 9, 10]
    z = [14,12,2,35,4]
    #print(base.quartile(z)['q3'])
    print(vars.standard_deviation(z))