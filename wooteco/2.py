from os import pipe


def solution(log):
    answer = ''
    sum_hour = 0
    sum_min = 0
    result = ""
    for i in range(0,len(log),2):
        Stime = log[i].split(':')
        Ftime = log[i+1].split(':')
        tmp2_hour = 0
        tmp2_min = 0
        # Hour 
        tmp_hour = int(Ftime[0]) - int(Stime[0])
        if tmp_hour > 0:
            tmp2_hour += tmp_hour
        elif tmp_hour < 0:
            tmp2_hour += tmp_hour + 24
        # Minuate
        tmp_min = int(Ftime[1]) - int(Stime[1])
        if tmp_min < 0:
            tmp2_hour -= 1
            tmp2_min += tmp_min + 60
        elif tmp_min >= 60:
            tmp2_hour += 1
            tmp2_min += tmp_min - 60
        else:
            tmp2_min = tmp_min
        # 최소시간 최대시간 조정
        if not(tmp2_hour < 1 and tmp2_min < 5) and not(tmp2_hour == 1 and tmp2_min > 45) and not(tmp2_hour >= 2):
            sum_hour += tmp2_hour
            sum_min += tmp2_min
        elif tmp2_hour == 1 and tmp2_min > 45:
            sum_hour += 1
            sum_min += 45
        elif tmp2_hour >= 2:
            sum_hour += 1
            sum_min += 45
    # Result
    if (sum_min > 59):
        sum_hour += int(int(sum_min) / 60)
        sum_min = int(sum_min) % 60

    answer = str('%02d'%sum_hour) + ":" + str(sum_min)

    return answer

log = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]
print(solution(log))