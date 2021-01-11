# -*- coding: utf-8 -*-
'''测试数据程序'''

import random
import functools
import hashlib
import string
import binascii
from Shamir_Secret_Sharing import make_random_shares
from Shamir_Secret_Sharing import recover_secret
from Bloom import Bloom
from aes_gcm import aesEncrypt
from aes_gcm import aesDecrypt
from aes_gcm import uqdata_quick_algorithm
from tuoyuan import curve25519


_RINT = functools.partial(random.SystemRandom().randint, 0)

_P = 2 ** 23 - 1
_z = 2 ** 128 -1
g = 2
N = 625994103176341579664226930767162576370916619299606554593919365405277831674354739266536500759439374157708124236397374320239325623808575574449295196238572963
_PRIME = 2 ** 128 - 1
_skime = 2 ** 64 - 1
_rs = 2 ** 128 - 1
_rc = 2 ** 128 - 1
_k = 2 ** 128 -1
g = 2

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

'''AES加密解密程序'''
BLOCK_SIZE = 32  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


#准备工作需要的

data_safety = 128
#"安全参数："
#print (data_safety)


H_hash = 3
# "哈希函数的个数"
#print (H_hash)

n_number = 245
#"插入GBF中的个数："
#print (n_number)

m_number = 13000
#"GBF的格子的数量："
#print m_number

""" 门限密钥共享 """

threshold = 75
shares = 150
secret, shares =make_random_shares(threshold, shares)
#"门限秘钥128位秘钥key的值:"
print secret
kk = []
if shares:
    for share in shares:
        kk.append(share[1])

#"原始分享的n份k："
print kk


#开始工作  根据是否注册过决定是否进行有关更新操作
sk_key = '1368964689231546'
data = 'herishsda'

upd = _RINT(_PRIME)
a_upd = upd
upd_str = upd

#"加密之前的upd:"
print str(upd_str)


ecdata = aesEncrypt(sk_key, str(upd_str))
#"加密之后cupd为："
print ecdata

dcdata = aesDecrypt(sk_key, ecdata)
#"解密之后的upd为："
print dcdata

for x in range(0,1):
    a = _RINT(_PRIME)
    temp = a * a_upd
    eu_n = N - 1
    a_upd = uqdata_quick_algorithm(temp, 1, N - 1)
    #"更新之后的upd:"
    print a_upd

    ecdata = aesEncrypt(sk_key, str(a_upd))
    #"更新一次之后 加密之后cupd为："
    print ecdata

    sk_new = _RINT(_skime)
    #"更新之后的sk_new:"
    print sk_new

    gb_sk = uqdata_quick_algorithm(g, sk_new, N)
    #"公布gb_sk:"
    print gb_sk


# 2.2.1 第一步模拟检测找到 参数 以及 模板
#生成的x的值
xs = []
zs = []
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
    data_z = curve25519(g,index)
    # 计算n个y的值
    data_y = data_z ^ kk[x]
    zs.append(data_z)
    # print(x)

# 2.2.2 将cupd解密为upd
dcdata = aesDecrypt(sk_key, ecdata)
#"更新一次之后，解密之后的upd为："
print dcdata

# 2.2.3 随机选取的数字

b_beita = _RINT(_PRIME)
#"随机选取的b_beita为:"
print b_beita

w_index = int(dcdata)
#w = obj.quick_algorithm(g, w_index, N)
w = curve25519(g,w_index)
#"w的值为:"
print w


v_index = b_beita * upd
#v = obj.quick_algorithm(g, v_index, N)
v = curve25519(g,v_index)
#"v的值为:"
print v

#生成的n个y的值
ys = []
for x in range(0,150):
    data_y = zs[x] ^ kk[x]
    #print(data_y)
    ys.append(data_y)
#print(xs[244])

#"原始n个x的值："
print xs

#"原始n个z的值："
print zs

#"原始n个y的值："
print ys

# 2.2.5 GBF有关操作
y_home = []
aa = Bloom(xs)
y_home = aa.generateGarbledBloom(ys,150)
intest = aa.getGarbledBloom()

#"生成的GBF为:"
print intest

#"存储n个y在GBF中的位置:"
print y_home


ans_y =[]
ans_ys = []
yy_ss = []
for j in range(0,150):
    x = xs[j]
    z = zs[j]
    ans_y = []
    h = [hashlib.sha1(), hashlib.sha384(), hashlib.sha512()]
    for i in range(len(h)):
        part_y = h[i]
        part_y.update(str(x).encode('utf-8'))
        j = int(part_y.hexdigest(), base=16) % m_number
        yy_ss.append(j)
        ans_y.append(j)
    y0 = ans_y[0]
    y1 = ans_y[1]
    y2 = ans_y[2]
    data_ans_y = intest[y0] ^ intest[y1] ^ intest[y2]
    ans_ys.append(data_ans_y)

#"恢复n个y在GBF选取的位置："
print yy_ss

#"恢复的n个y的值为："
print ans_ys

ans_ks = []
for i in range(0,150):
    ans_k = ys[i] ^ zs[i]
    ans_ks.append(ans_k)

# "恢复的n份k值："
print ans_ks


ans_points = []
ans_points = [(i, ans_ks[i-1])
              for i in range(1, 151)]
ans_sec = recover_secret(ans_points ,threshold)

#"恢复的n个k的所有:"
print ans_points

idc = id_generator()
ids = id_generator()
k = _RINT(_k)
rs = _RINT(_rs)
rc = _RINT(_rc)
# 2.2.6 key的生成
print k
print idc
print ids
print rs
print rc
st = str(k) + ids + idc + str(rs) + str(rc)
print(st)
out = hashlib.sha256(st.encode('utf-8')).hexdigest()
print out

string = out
out_data = int(binascii.hexlify(string),16)
print out_data

c_string = str(out_data)
c_code = c_string[0:16]
print c_code

c_ids = str(ids)
print c_ids
c = aesEncrypt(c_code, ids)
print c





