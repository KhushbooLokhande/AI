def selection_sort(arr):
    n = len(arr)

    if n == 1:  
        print(f"Array is already sorted: {arr}")
        return arr
    
    if n <= 0:  
        print(f"Array is empty: {arr}")
        return arr

    passes = 0

    for i in range(n - 1):
        min_index = i
        swapped = False  

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i: 
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swapped = True

        passes += 1
        print(f"Pass {passes}: {arr}")

        if not swapped:
            break  

    print(f"Total passes: {passes}")
    print("Sorted Array:")
    return arr

# Test cases
print(selection_sort([5]))       
print(selection_sort([]))        
print(selection_sort([11, 12, 22, 25, 64])) 
print(selection_sort([64, 25, 12, 22, 11]))  
print(selection_sort([5,10,2,20,6]))