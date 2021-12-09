def solution(ings, menu, sell):
    answer = 0
    # 재료 정보 {재료이름:가격}
    ingsDB = {}
    for i in ings:
        tmp_ings = i.split(" ")
        ingsDB[tmp_ings[0]] = tmp_ings[1]

    # 메뉴 정보 {메뉴이름:수익}
    menuDB = {}
    for i in menu:
        tmp_memu = i.split(" ")
        # 메뉴 재료비 계산
        memuCost = 0
        for j in tmp_memu[1]:
            memuCost += int(ingsDB[j])
        menuDB[tmp_memu[0]] = int(tmp_memu[2]) - memuCost

    # 판매 실적 {메뉴이름:판매수량}
    sellDB = {}
    for i in sell:
        tmp_sell = i.split(" ")
        sellDB[tmp_sell[0]] = menuDB[tmp_sell[0]] * int(tmp_sell[1])
    
    # 총수익
    for i in sellDB.values():
        answer += i
    return answer


ings = ["r 10", "a 23", "t 124", "k 9"]
menu = ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]
sell = ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]

solution(ings, menu, sell)