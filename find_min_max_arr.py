# Given an array of numbers, find both the max and min using the fewest number of comparisons

"""
1. Simple brute force method
Store the first element as the current max and min values. Traverse the array comparing the elements with the current max and min and updating these
variables as appropriate. 
Algorithm can be represented by the following python code:
"""
def find_max_min1(arr):

    length = len(arr)
    if length == 0: return "List is Empty"

    current_max, current_min = arr[0], arr[0]   

    for i in range(1, length):
        if arr[i] > current_max:
            current_max = arr[i]
        elif arr[i] < current_min:
            current_min = arr[i]

    return current_max, current_min

"""
In the worst case, we make 2 comparisons for every element in the array, excluding the first element. 2(n-1) = 2n-2 comparisons.
Time complexity O(n). Space Complexity O(1). But we want to have fewer comparisons.
"""


"""
2. Recursive Divide and Conquer method
We can keep dividing the array into a left half and a right half. Each time we can recursively find the min and max of the left and right halves.
We then compare the max and min from both havles to get an overall max and min value.
Algorithm can be represented by the following python code:
"""
def find_min_max2(arr, low, high):  # initially low = 0 (index of 1st element in array), high = len(arr) - 1 (index of last element in array)

    if len(arr) == 0: return "List is Empty" # Edge case, list is empty

    # Base case 1: array has 1 element which is set to both the max and min
    if low == high:
        max = arr[low]
        min = arr[low]
        return max, min

    # Base case 2: array has 2 elements, compare to find max and min
    elif low + 1 == high:
        if arr[low] > arr[high]:
            max, min = arr[low], arr[high]
        else:
            max, min = arr[high], arr[low]
        return max, min 

    # if array has >2 elements 
    else: 
        mid = (low + high) // 2    # array will be split into 2 parts

        left_max, left_min   = find_min_max2(arr, low, mid)       # recursively find max and min for the left side
        right_max, right_min = find_min_max2(arr, mid + 1, high)  # recursively find max and min for right side

        if left_max > right_max:    # find the max and min from both sides
            max = left_max
        else:
            max = right_max

        if left_min < right_min:
            min = left_min
        else:
            min = right_min

    return max, min
"""
Not sure how many comparisons this algorithm does but it seems to be less than the first method.
"""


"""
3. Checking in pairs method
Instead of checking every number against the current max and min values, we can compare subsequent pairs in the array. The bigger number from the pair
could be a possible max, so compare it against the current max. The smaller number from the pair could be a possible min, so compare it against the 
current min. In each case only 3 comparisons are needed for every 2 elements.
Algorithm can be represented by the following python code:
"""
def find_max_min3(arr):

    length = len(arr)
    if length == 0: return "List is Empty"

    if (length % 2) != 0:                   # if the list is of odd length 
        current_max = current_min = arr[0]  # Set the first element as the current max and min, the rest of the list is of an even amount so can be split into pairs
        j = 1   # We've looked at 1 number so far

    else:                                   # list is of even length, see which of the first 2 elements is bigger/smaller
        if arr[0] > arr[1]:                 
            current_max, current_min = arr[0], arr[1]
        else:
            current_max, current_min = arr[1], arr[0]
        j = 2   # We've looked at 2 numberes so far

    for i in range(j, length - 1, 2):       # go from the number(s) we have looked at so far to the 2nd last element in array. Jumping by 2 each time

        if arr[i] > arr[i + 1]:             # First element from pair is bigger
            if arr[i] > current_max:        # First element is a possible max value
                current_max = arr[i]
            if arr[i + 1] < current_min:    # Second element is a possible min value
                current_min = arr[i + 1]

        else:                               # Second element from pair is bigger
            if arr[i + 1] > current_max:    # Second element is a possible max value
                current_max = arr[i + 1]    
            if arr[i] < current_min:        # First element is a possible min value
                current_min = arr[i]
        
    return current_max, current_min
"""
For every 2 numbers we are making only 3 comparisons; in method 1 we were making 4 comparisons in the worst case. 
This means we are making around ( 3*(n-1) ) / 2 comparisons if the array is of odd length and ( 3*(n-2) ) / 2 comparisons if the array is of even length
Both of which are less than 2n-2 we had in the first method.
Time complexity = O(n). Space complexity O(1). 
"""

a = [-5, 3, 0, 0, 1, 2, 40, 40, 7, -20, -2, 3, -400, 6]

print(find_max_min1(a))
print(find_min_max2(a, 0, len(a) - 1))
print(find_max_min3(a))


