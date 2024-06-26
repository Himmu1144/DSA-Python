'''

State the problem clearly. Identify the input & output formats.

Come up with some example inputs & outputs. Try to cover all edge cases.

Come up with a correct solution for the problem. State it in plain English.

Implement the solution and test it using example inputs. Fix bugs, if any.

Analyze the algorithm's complexity and identify inefficiencies, if any.

Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

'''


""" Use The below code for notes   """


# Linear Search - For unsorted array - Time Complexity O(n)

def locate_element_unsorted(array, element):
    # Create a variable position with the value 0
    position = 0
    
    # Set up a loop for repetition
    while position < len(array):
        
        # Check if element at the current position matche the query
        if array[position] == element:
            
            # Answer found! Return and exit..
            return position
        
        # Increment the position
        position += 1
        
    return -1

        
# array = [2,6,1,1,4,9]
array = []
element = 1

print(f'Element {element} was found at index {locate_element_unsorted(array,element)}')

# Binary Search - For Sorted Arrays - Time Complexity - Log(n)

def locate_element_sorted(array, element):
    low, high = 0, len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_number = array[mid]
        
        print("low:", low, ", high:", high, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid_number == element:
            return mid
        elif mid_number < element:
            low = mid + 1  
        elif mid_number > element:
            high = mid - 1
    
    return -1


array = [1,2,4,6,7,8,9,10]
# array = []
element = 9

print(f'Element {element} was found at index {locate_element_sorted(array,element)}')

""" Use the code for nodes till here  """