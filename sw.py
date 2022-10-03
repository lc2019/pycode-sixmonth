# 目录结构如下：只需要改动前两个配置文件

# -rw-r--r-- 1 root root 79 Mar 14 23:53 cmd.txt
#
# -rw-r--r-- 1 root root 274 Mar 14 23:32 conf.py
#
# -rw-r--r-- 1 root root 933 Mar 14 23:51 ssh_sw_cmd.py

# cmd.txt用来存放要配置到交换机的命令,内容如下(以下内容为配置NTP)。
#
# sys
#
# ntp unicast-peer 192.168.6.100 version 4 source-interface LoopBack0
#
# commit
#
# conf.py 保存交换机的管理IP,及登陆交换机的用户名密码
#
# # -*- coding: utf-8 -*-
#
# # !/usr/bin/python
#
# #要执行操作的交换机管理
#
# swip={undefined
#
# 'testare4' : '172.16.200.6',
#
# 'testare1' : '10.57.1.22',
#
# };

# #交换机SSH用户名密码
#
# username = "wsf535" #用户名
#
# passwd = "****" #密码
#
# threads = [10] #多线程
#
# ss_sw_cmd.py为主运行文件
#
# #-*- coding: utf-8 -*-
##!/usr/bin/python

import paramiko

import threading

import time

import os

from conf import *

# 拿到cmd.txt文件中的命令

with open('./cmd.txt', 'r') as f:

cmd_line = f.readlines()

cmd = []

for c in cmd_line:

cmd.append(c)


# 定义连接与操作

def ssh2(ip, username, passwd, cmd):


try:

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(ip, 22, username, passwd, timeout=5)

ssh_shell = ssh.invoke_shell()

for m in cmd:

res = ssh_shell.sendall(m)

time.sleep(float(1))

print
ssh_shell.recv(1024)

ssh.close()

except:

print
'%s\tError\n' % (ip)

if __name__ == '__main__':

print
"Begin......"

for key in swip:

ip = swip[key]

a = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))

a.start()
