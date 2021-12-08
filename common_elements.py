# Common elements

# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays. Can you take care of the duplicates without using any additional Data Structure?

array1 = [ 1, 5, 10, 20, 40, 80 ]
array2 = [ 6, 7, 20, 80, 100 ]
array3 = [ 3, 4, 15, 20, 30, 70, 80, 120 ]

# find smallest array
temp = min ( len(array1) , len(array2) )
smallest_len = min ( temp , len(array3) )

if smallest_len != temp : array = array3
elif smallest_len != len(array1) : array = array2
else : array = array1

# check for common elements
common_elements = []
for index in range ( 0 , len ( array ) ) :
    temp = array [ index ]
    if ( temp in array1 and temp in array2 and temp in array3 ) :
        common_elements.append ( temp )

# list all common elements
print ( common_elements )