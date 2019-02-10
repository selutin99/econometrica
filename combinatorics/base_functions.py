import core.checker as ch

def factorial(n):
    """
    :return: returns the factorial of a number
    """
    if (ch.check_number(n) == True):
        i = 1
        fact = 1
        while(i<=n):
            fact *= i
            i+=1
        return fact

def combinations(n, m):
    """
    :return: number of combinations of n by m
    """
    if(ch.check_number(n) and ch.check_number(m)):
        return factorial(n)/(factorial(m)*factorial(n-m))

def accommodations(n, k):
    """
    :return: the number of allocations of n elements in k
    """
    if ch.check_number(n) and ch.check_number(k):
        return factorial(n) / factorial(n - k)