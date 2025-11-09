## Secret -> 100p
# Category => Misc

---

Inside the extracted archive I found `flag.txt` encrypted with git-crypt:

![gitcrypt](img/gitcrypt.png)

I have to found the key to decrypt it.

![confirm.png](img/confirm.png)

This confirms that flag.txt and other files inside secrets are protected with git-crypt.
The challenge is giving a hint to look at commits, and I got this:

![commit.png](img/commit.png)

![fake.png](img/commit.png)

Ok so this commit only added the rule inside .gitattributes, but I found this commit:

![secret.png](img/secret.png)

![flag.png](img/flag.png)

There it is our decrypted flag!