import sys
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().strip()))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_side = arr[:mid]
    right_side = arr[mid:]
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)
    return merge(left_side, right_side)

def merge(left,right):
    merged_arr = []
    l = h = 0
    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[h])
            h += 1
    merged_arr += left[l:]
    merged_arr += right[h:]
    return merged_arr

arr = merge_sort(arr)

for i in arr:
    print(i)