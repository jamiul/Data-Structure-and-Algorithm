def SelectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if(arr[min_index] > arr[j]):
                min_index = j

        '''if(min_index != i): # Manual Swap
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp'''

        arr[i],arr[min_index] = arr[min_index],arr[i] # Shortcut Swap tecnique 
    return arr


arr = [64, 25, 12, 22, 11]
sort = SelectionSort(arr)
print(sort)