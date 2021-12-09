import re

def solution(time, plans):
    answer = ''
    arriveTime = ''
    departTime = ''

    # 여행지
    for i in plans:
        arriveTime = ''
        departTime = ''
        # 출발시간
        tmpTime = re.findall('\d', i[1]) # 리스트에서 정수 빼오기     
        tmpHolly = time # 남은 휴가시간
        # 빼온 정수 시간으로 만들기
        for j in tmpTime: 
            arriveTime += j 
        tmpTime = float(arriveTime)
        arriveNoon = re.findall('[a-zA-Z]', i[1])
        if arriveNoon[0] == 'P':
            tmpTime += 12
        if tmpTime < 18:
            tmpHolly -= (18 - tmpTime)
        # 도착시간
        tmp2Time = re.findall('\d', i[2])
        for j in tmp2Time:
            departTime += j   
        tmp2Time = float(departTime)
        arriveNoon = re.findall('[a-zA-Z]', i[2])
        if arriveNoon[0] == 'P':
            tmp2Time += 12
        if tmp2Time > 9.5:
            tmpHolly -= (tmp2Time - 9.5)
        if time - tmpHolly >= 0:
            answer = i[0]
    return answer


    
time = 3.5
plans = [["엘에이", "6PM", "11AM"], ["홍콩", "11PM", "9AM"]]
print(solution(time, plans))