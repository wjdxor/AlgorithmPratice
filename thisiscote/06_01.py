arr = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(arr)):
    min_ = i
    for j in range(i+1, len(arr)):
        if arr[min_] > arr[j]:
            min_ = j
    arr[i], arr[min_] = arr[min_], arr[i]
