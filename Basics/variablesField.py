'''
https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
python的变量默认就是可以global调用的，但你要修改的话需要用global声明一下
'''


'''
同一个py file下
'''
# ### test without if __name__ == "__main__":
# # 其实if __name__ == "__main__": 具体运行 跟原始没啥区别
# globvar = 100

# def set_globvar_to_one():
#     global globvar    # Needed to modify global copy of globvar
#     globvar = 1

# def print_globvar():
#     print(globvar)     # No need for global declaration to read value of globvar

# set_globvar_to_one()
# print_globvar()       # Prints 1


# ### 不加global
# globvar = 100

# def set_globvar_to_one():
#     # global globvar    # Needed to modify global copy of globvar
#     globvar = 1

# def print_globvar():
#     print(globvar)     # No need for global declaration to read value of globvar

# set_globvar_to_one()
# print_globvar()       # Prints 1


# ### if __name__ == "__main__": 之外
# globvar = 100

# def set_globvar_to_one():
#     global globvar    # Needed to modify global copy of globvar
#     globvar = 1

# def print_globvar():
#     print(globvar)     # No need for global declaration to read value of globvar

# if __name__ == "__main__":
#     set_globvar_to_one()
#     print_globvar()       # Prints 1

# ### if __name__ == "__main__": 之内
# def set_globvar_to_one():
#     global globvar    # Needed to modify global copy of globvar
#     globvar = 1

# def print_globvar():
#     print(globvar)     # No need for global declaration to read value of globvar

# if __name__ == "__main__":
#     globvar = 100
#     set_globvar_to_one()
#     print_globvar()       # Prints 1

'''
class调用同一file下的另一个func
https://stackoverflow.com/questions/38097638/assign-external-function-to-class-variable-in-python
'''

# from math import pow
# def pow_(a, b):
#     return pow(a,b)

# class Foo3(object):
#     '''
#     class methods都会传入self，故可以使用staticmethod限定
#     '''
#     # func = pow_ # 不行
#     # func = pow # 可以
#     func = staticmethod(pow_) # 可以
#     def __init__(self):
#         print(self.func(2,3)) # 得用self调用class attribute

# f3 = Foo3()

