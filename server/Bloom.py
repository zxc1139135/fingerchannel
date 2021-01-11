#coding=utf-8
'''
生成布隆过滤器程序
'''

import hashlib
import random




class Bloom:
    """  Hash functions used for bloom filter """
    """ 选择三种哈希函数，实现布隆过滤器"""
    h = [hashlib.sha1(), hashlib.sha384(), hashlib.sha512()]
    ''' Security parameter lambda'''
    ''' 设置安全参数 实验中的m的值'''
    lam = 128
    def __init__(self, inputArray):
        self.inputArray = inputArray
        '''Length of bloom filter and garbled bloom filter'''
        ''' 设置过滤器的参数 '''
        self.m = 13000
        ''' 初始化过滤器都设置为空 '''
        self.garbledBloomArray = [None for i in range(self.m)]
        self.bloomArray = [0 for i in range(self.m)]
    """ 得到安全参数 """
    def getLambda(self):
        return self.lam
    """ 得到输入的参数 """
    def getInput(self):
        return self.inputArray
    """ 获取混淆布隆过滤器 """
    def getGarbledBloom(self):
        return self.garbledBloomArray
    
    def getBloom(self):
        return self.bloomArray
        
    """ 生成布隆过滤器 """
    def generateBloom(self):
        for element in self.inputArray:
            h = [hashlib.sha1(), hashlib.sha384(), hashlib.sha512()]
            for i in range(len(h)):
                val = h[i] #将一组字符型数据的数字部分转换成相应的数值型数据
                val.update(str(element).encode('utf-8')) 
                j = int(val.hexdigest(), base=16) % self.m  #作为十六进制数据字符串值
                self.bloomArray[j]=1

    ''' 生成GBF'''

    def generateGarbledBloom(self, y, n):
        js = []
        for x in range(0,n):
            element_x = self.inputArray[x]
            element = y[x]
            emptySlot = -1
            finalShare = element
            h = [hashlib.sha1(), hashlib.sha384(), hashlib.sha512()]
            for i in range(len(h)):
                x_index = h[i]
                x_index.update(str(element_x).encode("utf8"))
                #print(x_index.update(str(element).encode("utf8")))
                j = int(x_index.hexdigest(), base=16) % self.m
                #print(j)
                js.append(j)
                if(self.garbledBloomArray[j]==None):
                    if(emptySlot==-1):
                        emptySlot = j   # Reserve emptyslot for final share
                    else:
                        newShare = random.getrandbits(self.lam)    # Generate new lambda bit share
                        self.garbledBloomArray[j] = newShare
                        finalShare = finalShare ^ self.garbledBloomArray[j]
                else:
                    finalShare = finalShare ^ self.garbledBloomArray[j]
            self.garbledBloomArray[emptySlot] = finalShare
        for i in range(self.m):
            if(self.garbledBloomArray[i]==None):
                self.garbledBloomArray[i] = random.getrandbits(self.lam)
        return js


    def queryBloom(self, x):
        h = [hashlib.sha1(), hashlib.sha384(), hashlib.sha512()]
        for i in range(len(h)):
            val = h[i]
            val.update(str(x))
            j = int(val.hexdigest(), base=16) % self.m
            if(self.bloomArray[j]==0):
                return False
        return True

    '''在布隆过滤器中查询'''
    def queryGarbled(self, x, GBF):
        recovered = 0
        h = [hashlib.sha1(), hashlib.sha384(), hashlib.sha512()]
        for i in range(len(h)):
            val = h[i]
            val.update(str(x).encode('utf-8'))
            j = int(val.hexdigest(), base=16) % self.m
            recovered = recovered ^ GBF[j]
        if(recovered == x):
            return True
        else:
            return False
    '''彼此产生的交集'''
    def generateIntersection(self, GBF):
        GBFint = [None for i in range(self.m)]
        for i in range(len(self.bloomArray)):
            if(self.bloomArray[i]==0):
                GBFint[i]=random.getrandbits(self.lam)
            else:
                GBFint[i]=GBF[i]
        return GBFint

"""
st = [10,11,12,13,14]
sy = [6,4,7,5,8]
sr = [1,2,3]
a = Bloom(st)
b = Bloom(sr)
a.generateGarbledBloom(sy,5)
b.generateBloom()
inter = b.generateIntersection(a.getGarbledBloom())
print(inter)
intest = a.getGarbledBloom()
#print(intest)
for x in [1,2,3,4,5,6]:
    if(a.queryGarbled(x, intest)):
        print(x)
"""
