def check_missing_elements(input_list, n):
    '''Checks which elements are missing in the input_list to get the list from 1 till n'''
    difference =  list(set(range(1, n + 1)) - set(input_list))
    return difference

print (check_missing_elements([2,3,7,4,9], 10))