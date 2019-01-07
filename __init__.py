import core.regression.pair_regression as reg

if __name__ == '__main__':
    x = [10, 12, 15, 17, 18, 19, 19, 20, 20, 21]
    y = [6, 6, 7, 7, 7, 8, 8, 9, 9, 10]
    print(reg.pair_regression(x,y))