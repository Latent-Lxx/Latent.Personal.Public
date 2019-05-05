#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

  @Time    : 19-4-28 下午2:25
  @Author  : Latent
  @Site    : 
  @File    : publicMians.py
  @Software: PyCharm
  @PS      : 

'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

  @Time    : 18-10-23 上午9:42
  @Author  : Latent
  @Site    :
  @File    : PUBLIC_MAIN.py
  @Software: PyCharm
  @PS      : PUBLUC MAIN...


 # 前景色
    'black': 30,    #黑色
    'red': 31,      #红色
    'green': 32,    #绿色
    'yellow': 33,   #黄色
    'blue': 34,     #蓝色
    'purple': 35,   #紫红色
    'cyan': 36,     #青蓝色
    'white': 37,    #白色
    'default':0,    #默认

# 背景
    'black': 40,   #黑色
    'red': 41,     #红色
    'green': 42,   #绿色
    'yellow': 43,  #黄色
    'blue': 44,    #蓝色
    'purple': 45,  #紫红色
    'cyan': 46,    #青蓝色
    'white': 47,   #白色


# 显示模式
    'normal': 0,    #终端默认设置
    'bold': 1,      #高亮显示
    'underline': 4, #使用下划线
    'blink': 5,     #闪烁
    'invert': 7,    #反白显示
    'hide': 8,      #不可见



'''
import time


# Showed fo custom corlor...(/033[1;31;40m)
def getCorlor(str1,str2,mode,corlor,back):

    str1 = str1;
    str2 = str2;
    mode = mode;
    corlor = corlor;
    back = back;

    return print('\033[%s;%s;%sm'%(mode,corlor,back),str1,str2,'\033[0m')


def getPrint(str1,str2,corlor):
    str1 = str1 ;
    str2 = str2 ;
    corlor = corlor;

    return  print('\033[%sm'%(corlor),str1,str2,'\033[0m')


