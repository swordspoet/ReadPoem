#!/usr/bin/env python
# coding: utf-8

from socket import *
from poetry_request import poetry_query
from voice import Voice
from player import Player


host = 'localhost'
port = 21765
buff_size = 1024
address = (host, port)

server_sock = socket(AF_INET, SOCK_STREAM)
server_sock.bind(address)
server_sock.listen(5)

secret_id = 'LTAIsxMZyCpb7QFN'
secret_key = 'uIRdXxLS4UyMbLY1uk5N3CI4SLl7AV'
auth = Voice(secret_id, secret_key)
player = Player()


while 1:
    cli_sock, addr = server_sock.accept()

    while 1:
        query = cli_sock.recv(buff_size).decode()
        if not query:
            break
        query = poetry_query()
        print(query.get('result').get('content'))
        content = query.get('result').get('content')
        cli_sock.send(bytes(content.encode('utf8')))

        auth.save_voice(content.encode('utf8'), 'test')
        player.play_voice_by('test')

    cli_sock.close()
server_sock.close()
