import core.regression.сorrelation as cor
import core.variations.variations_indicators as vars

if __name__ == '__main__':
    x = [10, 12, 15, 17, 18, 19, 19, 20, 20, 21]
    y = [6, 6, 7, 7, 7, 8, 8, 9, 9, 10]
    z = [1,2,3,4,5,6]
    print(vars.confidence_interval(z))