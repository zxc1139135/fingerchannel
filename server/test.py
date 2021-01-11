# -*- coding: utf-8 -*-
'''登录验证以及返回有关数据程序'''

import codecs
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
shares = 245
secret, shares =make_random_shares(threshold, shares)
#"门限秘钥128位秘钥key的值:"
print secret
with open("G:/xinan/new_code/test/k.txt", "w") as f:
    f.write('k的值： \n'.decode('utf-8').encode('GBK'))
    f.write(str(secret))

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

with open('G:/xinan/TcpFile/runsever/informationForLogin.txt', 'r') as f:
    content = f.read()
content = content.replace('*', '')

with open('G:/xinan/new_code/test/fingerprint_processing_client.txt', 'w') as f:
    f.write(content)
zs = []
# β的指数的值
b_index = _RINT(_z)
xs = []
f = codecs.open("G:/xinan/new_code/test/fingerprint_processing_client.txt", "r",encoding='GBK')
for line in f.readlines()[0:245]:
    txt_data = eval(line) # 可将字符串变为元组
    xs.append(txt_data) # 列表增加
    line = f.readline() # 读取下一行


for x in range(0,245):
    data_z = curve25519(xs[x],b_index)
    # 计算n个y的值
    data_y = data_z ^ kk[x]
    zs.append(data_z)
    # print(x)
with open("G:/xinan/new_code/test/zs.txt", "w") as f:
    f.write('zs为： \n'.decode('utf-8').encode('GBK'))
    for x in range(0, 245):
        f.write(str(zs[x]))
        f.write("\n")
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

with open("G:/xinan/new_code/test/w.txt", "w") as f:
    f.write('w的值： \n'.decode('utf-8').encode('GBK'))
    f.write(str(w))

v_index = b_beita * upd
#v = obj.quick_algorithm(g, v_index, N)
v = curve25519(g,v_index)
#"v的值为:"
print v
with open("G:/xinan/new_code/test/v.txt", "w") as f:
    f.write('v的值： \n'.decode('utf-8').encode('GBK'))
    f.write(str(v))

#生成的n个y的值
ys = []
for x in range(0,245):
    data_y = zs[x] ^ kk[x]
    #print(data_y)
    ys.append(data_y)

#"原始n个x的值："
#print xs

#"原始n个z的值："
#print zs

#"原始n个y的值："
print ys

# 2.2.5 GBF有关操作
y_home = []
aa = Bloom(xs)
y_home = aa.generateGarbledBloom(ys,245)
intest = aa.getGarbledBloom()

#"生成的GBF为:"
print intest
with open("G:/xinan/new_code/test/GBF.txt", "w") as f:
    f.write('GBF为： \n'.decode('utf-8').encode('GBK'))
    for x in range(0, 13000):
        f.write(str(intest[x]))
        f.write("\n")
#"存储n个y在GBF中的位置:"
#print y_home

idc = id_generator()
ids = id_generator()
rs = _RINT(_rs)
rc = _RINT(_rc)

# 2.2.6 key的生成
print idc
print ids
print rs
print rc

st_s = str(secret) + ids + idc + str(rs) + str(rc)
print(st_s)
#进行hash
out_s = hashlib.sha256(st_s.encode('utf-8')).hexdigest()
print out_s

#将哈希结果进行转换为数字
out_data_s = int(binascii.hexlify(out_s),16)
print out_data_s

#进行截取前16位数字
c_string_s = str(out_data_s)
c_code_s = c_string_s[0:16]
print c_code_s

#加密ids 生成c
c = aesEncrypt(c_code_s, ids)
print c

with open("G:/xinan/new_code/test/idc.txt", "w") as f:
    f.write('idc的值： \n'.decode('utf-8').encode('GBK'))
    f.write(str(idc))
with open("G:/xinan/new_code/test/ids.txt", "w") as f:
    f.write('ids的值： \n'.decode('utf-8').encode('GBK'))
    f.write(str(ids))
with open("G:/xinan/new_code/test/rs.txt", "w") as f:
    f.write('rs的值： \n'.decode('utf-8').encode('GBK'))
    f.write(str(rs))
with open("G:/xinan/new_code/test/rc.txt", "w") as f:
    f.write('rc的值： \n'.decode('utf-8').encode('GBK'))
    f.write(str(rc))
with open("G:/xinan/new_code/test/c.txt", "w") as f:
    f.write('c的值： \n'.decode('utf-8').encode('GBK'))
    f.write(str(c))







