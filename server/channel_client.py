# -*- coding: utf-8 -*-
'''服务器随机生成密钥进行安全通道验证'''

import codecs
from Shamir_Secret_Sharing import recover_secret


threshold = 75
kk = []
f = codecs.open("G:/xinan/aaa/testchannel.txt", "r",encoding='GBK')
for line in f.readlines()[1:]:
    txt_data = eval(line) # 可将字符串变为元组
    kk.append(txt_data) # 列表增加
    line = f.readline() # 读取下一行

ans_points = [(i, kk[i-1])
              for i in range(1, 151)]
print ans_points
recover_client = recover_secret(ans_points[:100], threshold)
print recover_client
f = codecs.open("G:/xinan/new_code/test/channel_server_key.txt", "r",encoding='GBK')
for line in f.readlines()[1:]:
    channel_server_key = str(line)
print channel_server_key
with open("G:/xinan/new_code/test/result_channel.txt", "w") as f:
    f.write('channel_secret_key: \n'.decode('utf-8').encode('GBK'))
    f.write(str(recover_client))
if str(channel_server_key) == str(recover_client):
    with open("G:/xinan/new_code/test/result_channel.txt", "a") as f:
        f.write('\nthe channel is successfully established\n'.decode('utf-8').encode('GBK'))