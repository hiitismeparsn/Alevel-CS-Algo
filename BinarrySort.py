def binarrySort(sequence, data):
    left = 0 
    right = len(sequence) - 1
   
    while left <= right:
        mid = (left + right) // 2
        print("Entered the loop")
        if sequence[mid] == data:       # Check if the data equals the mid of the sequence
            return mid
        elif sequence[mid] < data:      # Check if the data is less than the mid of the sequence and set left accordingly
            left = mid + 1
        elif sequence[mid] > data:      # Check if the data is greater than the mid of the sequence and set right accordingly
            right = mid - 1
        
    return -1       # Return -1 if the data is not present in the sequence

order = [1,2,3,4,5,6,7,8,9,10,11,98]

print(binarrySort(order, 98))