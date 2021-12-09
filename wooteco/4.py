def solution(s):
    answer = []

    tmp_str = ''
    if s[:1] == s[-1:]:
        # 처음과 끝에 모으기
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                tmp_str = s[i+1:] + s[:i+1]
                break
    else:
        tmp_str = s[:]

    # 처음부터 같은 문자 세기
    count = 1
    for i in range(len(tmp_str)-1):
        if tmp_str[i] == tmp_str[i+1]:
            count += 1
        elif tmp_str[i] != tmp_str[i+1]:
            answer.append(count)
            count = 1
        
    answer.append(count)
    answer.sort()
    return answer

s = "wowwow"
print(solution(s))