import hashlib

lines = []
with open("f-l-a-g.txt","r") as f:
    for linie in f:
        lines.append(linie.strip())

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()}{;[]',./?`~_-+=|"

dict = {hashlib.sha256(ch.encode()).hexdigest(): ch for ch in chars}

flag = ""
for linie in lines:
    flag = flag + dict.get(linie,"?")
print(flag)