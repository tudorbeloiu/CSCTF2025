from pwn import remote
import base64
import re

def dec_concat(s):
    lines = s.strip().split('\n')
    lines = lines[:-1]
    dict = {}
    result = ""
    for linie in lines:
        gr,sir = linie.split(":")
        dict[int(gr[0],10)] = base64.b64decode(sir).decode('utf-8')
    
    return ''.join(dict[cheie] for cheie in sorted(dict))

    

HOST = "chals.2025.chronos-security.ro"
PORT = 35167

choice = "3"
r = remote(HOST,PORT)

banner = r.recvuntil(b'6) Binary TLV: type 0x42 varlen fragments -> string\n> ').decode(errors='ignore')
r.sendline(choice)

banner2 = r.recvuntil(b'BEGIN\n')

chall_output = r.recvuntil(b'\nE').decode(errors='ignore')

rAns = r.recvline()

result = dec_concat(chall_output)

r.sendline(result)

flag = r.recvline().decode('utf-8').split(" ")

print(flag[2])
