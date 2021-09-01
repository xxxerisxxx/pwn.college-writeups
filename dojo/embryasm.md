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
