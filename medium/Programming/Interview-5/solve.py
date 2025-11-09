from pwn import remote
import hmac
import hashlib
import base64
import re

HOST = "chals.2025.chronos-security.ro"
PORT = 35347

choice = "5"

r = remote(HOST,PORT)
banner = r.recvuntil(b'6) Binary TLV: type 0x42 varlen fragments -> string\n> ').decode('utf-8',errors='ignore')
r.sendline(choice)

r.recvuntil(b'only.\n')

resp = r.recvuntil('\nA').decode('utf-8')

resp = resp[:-1]

print(resp)

parts = dict(re.findall(r'([A-Za-z0-9_+-]+)=([^\s]+)', resp))

secret = parts['secret']
header = parts['header']
payload = parts['payload']

new_hmac = hmac.new(secret.encode(),(header+"."+payload).encode(),hashlib.sha256).digest()

msg_sent = base64.urlsafe_b64encode(new_hmac).rstrip(b'=').decode()
r.sendline(msg_sent.encode())

print(r.recvall().decode(errors='ignore'))

r.close()