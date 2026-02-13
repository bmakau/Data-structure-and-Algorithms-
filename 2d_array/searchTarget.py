from typing import List

def searchTarget(self, matrix: List[List[int]], target: int) -> bool:
    #find the rows and columns
    rows = len(matrix)
    columns = len(matrix[0])

    #initialize the first element and last element index
    left = 0
    right = rows * columns - 1 # total of elements in the 2D array(matrix)

    #Required time complexity for this problem is O(log(n * m))
    #binary search would be a good choice.

    while (left <= right):
        #as long as the left is smaller than right we will continue to loop 
        #need middle value
        middle = (left + right) // 2 #getting mid value
        #returns a tuple with dividend and remainder
        middle_row_index, middle_column_index = divmod(middle, columns)
        #Target equal the middle value return true 
        if matrix[middle_row_index][middle_column_index] == target:
            return True
        #Target < middle value our right equals middle minus one
        elif matrix[middle_row_index][middle_column_index] > target:
            right = middle - 1
        else:
            #Target > middle value our left equals middle plus one
            left = middle + 1

    return False


    