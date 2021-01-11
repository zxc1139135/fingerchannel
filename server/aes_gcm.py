#coding=utf-8

from Crypto.Cipher import AES
import base64
import functools
import random
import time
_PRIME = 2 ** 128 - 1
_skime = 2 ** 64 - 1
_RINT = functools.partial(random.SystemRandom().randint, 0)
g = 2
N = 625994103176341579664226930767162576370916619299606554593919365405277831674354739266536500759439374157708124236397374320239325623808575574449295196238572963

'''AES加密解密程序'''
BLOCK_SIZE = 32  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def aesEncrypt(key, data):
    '''
    AES的ECB模式加密方法
    :param key: 密钥
    :param data:被加密字符串（明文）
    :return:密文
    '''
    key = key.encode('utf8')
    # 字符串补位
    data = pad(data)
    cipher = AES.new(key, AES.MODE_ECB)
    # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    result = cipher.encrypt(data.encode())
    encodestrs = base64.b64encode(result)
    enctext = encodestrs.decode('utf8')
    #print(enctext)
    return enctext

def aesDecrypt(key, data):
    '''

    :param key: 密钥
    :param data: 加密后的数据（密文）
    :return:明文
    '''
    key = key.encode('utf8')
    data = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_ECB)

    # 去补位
    text_decrypted = unpad(cipher.decrypt(data))
    text_decrypted = text_decrypted.decode('utf8')
    #print(text_decrypted)
    return text_decrypted

def uqdata_quick_algorithm(a,b,c):
    a=a%c
    ans=1
    #这里我们不需要考虑b<0，因为分数没有取模运算
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1
        a=(a*a)%c
    return ans

if __name__ == '__main__':
    sk_key = '1368964689231546'
    data = 'herishsda'

    print("原始ID信息为：",(data))
    ecdata = aesEncrypt(sk_key, data)
    print("加密之后ID为：",ecdata)

    dcdata = aesDecrypt(sk_key, ecdata)
    print(dcdata)
    #input("end")

