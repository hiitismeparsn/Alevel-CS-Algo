
def LinearSearch(sequence,data):
    for i in range(len(sequence)):
        if sequence[i] == data:
            return i 
    
    return -1

orderd = [1,2,3,4,5,6,7,8]
print(LinearSearch(orderd, 9))