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

def check_equality(list1, list2):
    """
    Function return True if 2 inputs 
    params length is equal
    """
    if(len(list1)==len(list2)):
        return True
    else:
        raise ValueError('Length of list must be equal')