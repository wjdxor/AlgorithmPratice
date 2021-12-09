def solution(new_id):
    answer = ''
    # 1단계
    tmp_2nd = new_id.lower()
    # 2단계
    count_3rd = 0
    for i in tmp_2nd:
        # 3단계
        if i == '.':
            count_3rd += 1
        else:
            if count_3rd >= 2:
                answer += '.'
                count_3rd = 0
            elif count_3rd == 1:
                answer += '.'
                count_3rd = 0
        # 2단계
        if i.islower() or i.isdigit() or i == '-' or i == '_':
            answer += i        
    # 6단계
    if answer[0] == '.':
        answer = answer[1:]    
    if len(answer) >= 16:
        answer = answer[:15]
    # 4단계
    if answer[-1:] == '.':
        answer = answer[:-1]
    # 5단계
    if answer == "":
        answer += "a"
    # 7단계
    while len(answer) <= 2:
        answer += answer[-1:]
    

    return answer

print(solution('z-+.^.'))
# print(solution('z-+.^.'))