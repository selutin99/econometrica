def check_list(data):
    """
    Function return True if param data is list and this param non empty
    """
    if type(data) is list:
        if(len(data)>0 and data!=[]):
            return True
        else:
            raise ValueError('List is must be non empty')
    else:
        raise ValueError('Data is must be as list')