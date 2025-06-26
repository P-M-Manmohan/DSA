def MergeSort(A):
    if len(A) > 1:

        m = (len(A))//2
        L = A[:m]
        R = A[m:]
        MergeSort(L)
        MergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i+=1
            else:
                A[k] = R[j]
                j+=1
            k+=1
        
        while i < len(L):
            A[k] = L[i]
            i+=1
            k+=1
            
        while j < len(R):
            A[k] = R[j]
            j+=1
            k+=1


array = [5,4,3,2,1]
MergeSort(array)
for i in range(len(array)):
    print(array[i],end=" ")
