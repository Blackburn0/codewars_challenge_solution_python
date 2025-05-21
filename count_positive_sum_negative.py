def count_positives_sum_negatives(arr):
    # count positive number in the list
    new_arr = []
    positive_number = []
    sum_of_negative_number = []
    
    if not arr:
        return arr
    else:
        for item in arr:
            if item > 0:
                positive_number.append(item)
            else:
                sum_of_negative_number.append(item)

    x = len(positive_number)
    new_arr.append(x)
    new_arr.append(sum(sum_of_negative_number))
    return new_arr
