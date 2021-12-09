def hansoo(a):
    arr = []
    for i in str(a):
        arr.append(int(i))
    if len(arr) > 2:
        for i in range(0,len(arr)-2):
            if arr[i] - arr[i+1] != arr[i+1] - arr[i+2]:
                return False
    return True

N = int(input())
count = 0
for i in range(1,N+1):
    if hansoo(i):
        count += 1
print(count)