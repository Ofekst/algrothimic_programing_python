def dnc(baseFunc, combineFunc):
    def recursive_seperate(array):
        if len(array) == 1:
            return baseFunc(array[0])
        mid = len(array) // 2
        left_array = recursive_seperate(array[:mid])
        right_array = recursive_seperate(array[mid:])
        return combineFunc(left_array, right_array)
    return recursive_seperate



def maxAreaHist(hist):
    def get_min_index(start,end):
        min_index = start
        for i in range(start,end):
            if hist[i] < hist[min_index]:
                min_index = i
        return min_index

    def recursive_max_area_hist(start,end):
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

