def sort_array(array: []) -> []:
    for i in range(1, len(array)):
        j = i - 1
        current_value = array[i]
        while j >= 0:
            if array[j] < current_value:
                break
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = current_value
    return array
