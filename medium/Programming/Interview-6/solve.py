from pwn import remote

HOST = "chals.2025.chronos-security.ro"
PORT = 35404

choice = "6"
r = remote(HOST,PORT)
banner = r.recvuntil(b'6) Binary TLV: type 0x42 varlen fragments -> string\n> ')
r.sendline(choice)
r.recvuntil(b"HEX: ")
hex_val = r.recvuntil(b'\nAn').decode('utf-8',errors='ignore')
hex_val = hex_val[:-2]
print(hex_val)

data = bytes.fromhex(hex_val)

i = 0
fragm = []

while i< len(data):
    t = data[i]
    length = int.from_bytes(data[i+1:i+3],"big")

    val_st = i + 3
    val_end = val_st + length

    val = data[val_st:val_end]

    if t == 0x42:
        idx = val[0]
        dlen = val[1]
        fragm_data = val[2:2+dlen]
        fragm.append((idx,fragm_data))
    
    i = val_end

fragm.sort(key = lambda x: x[0])
ans_bytes = b"".join(pc for _, pc in fragm)

print(ans_bytes.decode('ascii',errors='ignore'))

r.sendline(ans_bytes)

print(r.recvall().decode('utf-8',errors='ignore'))