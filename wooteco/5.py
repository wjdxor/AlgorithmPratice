def solution(rows, columns):
    answer = [[]]
    tmpArr = [[0 for c in range(columns)] for r in range(rows)]
    r = 1
    c = 1
    i = 1
    flag = 0

    while (i):    
        if tmpArr[r-1][c-1] == 0:
            flag += 1
        tmpArr[r-1][c-1] = i
        if flag == rows * columns:
            break
         # 빙글빙글
        if (rows == columns):
            if r == rows:
                if c == 0:
                    break
        # 다음위치 변경
        if i % 2 != 0:
            c += 1
        else:
            r += 1
        if r < 1:
            r = rows
        elif r > rows:
            r = 1
        if c < 1:
            c = columns
        elif c > columns:
            c = 1
        i += 1
       
            

    answer = tmpArr
    return answer


print(solution(4,4))