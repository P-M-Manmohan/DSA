def counting_sort(arr: list[int]) -> list[int]:
    size = len(arr)
    m = max(arr)
    count = [0] * (m + 1 )
    for i in arr:
        count[i]+=1

    for i in range(1,max(arr)+1):
        count[i] += count[i-1]

    i = size-1
    output = [0] * size
    while i >= 0:
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -=1
        i-=1

    for i in range(size):
        arr[i] = output[i]

    return arr


print(counting_sort([4,3,2,5,2,1,2]))
        
