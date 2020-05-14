def calculate_percentage(value, total):
    """
    A simple method to calculate percentage
    :param value:
    :param total:
    :return:
    """
    return (value * 100) / total

def calculate_int_average(values):
    """
    Get int average

    :param values: A list of n values
    :return: An int value that represents an average.
    """
    total = 0
    number_of_elements = len(values)
    for value in values:
        total += value

    return int(total/number_of_elements)