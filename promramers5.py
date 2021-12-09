
columns = 6
rows = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]


def solution(rows, columns, queries):
    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    for i in range(1,columns+1):
        for j in range(1,rows+1):
            array[i-1][j-1] = (i-1) * columns + j

    for i in queries:
        x1 = i[0]
        y1 = i[1]
        x2 = i[2]
        y2 = i[3]
        for j in range(x1, y2):
            tmp = array[x1-1][j]
            array[x1-1][j] = array[x1-1][j-1]
        # for j in range(x2,y1):

            
        return answer

solution(rows, columns, queries)