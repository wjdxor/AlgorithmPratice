record = ["Enter uid1234 Muzi","Change uid1234 Ryan","Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    database = {}

    # 데이터베이스 만들기
    for i in record:
        output = ''
        tmpArr = i.split(" ")

        if tmpArr[0] == 'Enter' or tmpArr[0] == 'Change':
            database[tmpArr[1]] = tmpArr[2]

    # 채팅창 기록 만들기
    for i in record:
        output = ''
        tmpArr = i.split(" ")

        if tmpArr[0] == "Enter":
            output = database[tmpArr[1]] + '님이 들어왔습니다.'
            answer.append(output)
        elif tmpArr[0] == "Leave":
            output = database[tmpArr[1]] + '님이 나갔습니다.'
            answer.append(output)
        
    return answer
        
print(solution(record))