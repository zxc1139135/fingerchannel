# -*- coding: utf-8 -*-
'''服务器随机生成密钥进行安全通道验证'''

from Shamir_Secret_Sharing import make_random_shares

threshold = 75
shares = 150
secret, shares =make_random_shares(threshold, shares)
#"门限秘钥128位秘钥key的值:"
print secret
kk = []
if shares:
    for share in shares:
        kk.append(share[1])

with open("G:/xinan/new_code/test/channel_server_key.txt", "w") as f:
    f.write('channel_secret_key: \n'.decode('utf-8').encode('GBK'))
    f.write(str(secret))
#"原始分享的n份k："
print kk
with open("G:/xinan/aaa/testchannel.txt", "w") as f:
    f.write('shares为： \n'.decode('utf-8').encode('GBK'))
    for x in range(0, 150):
        f.write(str(kk[x]))
        f.write("\n")