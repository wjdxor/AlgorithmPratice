# def solution(lottos, win_nums):
#     answer = []
#     count = 0
#     count2 = 0

#     for i in range(6):
#         if lottos[i] == 0:
#             count2 += 1
#             continue
#         else:
#             for j in range(6):
#                 if lottos[i] == win_nums[j]:
#                     count += 1
#     #최저 순위
#     rank = 7 - count
#     #최고 가능 순위
#     rank_able = rank - count2

#     if rank == 7:
#         rank == 6
#     if rank_able == 7:
#         rank_able == 6
#     answer = [rank_able,rank]
#     return answer



# print(solution([1, 2, 3, 4, 0, 0], [10, 11, 12, 13, 14, 15]))

s = 'rkskekfkfk'
a = list(s)
for i in range(5):
    print("1")