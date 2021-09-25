'''
首先得有__init__.py
其次用sys.path包含目标module的目录
https://stackoverflow.com/questions/30669474/beyond-top-level-package-error-in-relative-import
'''


import sys
sys.path.append("..") # Adds higher directory to python modules path.
