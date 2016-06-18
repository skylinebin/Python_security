# -*- coding: utf-8 -*-
'''
Decrypt the message  ASE dll in Python
@author liubin
@time 2016年6月13日 19：42
'''

from Crypto.Cipher import AES
from Crypto import Random
import binascii

def ASE_decrypt(mess,key):
    iv = Random.new().read(AES.block_size)
    # 确定初始化向量 从Random中读取16字节
    cipher = AES.new(key,AES.MODE_CBC,iv)
    # 生成解密时需要的实际密码,以CBC模式生成
    messtwo = mess+iv
    realmes = cipher.decrypt(mess)
    return realmes

be_encrypted =open('fc','rb')
mess = be_encrypted.read()
print u'加密后信息流：',mess
be_encrypted.close()

whatkey =open('savekey','rb')
key = whatkey.read()
print key
whatkey.close()
# key = raw_input('Please input your keys(16 bytes):')
res = ASE_decrypt(mess,key)
print u'解密后得到：',res

raw_input('Enter for Exit...')


