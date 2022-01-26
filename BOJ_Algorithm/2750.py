n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

arr = quick_sort(arr)

for i in range(n):
    print(arr[i])