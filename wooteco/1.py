def solution(arr):
    answer = []
    count = [0,0,0]
    for i in arr:
        count[i-1] += 1
    maxCount = max(count)
    for j in range(0,3):
        if count[j] < maxCount:
            answer.append(maxCount - count[j])
        else:
            answer.append(0)
    return answer

arr = [1, 3, 3, 3, 3, 3]
print(solution(arr))