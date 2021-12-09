# # 15596 함수문제

# def d(n):
#     ans = 0
#     ans += n
#     for i in str(n):
#         ans += int(i)
#     return ans

# for j in range(1,10000):
#     flag = False
#     for k in range(1,j):
#         if d(k) == j:
#             flag = True
#             break
#     if flag == False:
#         print(j)


def d(n):
    ans = 0
    ans += n
    for i in str(n):
        ans += int(i)
    return ans


num = set(range(1,10001))
rmv = set()


for j in range(1,10000):
    rmv.add(d(j))
num = num - rmv
for k in sorted(num):
    print(k)