
import socket
from pwn import *
import string

#encode --> string to bytes
#decode --> byte to string

def send(s,user,msg):
    s.send(f"PRIVMSG {user} :{msg}\n".encode())

def rot13(text):
    rot13 = str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return text.translate(rot13)


#s = socket.socket()
#s.connect(("irc.root-me.org", 6667))
s = remote("irc.root-me.org" , 6667)

print(s.recvline())
print(s.recvline())
s.send(b"USER hari hari hari :python\n")
s.send(b"NICK Hari\n")
print(s.recvline())
print(s.recvline())
print(s.recv(2048))
print(s.recv(2048))
s.send(b"JOIN #root-me_challenge\n")
print(s.recvuntil(b"/NAMES list.\r\n"))
send(s,"candy","!ep3")
#s.send(b"PRIVMSG candy :!ep1\n")
#print(s.recvline())
a = s.recvline().split()
enc = rot13(a[-1].strip(b":").decode())
send(s,"candy",f"!ep3 -rep {enc}")
print(s.recv(2048))
