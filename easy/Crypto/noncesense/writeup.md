## Noncesense -> 100p
## Category -> Crypto

---

From the archive I extracted:
-> `notflag.png` a normal PNG file
-> `notflag.png.enc` a file that looks like a ciphertext
-> `flag.enc` another ciphertext(this should be our flag)

So I have one pair, ciphertext and its plaintext and another ciphertext.

If both my .enc files were encrypted with the same key, that means the keystream is notflag.png.enc XOR notflag.png.

If i have cipher1 = plain1 XOR K
          cipher2 = plain2 XOR K

        then => cipher1 XOR cipher2 = plain1 XOR plain2

I wrote a python script and got the flag:

![flag.png](img/flag.png)