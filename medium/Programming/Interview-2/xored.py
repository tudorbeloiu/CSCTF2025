from pwn import remote
import re

def xor_from_string(s):
    pattern = re.search(r'BYTES:\s*([0-9A-Fa-f]{2}(?:[- ][0-9A-Fa-f]{2})*)', s)
    b_seq = pattern[1]
    
    hex_values = re.findall(r'[0-9A-Fa-f]{2}',b_seq)
    xor_val = 0
    for hv in hex_values:
        xor_val = xor_val ^ int(hv,16)
    return f"{xor_val:02x}"

HOST = "chals.2025.chronos-security.ro"
PORT = 35082

choice = "2"

r = remote(HOST,PORT)

banner = r.recvuntil(b'6) Binary TLV: type 0x42 varlen fragments -> string\n> ').decode(errors='ignore')
print(banner)
r.sendline(choice)

chall_output = r.recvuntil(b'Answer: ').decode('utf-8')
xor_value = xor_from_string(chall_output)

r.sendline(xor_value)

flag = r.recvline().decode('utf-8')
print(flag)