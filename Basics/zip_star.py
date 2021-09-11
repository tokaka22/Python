

### zip 一一对应，返回的数据由()包括，所以是tuple
# https://blog.csdn.net/PaulZhn/article/details/104391756
a = ['a', 'b', 'c', 'd']
b = ['1', '2', '3', '4']
print(zip(a, b))
print(list(zip(a, b)))


### * 和 ** 
# https://blog.csdn.net/zhihaoma/article/details/50572854
'''
作为运算符
    **两个乘号就是乘方，比如2**4,结果就是2的4次方，结果是16
    一个乘号*，如果操作数是两个数字，就是这两个数字相乘，如2*4,结果为8
    *如果是字符串、列表、元组与一个整数N相乘，返回一个其所有元素重复N次的同类型对象，比如"str"*3将返回字符串"strstrstr"
'''

## 函数定义中
# 参数前的*表示的是将调用时的多个参数放入元组tuple中
def func1(*args):
    print(args)
func1(1,2,3,'a')

# **则表示将调用函数时的关键字参数放入一个字典中
def func2(**args):
    print(args)
func2(a=1,b=2)

## 函数调用中
'''
*args表示将可迭代对象扩展为函数的参数列表
args=(1,2,3)
func=(*args)
等价于函数调用func(1,2,3)

函数调用的**表示将字典扩展为关键字参数
args={'a':1,'b':2}
func(**args)
等价于函数调用 func(a=1,b=2)
'''