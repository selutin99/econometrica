import core.regression.сorrelation as cor
import core.variations.variations_indicators as vars
import core.base_functions as base
import core.distribution as dist

if __name__ == '__main__':
    x = [10, 12, 15, 17, 18, 19, 19, 20, 20, 21]
    y = [6, 6, 7, 7, 7, 8, 8, 9, 9, 10]
    z = [1,2,3,4,4,4,5,5,6,8]

    print(dist.asymmetry_coefficient(z)/dist.asymmetry_estimation(z))