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
threshold = 75
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

with open('G:/xinan/TcpFile/runclient/clientreceive.txt', 'r') as f:
    content = f.read()
content = content.replace('*', '')

with open('G:/xinan/new_code/test/fingerprint_processing_client.txt', 'w') as f:
    f.write(content)
xs = []
f = codecs.open("G:/xinan/new_code/test/fingerprint_processing_client.txt", "r",encoding='GBK')
for line in f.readlines()[0:245]:
    txt_data = eval(line) # 可将字符串变为元组
    xs.append(txt_data) # 列表增加
    line = f.readline() # 读取下一行

zs = []
f = codecs.open("G:/xinan/new_code/test/zs.txt", "r",encoding='GBK')
for line in f.readlines()[1:]:
    txt_data = eval(line) # 可将字符串变为元组
    zs.append(txt_data) # 列表增加
    line = f.readline() # 读取下一行
intest = []
f = codecs.open("G:/xinan/new_code/test/GBF.txt", "r",encoding='GBK')
for line in f.readlines()[1:]:
    txt_data = eval(line) # 可将字符串变为元组
    intest.append(txt_data) # 列表增加
    line = f.readline() # 读取下一行
ans_y =[]
ans_ys = []
yy_ss = []
for j in range(0,245):
    x = xs[j]
    z = zs[j]
    ans_y = []
    h = [hashlib.sha1(), hashlib.sha384(), hashlib.sha512()]
    for i in range(len(h)):
        part_y = h[i]
        part_y.update(str(x).encode('utf-8'))
        j = int(part_y.hexdigest(), base=16) % 13000
        yy_ss.append(j)
        ans_y.append(j)
    y0 = ans_y[0]
    y1 = ans_y[1]
    y2 = ans_y[2]
    data_ans_y = intest[y0] ^ intest[y1] ^ intest[y2]
    ans_ys.append(data_ans_y)
print ans_ys

ans_ks = []
for i in range(0,245):
    ans_k = ans_ys[i] ^ zs[i]
    ans_ks.append(ans_k)

ans_points = []
ans_points = [(i, ans_ks[i-1])
              for i in range(1, 246)]
ans_sec = recover_secret(ans_points ,threshold)
print ans_sec

f = codecs.open("G:/xinan/new_code/test/ids.txt", "r",encoding='GBK')
for line in f.readlines()[1:]:
    ids = str(line)
f = codecs.open("G:/xinan/new_code/test/idc.txt", "r",encoding='GBK')
for line in f.readlines()[1:]:
    idc = str(line)
f = codecs.open("G:/xinan/new_code/test/rs.txt", "r",encoding='GBK')
for line in f.readlines()[1:]:
    rs = str(line)
f = codecs.open("G:/xinan/new_code/test/rc.txt", "r",encoding='GBK')
for line in f.readlines()[1:]:
    rc = str(line)
f = codecs.open("G:/xinan/new_code/test/c.txt", "r",encoding='GBK')
for line in f.readlines()[1:]:
    c = str(line)
#客户端进行恢复
st_c = str(ans_sec) + ids + idc + str(rs) + str(rc)
print(st_c)
#进行hash
out_c = hashlib.sha256(st_c.encode('utf-8')).hexdigest()
print out_c
#将哈希结果进行转换为数字
out_data_c = int(binascii.hexlify(out_c),16)
print out_data_c
#进行截取前16位数字
c_string_c = str(out_data_c)
c_code_c = c_string_c[0:16]
print c_code_c
#使用key解密c，验证是否为ids
c_ids_c = aesDecrypt(c_code_c,c)
print c_ids_c


if c_ids_c == ids:
    with open("G:/xinan/new_code/test/result_login.txt", "w") as f:
        f.write('success\n'.decode('utf-8').encode('GBK'))