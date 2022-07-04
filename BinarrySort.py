def binarrySort(sequence, data):
    left = 0 
    right = len(sequence) - 1
   
    while left <= right:
        mid = (left + right) // 2
        print("Entered the loop")
        if sequence[mid] == data:
            return mid
        elif sequence[mid] < data:
            left = mid + 1
        elif sequence[mid] > data:
            right = mid - 1
        
    return -1

order = [1,2,3,4,5,6,7,8,9,10,11,98]
print(binarrySort(order, 98))