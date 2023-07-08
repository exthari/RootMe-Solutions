
import socket
from pwn import *
import math

#encode --> string to bytes
#decode --> byte to string

def send(s,user,msg):
    s.send(f"PRIVMSG {user} :{msg}\n".encode())

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
print(s.recv(2048))
print(s.recv(2048))
send(s,"candy","!ep1")
#s.send(b"PRIVMSG candy :!ep1\n")
#print(s.recvline())
a = s.recvline().split()
n1 = int(a[3].strip(b":"))
n2 = int(a[5])
print(n1 , n2)
ans = round(math.sqrt(n1) * n2 , 2)
print(ans)
send(s,"candy",f"!ep1 -rep {ans}")
print(s.recv(2048))
