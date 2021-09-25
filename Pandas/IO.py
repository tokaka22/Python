'''
python pandas读文件(不把第一行作列属性)
'''
import pandas as pd
#read_table可以指定分隔符
data1=pd.read_csv=("test.csv")#自动把第一行作列属性，第一行不能用
data2pd.read_csv("test.cvs",header=None)#不把第一行作列属性

data1=data1.conlumns(["A","B"])#修改列属性
data1=data1.reindex(["1","2"])#修改行属性
