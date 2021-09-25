'''
通配符
    星号"*"匹配0个或多个字符
    问号"?"匹配任何单个字符
    "[]"匹配指定范围内的一个特定字符，如：[0-9]匹配范围内数字，[a-z]和[A-Z]匹配范围内字母
排序
    名称
    sorted(glob.glob('*.txt'))
    修改时间
    import os
    sorted(glob.glob('*.png'), key=os.path.getmtime)
    大小
    import os
    sorted(glob.glob('*.png'), key=os.path.getsize)
'''

import glob
import os

for f in sorted(glob.glob('E:\\tokaka\\recent_learn\\crowd_counting\\dataset\\UCF-QNRF_ECCV18\\Train\\*.jpg')
):
    temp = f.split('\\')[-1]
    temp1 = os.path.basename(f)
    print(temp)
    print(temp1)
    print(f)
