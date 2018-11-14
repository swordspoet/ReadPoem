#!/usr/bin/bin python
# coding: utf-8

from socket import *

host = 'localhost'
port = 21765
buff_size = 1024
address = (host, port)

cli_sock = socket(AF_INET, SOCK_STREAM)
cli_sock.connect(address)

while 1:
    query = input("念诗一首: ")
    if not query:
        break
    cli_sock.send(query.encode())
    data = cli_sock.recv(buff_size).decode()
    if not data:
        break
    print(data)

cli_sock.close()
