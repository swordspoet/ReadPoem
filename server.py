#!/usr/bin/env python
# coding: utf-8

from socket import *
from poetry_request import poetry_query


host = 'localhost'
port = 21765
buff_size = 1024
address = (host, port)                      # 主机-地址对

server_sock = socket(AF_INET, SOCK_STREAM)  # 创建服务器套接字
server_sock.bind(address)                   # 套接字与主机-地址对绑定
server_sock.listen(5)                       # 监听连接


while 1:      # 服务器无线循环
    cli_sock, addr = server_sock.accept()         # 接受客户端连接，开启单线程服务器

    while 1:  # 通信无限循环
        query = cli_sock.recv(buff_size).decode()  # 接受客户端消息
        if not query:
            break
        query = poetry_query()
        print(query.get('result').get('content'))  # 从API返回结果中提取诗句内容并发送至客户端
        content = query.get('result').get('content')
        cli_sock.send(bytes(content.encode('utf8')))

        # auth.save_voice(content.encode('utf8'), 'test')
        # player.play_voice_by('test')

    cli_sock.close()
server_sock.close()
