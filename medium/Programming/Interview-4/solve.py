from pwn import remote
import hmac,hashlib

HOST = "chals.2025.chronos-security.ro"
PORT = 35287

choice = "4"
r = remote(HOST,PORT)

banner = r.recvuntil(b'6) Binary TLV: type 0x42 varlen fragments -> string\n> ').decode('utf-8',errors='ignore')
r.sendline(choice)

r.recvuntil(b'lower.\n')

resp = r.recvuntil(b'\n').decode('utf-8').strip()

parts = dict(item.split('=') for item in resp.split())

key = parts['key']
token = parts['token']
salt = parts['salt']

message = token + salt

dig = hmac.new(key.encode(),message.encode(),hashlib.sha256).hexdigest()

r.sendline(dig.lower())
r.recvuntil('OK ')

flag = r.recvline().decode('utf-8')
print(flag)