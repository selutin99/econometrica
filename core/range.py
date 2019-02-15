import core.checker as ch

def range_sort(data, order=False):
    """
    Sort list of data by ascending and range by ascending
    :param data: list of int or float values
    :param order: ascending or descending sort
    :return: dictionary with serial number
    """
    if ch.check_list(data) and ch.check_boolean(order):
        data.sort(reverse=order)
        dict = {}
        j = 1
        for i in data:
            dict.update({j:i})
            j += 1
        return dict

def rank_simple(data):
    return sorted(range(len(data)), key=data.__getitem__)

def rank_data(data):
    """
    Rank by averages
    :param data: list of int or float values
    :return: list with new rank values
    """
    n = len(data)
    ivec = rank_simple(data)
    svec = [data[rank] for rank in ivec]
    sum_ranks = 0
    dup_count = 0
    new_array = [0]*n
    for i in range(n):
        sum_ranks += i
        dup_count += 1
        if i == n-1 or svec[i] != svec[i+1]:
            averank = sum_ranks / float(dup_count) + 1
            for j in range(i-dup_count+1, i+1):
                new_array[ivec[j]] = averank
            sum_ranks = 0
            dup_count = 0
    return new_array

def check_range_correct(data):
    if ch.check_list(data):
        s = (len(data)*(1+len(data)))/2
        return sum(rank_data(data))==s