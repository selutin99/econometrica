from core.regression.сorrelation import fisher_criteria
import core.regression.сorrelation as cor
import core.average_params as avg

import core.variations.variations_indicators as vars

import combinatorics.base_functions as com

if __name__ == '__main__':
    x = [10, 12, 15, 17, 18, 19, 19, 20, 20, 21]
    y = [6, 6, 7, 7, 7, 8, 8, 9, 9, 10]
    z = [1,2,3,4,4,4,5,5,6,8]

    #x = [1,2,3,4,5,6]
    q = [0.2,0.1,0.4,0.1,0.1,0.1]

    print(com.accommodations(10, 6))