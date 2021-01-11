# -*- coding: utf-8 -*-
'''指纹处理'''
import codecs
import random
import functools


_RINT = functools.partial(random.SystemRandom().randint, 0)

_P = 2 ** 23 - 1
_z = 2 ** 128 -1
_PRIME = 2 ** 128 - 1

''' x1 = g α p1 xn = g α pn'''

#生成的x的值
xs = []
# β的指数的值
b_index = _RINT(_z)
for x in range(0,245):
    # 计算n个x的值
    data_x = _RINT(_PRIME)
    xs.append(data_x)

#a = "原始n个x的值："
#print(unicode(a,"utf-8"))
print xs


with open("G:/xinan/TcpFile/runclient/user.txt", "a") as f:
    #f.write('原始n个x的值： \n'.decode('utf-8').encode('GBK'))
    f.write(" ")
    for x in range(0, 245):
        f.write(str(xs[x]))
        f.write("\n")
txt_tables = []
f = codecs.open("G:/xinan/aaa/user.txt", "r",encoding='GBK')
for line in f.readlines()[1:]:
    txt_data = eval(line) # 可将字符串变为元组
    txt_tables.append(txt_data) # 列表增加
    line = f.readline() # 读取下一行
print(txt_tables)

