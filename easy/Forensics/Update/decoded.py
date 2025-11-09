import base64

enc_string = "QwBTAEMAVABGAHsAcwBoADAAcgB0AGMAdQA3AHMAXwBjADQAbgBfAGIAMwBfAGQANABuAGcAMwByAG8AdQBzAH0A"

dec_string = base64.b64decode(enc_string)

flag = dec_string.replace(b"\x00",b'')
print(flag.decode('ascii'))