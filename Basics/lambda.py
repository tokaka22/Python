
import time

# # 测试的Def函数
# def square1(n):
#     return n ** 2


# # 测试的Lambda函数
# square2 = lambda n: n ** 2

# print(time.time())

# # 使用Def函数
# i = 0
# while i < 1000000000:
#     square1(100)
#     i += 1

# print(time.time())

# # 使用lambda函数
# i = 0
# while i < 1000000000:
#     square2(100)
#     i += 1

# print(time.time())

expr = (lambda x,y:x+y)(4, 6) 
print(expr)