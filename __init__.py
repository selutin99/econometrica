import core.regression.сorrelation as cor

if __name__ == '__main__':
    x = [10, 12, 15, 17, 18, 19, 19, 20, 20, 21]
    y = [6, 6, 7, 7, 7, 8, 8, 9, 9, 10]
    z = [1,2,3,4,5,6]
    print(cor.pearson_correltaion(x,y))