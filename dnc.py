def dnc(baseFunc, combineFunc):
    """
    A general-purpose divide and conquer (DnC) higher-order function.
    :param baseFunc: A function to apply to a single element (base case).
    :param combineFunc: A function to combine two results.

    :return: A recursive function that applies divide and conquer on a list.
    """
    def recursive_seperate(array):
        """
        Recursively divides the array and combines results using baseFunc and combineFunc.
        :param array: The input list to process.
        :return: Result after recursively applying baseFunc and combineFunc
        """
        if len(array) == 1:
            return baseFunc(array[0])
        mid = len(array) // 2
        left_array = recursive_seperate(array[:mid])
        right_array = recursive_seperate(array[mid:])
        return combineFunc(left_array, right_array)
    return recursive_seperate



def maxAreaHist(hist):
    """
    Computes the maximum rectangular area under a histogram using a divide and conquer approach.

    :param hist: A list of integers representing bar heights in the histogram.
    :return: The area of the largest rectangle under the histogram.
    """
    def get_min_index(start,end):
        """
        Finds the index of the smallest bar in hist[start:end].

        :param start: Starting index
        :param end: Ending index
        :return: Index of the minimum height bar in the given range.
        """
        min_index = start
        for i in range(start,end):
            if hist[i] < hist[min_index]:
                min_index = i
        return min_index

    def recursive_max_area_hist(start,end):
        """
        Recursively computes the largest rectangle in the histogram using divide and conquer.

        :param start: Starting index
        :param end: Ending index
        :return: Maximum area found in the current subrange.
        """
        if start == end:
            return 0
        if start + 1 == end:
            return hist[start]

        min_index = get_min_index(start,end)
        current_min_area = hist[min_index] * (end - start)
        left_array = recursive_max_area_hist(start,min_index)
        right_array = recursive_max_area_hist(min_index + 1,end)

        return max(current_min_area, left_array , right_array)
    return recursive_max_area_hist(0,len(hist))

