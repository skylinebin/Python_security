# -*- coding: utf-8 -*-
'''
Use ASE dll in Python
A Test to Return a AES-File of a Common File
@author liubin
@time 2016年6月13日 16：30
'''

from Crypto.Cipher import AES
from Crypto import Random
import binascii

#This founction is to encrypt the file by ASE
def AES_File(files,key):
    y =len(key)%16
    if len(key)>16:
        key =key[0:15]
    else:
        if y!=0:
            key = key + '0'*(16-y)
        else:
            print key
    print key
    savekey = open('savekey','w+')
    savekey.writelines(key)
    savekey.close()
    # key = b'1234567890!@#$%^'
    #password are 16bytes 指定16字节的初始密钥
    iv = Random.new().read(AES.block_size)
    # 确定初始化向量 从Random中读取16字节
    cipher = AES.new(key,AES.MODE_CBC,iv)
    # 生成加密时需要的实际密码,以CBC模式生成
    # if files is a multiple of 16
    print 'If the length of file is a multiple of 16 ?'
    #判断数据长度是否为16的整数倍，不是的用0填充至整数倍
    x =len(files)%16
    print 'The length of files is :',len(files)
    print 'The number to padded is :',x
    if x != 0:
        fs_pad = files +'0'*(16-x)
        print 'fs_pad is :',fs_pad
        print len(fs_pad)
        print len(fs_pad)%16
    else:
        print 'The length of this file is a multiple of 16 '
    message = iv + cipher.encrypt(fs_pad)
    #生成密文文件流message,是基于实际密码的加密
    print 'File after AES is like :',binascii.b2a_hex(message[:10])
    #查看密文文件流的前十个字节(转换成十六进制查看)
    print u'解密之后为：',cipher.decrypt(message+iv)
    return message

#Create a Test file abd get FileSteam
files = open('test','w+')
# files.write('努力学习Python!')
# files.write('至精通方休~')
message_real = raw_input('Please input the message what you want to encrypt :\r\n')
files.write(message_real)
files.seek(0,0)
files_message = files.read()
print files_message
files.close()
key = raw_input('Please input your key(16 btyes):')

#Crypt this SRC FileStream
#将加密完的文件流写入fc文件中
fc = open('fc','wb')
fc_message = AES_File(files_message,key)
print fc_message
fc.writelines(fc_message)
fc.close()

raw_input('Enter for Exit...')
