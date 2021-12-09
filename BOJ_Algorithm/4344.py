tc = int(input())
for i in range(tc):
    arr = list(map(int,input().split())) #띄워쓰기 구분하여 리스트에 정수넣기
    N = arr[0]
    del arr[0]
    sum = 0
    count = 0
    for j in arr:
        sum += j
    mean = sum / N
    for j in arr:
        if j > mean:
            count += 1
    print("{:0.3f}%".format(count / N * 100)) # format함수 사용하여 프린트하기 #소수점 맞춰주기