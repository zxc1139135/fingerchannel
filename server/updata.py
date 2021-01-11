#coding=utf-8
import random
import functools

import binascii
import hashlib

_PRIME = 2 ** 128 - 1
_xprime = 2 **10 -1
_Nprime = 2**30 -1
_RINT = functools.partial(random.SystemRandom().randint, 0)

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

'''随机生成128位数据，准备进行更新'''
print(_RINT(_PRIME))

x = _RINT(_xprime)
N = _RINT(_Nprime)
ran_a = _RINT(_PRIME)
obj =  updata()

print(obj.quick_algorithm(x,ran_a,N))
print(obj.quick_algorithm(2,255,1))
print(2**255 -19)