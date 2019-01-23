def check_list(data):
    """
    Function return True if param data is list and this param non empty
    """
    if type(data) is list:
        if(len(data)>0 and data!=[]):
            if(all(isinstance(i, (int, float)) for i in data)):
                return True
            else:
                raise ValueError('List values must be int or float')
        else:
            raise ValueError('List is must be non empty')
    else:
        raise ValueError('Data is must be as list')

def check_degree(value):
    """
    :param value: positive integer number
    :return: true or error
    """
    if type(value) is int:
        if(value>0):
            return True
        else:
            raise ValueError('Degree must be positive')
    else:
        raise ValueError('Degree must be integer')

def check_equality(list1, list2):
    """
    Function return True if 2 inputs 
    params length is equal
    """
    if(len(list1)==len(list2)):
        return True
    else:
        raise ValueError('Length of list must be equal')

def check_probability(list):
    """
    Function return True if sum of list is 1
    """
    if (check_list(list) == True):
        if(sum(list)==1 or sum(list)==1.0):
            return True
        else:
            raise ValueError('Probability must be equal to 1')