from pathlib import Path


def decrypt_flag(flag_enc,keystream):
    flag_pl = bytearray()
    keystreamLen = len(keystream)
    for i,b in enumerate(flag_enc):
        flag_pl.append(b ^ keystream[i%keystreamLen])
    return bytes(flag_pl)


notflag_plain = Path("notflag.png").read_bytes()
notflag_enc = Path("notflag.png.enc").read_bytes()
flag_enc = Path("flag.enc").read_bytes()

key_len = min(len(notflag_plain),len(notflag_enc))

keystream = bytes([notflag_plain[i] ^ notflag_enc[i] for i in range(key_len)])

flag_plain = decrypt_flag(flag_enc=flag_enc, keystream=keystream)
print(flag_plain)
