#!/usr/bin/bin python
# coding: utf-8

from socket import *
from voice import Voice
from player import Player


host = 'localhost'
port = 21765
buff_size = 1024
address = (host, port)

cli_sock = socket(AF_INET, SOCK_STREAM)
cli_sock.connect(address)
# 阿里云语音合成配置（秘钥可以找我索取）
secret_id = ''
secret_key = ''
auth = Voice(secret_id, secret_key)
player = Player()


while 1:
    query = input("念诗一首: ")
    if not query:
        break
    cli_sock.send(query.encode())
    data = cli_sock.recv(buff_size).decode()  # 客户端接收来自服务器的消息
    print(data)

    auth.save_voice(data.encode('utf8'), 'test')  # 将服务器返回的诗句合成为MP3文件
    player.play_voice_by('test')                  # 调用系统播放器播放MP3文件
    if not data:
        break

cli_sock.close()
