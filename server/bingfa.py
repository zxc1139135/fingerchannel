# encoding: utf-8
import threading
import random
import functools
import hashlib
import time
import sys
from Shamir_Secret_Sharing import make_random_shares
from Shamir_Secret_Sharing import recover_secret
from Bloom import Bloom
from updata import updata

_RINT = functools.partial(random.SystemRandom().randint, 0)

_P = 2 ** 23 - 1
_z = 2 ** 128 -1
g = 2
N = 625994103176341579664226930767162576370916619299606554593919365405277831674354739266536500759439374157708124236397374320239325623808575574449295196238572963

# 并发测试框架
THREAD_NUM = 10

ONE_WORKER_NUM = 1
ti = []

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


def test():
    # 生成的x的值
    xs = []
    zs = []
    b_index = _RINT(_z)
    for x in range(0, 245):
        # p * β的指数的值
        p_index = _RINT(_P)
        z_index = b_index
        index = p_index * z_index
        # 计算n个x的值
        data_x = uqdata_quick_algorithm(g, p_index, N)
        xs.append(data_x)
        # 计算n个z的值
        data_z = uqdata_quick_algorithm(g, index, N)
        # 计算n个y的值
        data_y = data_z ^ kk[x]
        zs.append(data_z)
        # print(x)

    # 生成的n个y的值
    datas_y = []
    for x in range(0, 245):
        data_y = zs[x] ^ kk[x]
        # print(data_y)
        datas_y.append(data_y)
    x_news = []
    ran_a = _RINT(_z)
    for x in range(0, 245):
        x_new = updata.quick_algorithm(xs[x], ran_a, N)
        x_news.append(x_new)
    aa = Bloom(xs)
    intest = aa.getGarbledBloom()
    print("GBF存储空间为", sys.getsizeof(intest))


    pass  # 测试代码


def working():
    global ONE_WORKER_NUM
    for i in range(0, ONE_WORKER_NUM):
        test()


def t():
    global THREAD_NUM
    Threads = []
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working, name='T' + str(i))
        t.setDaemon(True)
        Threads.append(t)
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()


if __name__ == "__main__":

    threshold = 245
    shares = 245
    secret, shares = make_random_shares(threshold, shares)

    kk = []
    if shares:
        for share in shares:
            kk.append(share[1])

    start = time.time()
    t()
    end = time.time()

    print('门限秘钥128位秘钥key的值10个用户总时间: {} Seconds\n'.format(end - start))

    """
    threshold = 245
    shares = 245
    secret, shares = make_random_shares(threshold, shares)

    kk = []
    if shares:
        for share in shares:
            kk.append(share[1])

    # 生成的x的值
    xs = []
    zs = []
    b_index = _RINT(_z)
    for x in range(0, 245):
        # p * β的指数的值
        p_index = _RINT(_P)
        z_index = b_index
        index = p_index * z_index
        # 计算n个x的值
        data_x = uqdata_quick_algorithm(g, p_index, N)
        xs.append(data_x)
        # 计算n个z的值
        data_z = uqdata_quick_algorithm(g, index, N)
        # 计算n个y的值
        data_y = data_z ^ kk[x]
        zs.append(data_z)
        # print(x)

    # 生成的n个y的值
    datas_y = []
    for x in range(0, 245):
        data_y = zs[x] ^ kk[x]
        # print(data_y)
        datas_y.append(data_y)
    x_news = []
    ran_a = _RINT(_z)
    for x in range(0, 245):
        x_new = updata.quick_algorithm(xs[x], ran_a, N)
        x_news.append(x_new)
    """
    
