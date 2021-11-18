# Write a function do_math that takes in an array of integers and returns its sum, max, average and median

my_array = [2,3,4,6,7,8]
def do_math(array):
    max_num = array[0]
    sum = 0
    sorted_array = sorted(array)
    index = (len(array)-1) //2
    if len(array) % 2:
        return sorted_array[index]
    else:
        return (sorted_array[index] + sorted_array[index + 1])/2.0
    for index in range(len(array)):
        sum += array[index]
        
        if array[index] >= max_num:
            max_num = array[index]
    return [max_num, (sum/len(array))]

print(do_math(my_array))
