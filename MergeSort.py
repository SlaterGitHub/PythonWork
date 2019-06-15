# Python program for implementation of MergeSort
def mergeSort(arr, array, l):
    arr = [i[l] for i in array]
    if len(arr) >1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        LArray = array[:mid]
        R = arr[mid:] # into 2 halves
        RArray = array[mid:]

        mergeSort(L, LArray, l) # Sorting the first half
        mergeSort(R, RArray, l) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = LArray[i]
                i+=1
            else:
                array[k] = RArray[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            array[k] = LArray[i]
            i+=1
            k+=1

        while j < len(R):
            array[k] = RArray[j]
            j+=1
            k+=1

# driver code to test the above code
def sort(arr, indx):
    mergeSort(arr, arr, indx)
    print([i[3] for i in arr])
