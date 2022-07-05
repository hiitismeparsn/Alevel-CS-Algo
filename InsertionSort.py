def InsertionSort(data):
    for i in range(1, len(data)):
        j = i                       # J is the a variable used to manipulate the array for swapping
        while data[j - 1] > data[j] and j != 0:
            data[j], data[j -1] = data[j-1], data[j]


data = [1,2,3,4,7,5,123,345,1231]


print(InsertionSort(data))

