## Level1
a.s
```
.global _start
.intel_syntax noprefix
_start:
	mov rdi, 0x1337
```
gcc -nostdlib -static -o a.elf a.s
objcopy --dump-section .text=a.bin a.elf
cat a.bin | /challenge/embryoasm_level1
pwn.college{c1tEi6f_VaaYW9pzT2FDFBo4P7p.0FN5EDLwIzW}

## Level2
same as level1 but do add rdi, 0x331337 instead
pwn.college{0HnRWJUKe8ExwGQLZAaQTPI3aSH.0VN5EDLwIzW}

## Level3
```
imul rdi, rsi
add rdi, rdx
mov rax, rdi
```
pwn.college{YS0lpFbEIIxJmQJRV9vPPBTx3HC.0lN5EDLwIzW}

## Level4
cheesed:
```
mov ax, di
div sil ;idiv works too
; run this until it leaks the flag
```
right, not-over-complicated way:
```
mov rax, rdi
div rsi
```
pwn.college{IR6Nd-i76hpeApMO_kf-fr78dQK.01N5EDLwIzW}

## Level5
cheesed way
```
mov rsi, rdi
div rax
```
gives unhandled error exception

more accurate cheesed way
```
mov rax, 0
mov al, sil
div rsi
```
pwn.college{8TKrbPMHXsrIrxs8_4Tx4MRUAMl.0FO5EDLwIzW}

## Level6
solve.py
```
mov rax, 0
mov al, dil ; lower 8 bits of rdi into lower 8 bits of rax
mov rbx, 0
mov bx, si ; lower 16 of rsi into lower 16 rbx
```
pwn.college{UWejoJijZ__U4tHGY9XBBGonpNV.0VO5EDLwIzW}

## Level7
```
mov rax, rdi 
shl rax, 32 // move completely to left
shr rax, 56 // move compeltely to right, fill w/ 0
```
pwn.college{orVIqIw06SdYjBDU8Hm5XKqWcfR.0FMwIDLwIzW}

## Level8
```
and rdi, rsi
or rax, 0xFFFFFF // set rax to all 1's
and rax, rdi // w/o move instruction
```
pwn.college{Ypk4p3Nz2Qtp08q2I4u2FPnFMC4.0VMwIDLwIzW}

## Level9
```
xor rax, rax
```
Not cheese:
```
//clear rax
xor rax, rax
//set the last bit to 1 (odd)
or rax, 0b1
//if even, set last bit to 1 else set to 0. This screws up the other bits tho
xor rax, rdi
//clear all but the last bit
and rax, 0b1
```
pwn.college{Erzx2O4k1prveU5R77F1ywZeca6.0lMwIDLwIzW}

## Level10
```
    mov rax, [0x404000]
    add dword ptr [0x404000], 0x1337
```
pwn.college{oJ2c0bIriZFgxVid5kxpRa95E8q.01MwIDLwIzW}

## Level11
```
    mov al, BYTE PTR[0x404000]
    mov bx, WORD PTR[0x404000]
    mov ecx, DWORD PTR[0x404000]
    mov rdx, QWORD PTR[0x404000]
```
pwn.college{Q1GqcWVfp1vAyzOCFr7IQ5Pk0dy.0FNwIDLwIzW}

## Level14
```
// rdi = 0x1354a, (stack) [0x7fffff1ffff8] = 0x14f0d766 (last 4 bytes is r8)
    pop r8
    sub r8, rdi
    push r8 // push new value back onto stack
```
pwn.college{8xQ3s0UBY62gEkY68Jy5g8s1WOn.01NwIDLwIzW}

## Level15
```
// rdi = 2, rsi = 5
// swap the 2 and 5
    push rdi
    push rsi
    pop rdi
    pop rsi // like taking jenga pieces out from the bottom
```
pwn.college{U1CJyAEBDPyXy2EwnrNL2GJ5dsJ.0FOwIDLwIzW}


## Level18
solve.py (don't ever run with comments)
```
#!/usr/bin/python3
import pwn

pwn.context.arch = "amd64"
pwn.context.encoding = "latin"
pwn.context.log_level = "INFO" #DEBUG, CRITICAL
pwn.warnings.simplefilter("ignore")

assembly = """
cmp dword ptr [rdi], 0x7f454c46 ; if [x] is 0x7f454c46:
jne else_if
; y = [x+4] + [x+8] + [x+12]
if:
    mov rax, 0 ;zero out rax
    add eax, dword ptr [rdi + 4] ;32-bit registers
    add eax, dword ptr [rdi + 8]
    add eax, dword ptr [rdi + 12]
    jmp post
; y = [x+4] - [x+8] - [x+12]
else_if:
    cmp dword ptr [rdi], 0x00005A4D ; else if [x] is 0x00005A4D:
    jne else
    mov eax, dword ptr [rdi + 4]
    sub eax, dword ptr [rdi + 8]
    sub eax, dword ptr [rdi + 12]
    jmp post
; y = [x+4] * [x+8] * [x+12]
else:
    mov rax, 1
    mul dword ptr [rdi + 4]
    mul dword ptr [rdi + 8]
    mul dword ptr [rdi + 12]
    jmp post
post:
    nop
"""

#with open("/flag") as f:
    #f.read()
with pwn.process(f"/challenge/{pwn.os.getenv('HOSTNAME')}") as target:
    pwn.info(target.readrepeat(1)) #read until no new data
    target.send(pwn.asm(assembly))
    pwn.info(target.readrepeat(1))


#print(pwn.asm(assembly))

```
pwn.college{gEX8OhAjDUe6We76z6Ws0WALHY9.0VMxIDLwIzW}

## Level20
solve.py
```
    mov rax, 0
    mov r12, rsi ; save n
loop:
    cmp rsi, 0 ; n=0, exit loop
    je done
    mov ebx, dword ptr [rdi] ; move last 4 bits to last 4 of rbx
    add rax, rbx ; move entire rbx to rax (set aside 64 bits of space for 32 bit computations so no overflow)
    add rdi, 4 ; add back (shift) 4 bits bc dword
    dec rsi ; keep decrementing counter n after each loop
    jmp loop
done:
    div r12
```
pwn.college{Mi7rY0bTndEaLn17MKItgafh4jj.01MxIDLwIzW}

## Level23
```
push rbp
mov rbp, rsp
sub rsp, 256 
# initialize all 256 as 0


mov r12, 0 #b
mov r13, 0 #i

loop: #for loop
cmp r13, rsi
je done
mov rax, 0
mov al, byte ptr [rdi+r13]
mov rbx, rbp
sub rbx, rax
inc byte ptr[rbx]
inc r13
jmp loop

done:
# 2nd loop
mov r13, 0
mov r14, 0
mov r15, 0

loop2:
cmp r13, 256
je done2
mov rbx, rbp
sub rbx, r13
mov rax, 0
mov al, byte ptr [rbx]
cmp rax, r14
jle not_greater
mov r14, rax
mov r15, r13

not_greater:
inc r13
jmp loop2

done2:
mov rax, r15


leave // mov rsp, rbp (stack=base ptr)
ret
```
pwn.college{4f8oPk4C-BstdZVcOBLhI7AgtXC.0lNxIDLwIzW}
