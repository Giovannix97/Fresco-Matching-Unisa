import statistics


def is_int_number_even(number):
    if (number % 2) == 0:
        return True

    return False


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
    return int(statistics.mean(values))


def calculate_int_median(values):
    """
        Get int median

        :param values: A list of n values
        :return: An int value that represents the median value.
        """
    return int(statistics.median(values))
