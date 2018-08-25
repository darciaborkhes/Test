def generate_decimals(start=2, end=5.5, step=0.5):
    '''Function that generates a list of decimal numbers from start=2 till end=5.5 with the step 0.5,
    if other values are not passed'''
    current = start
    result = []
    while current <= end:
        result.append(current)
        current += step
    return result


print(generate_decimals())

