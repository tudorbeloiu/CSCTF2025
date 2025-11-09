# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: challenge.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import sys
import os
import json
import time
import base64
import zlib
import hashlib
from Crypto.Cipher import AES
PEPPER = b'Croissant-CTF-2025'

def resource_path(relpath: str) -> str:
    base = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(base, relpath)

def load_blob():
    with open(resource_path('blob.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def derive_argument_from_assets() -> str:
    png = open(resource_path('chronos_kronos.png'), 'rb').read()
    blob = open(resource_path('table.bin'), 'rb').read()
    crc = zlib.crc32(png).to_bytes(4, 'big')
    sha1 = hashlib.sha1(blob).digest()
    digest = hashlib.sha256(crc + sha1 + PEPPER).digest()
    print(base64.b32encode(digest).decode().rstrip('='))
    return base64.b32encode(digest).decode().rstrip('=')

def derive_key(candidate: str, BLOB: dict) -> bytes:
    return hashlib.scrypt(candidate.encode('utf-8'), salt=bytes.fromhex(BLOB['salt_hex']), n=2 ** int(BLOB.get('nexp', 18)), r=int(BLOB.get('r', 8)), p=int(BLOB.get('p', 1)), dklen=int(BLOB.get('dklen', 32)), maxmem=2000000000)

def try_decrypt(candidate: str, BLOB: dict) -> str | None:
    key = derive_key(candidate, BLOB)
    nonce = bytes.fromhex(BLOB['nonce_hex'])
    ct = bytes.fromhex(BLOB['ct_hex'])
    tag = bytes.fromhex(BLOB['tag_hex'])
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    try:
        return cipher.decrypt_and_verify(ct, tag).decode('utf-8')
    except Exception:
        return None
    else:
        pass

def main():
    if len(sys.argv) != 2:
        print('Usage: challenge <argument>')
        return
    BLOB = load_blob()
    _ = derive_argument_from_assets()
    flag = try_decrypt(sys.argv[1], BLOB)
    if flag is None:
        time.sleep(0.25)
        print('Wrong argument.')
    else:
        print(flag)
if __name__ == '__main__':
    main()