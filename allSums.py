def allSumsDP(arr):
    """
    Computes all possible subset sums that can
    be formed from the given list of integers.
    :param arr: list of integers.
    :return: set containing all possible sums that can
    be formed from subsets of arr
    """
    all_sum_set = {0}

    for num in arr:
        new_sums = set()
        for sum in all_sum_set:
            new_sums.add(sum + num)
        all_sum_set.update(new_sums)
    return all_sum_set