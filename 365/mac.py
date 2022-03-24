from pwn import *
#import pwn

proc = process("/challenge/midtermctf_MACAttack")
#print(proc.recvall(2).decode())
q1 = proc.recvuntil('?\n')
print(b'q1')

if 
proc.sendline(b'yes')
#print(proc.recvall(2).decode())

proc.interactive()
