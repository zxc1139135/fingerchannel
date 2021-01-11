# -*- coding: utf-8 -*-
'''指纹模板更新'''

import random
import functools
from tuoyuan import curve25519

_RINT = functools.partial(random.SystemRandom().randint, 0)

_P = 2 ** 23 - 1
_z = 2 ** 128 -1
_PRIME = 2 ** 128 - 1

''' x1 = g α p1 xn = g α pn'''

#生成的x的值
xs = []
# β的指数的值
b_index = _RINT(_z)
for x in range(0,150):
    # p * β的指数的值
    p_index = _RINT(_P)
    #z_index = b_index
    index = p_index * b_index
    # 计算n个x的值
    data_x = _RINT(_PRIME)
    xs.append(data_x)

    # 计算n个z的值
    #data_z = obj.quick_algorithm(g, index, N)
    # 计算n个y的值
    #data_y = data_z ^ kk[x]
    # print(x)

#a = "原始n个x的值："
#print(unicode(a,"utf-8"))
print xs

x_news = []
ran_a = _RINT(_z)
for x in range(0,150):
    #x_new = obj.quick_algorithm(xs[x],ran_a,N)
    x_new = curve25519(xs[x],ran_a)
    x_news.append(x_new)
print x_news



with open("updata_fingerprint_server.txt", "w") as f:
    f.write("更新之后n个x的值： \n")
    for x in range(0, 150):
        f.write(str(x_news[x]))
        f.write("\n")
