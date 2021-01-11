# -*- coding: utf-8 -*-
'''注册流程'''

import random
import functools
import hashlib
import time
import sys
import binascii
from Shamir_Secret_Sharing import make_random_shares
from Shamir_Secret_Sharing import recover_secret
from Bloom import Bloom
from updata import updata
from aes_gcm import aesEncrypt
from aes_gcm import aesDecrypt
from tuoyuan import curve25519


_RINT = functools.partial(random.SystemRandom().randint, 0)

_P = 2 ** 23 - 1
_z = 2 ** 128 -1
g = 2
N = 625994103176341579664226930767162576370916619299606554593919365405277831674354739266536500759439374157708124236397374320239325623808575574449295196238572963

_PRIME = 2 ** 128 - 1
_skime = 2 ** 64 - 1


'''AES加密解密程序'''
BLOCK_SIZE = 32  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

"""快速模幂运算  a^b%c"""

class updata:
    '''快速模幂程序 a的b次方模N '''
    def quick_algorithm(slef,a,b,c):
        a=a%c
        ans=1
        #这里我们不需要考虑b<0，因为分数没有取模运算
        while b!=0:
            if b&1:
                 ans=(ans*a)%c
            b>>=1
            a=(a*a)%c
        return ans
obj =  updata()

#开始工作

sk_key = '1368964689231546'
data = 'herishsda'

upd = _RINT(_PRIME)
a_upd = upd
upd_str = upd

a = "加密之前的upd:"
print(unicode(a,"utf-8"))
print str(upd_str)


ecdata = aesEncrypt(sk_key, str(upd_str))
a = "加密之后cupd为："
print(unicode(a,"utf-8"))
print ecdata

dcdata = aesDecrypt(sk_key, ecdata)
a = "解密之后的upd为："
print(unicode(a,"utf-8"))
print dcdata

w_index = upd
#w = obj.quick_algorithm(g, w_index, N)
w = curve25519(g,w_index)
a = "w的值为:"
print(unicode(a,"utf-8"))
print w

b_beita = _RINT(_PRIME)
a = "随机选取的b_beita为:"
print(unicode(a,"utf-8"))
print b_beita

v_index = b_beita * upd
#v = obj.quick_algorithm(g, v_index, N)
v = curve25519(g,v_index)
a = "v的值为:"
print(unicode(a,"utf-8"))
print v


for x in range(0,1):
    a = _RINT(_PRIME)
    temp = a * a_upd
    eu_n = N - 1
    a_upd = obj.quick_algorithm(temp, 1, N - 1)
    a = "更新之后的upd:"
    print(unicode(a, "utf-8"))
    print a_upd

    ecdata = aesEncrypt(sk_key, str(a_upd))
    a = "加密之后cupd为："
    print(unicode(a, "utf-8"))
    print ecdata

    dcdata = aesDecrypt(sk_key, ecdata)
    a = "解密之后的upd为："
    print(unicode(a, "utf-8"))
    print dcdata

    gb_sk = obj.quick_algorithm(g, int(sk_key), N)
    a = "公布gb_sk:"
    print(unicode(a, "utf-8"))
    print gb_sk
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
    x_new = curve25519(xs[x],int(dcdata))
    x_news.append(x_new)
print x_news

with open("register_fingerprint_server.txt", "w") as f:
    f.write("注册更新之后n个x的值： \n")
    for x in range(0, 150):
        f.write(str(x_news[x]))
        f.write("\n")
