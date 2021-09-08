## Level1
gcc -nostdlib -static -o solve.elf solve.s && objcopy --dump-section .text=solve.bin solve.elf
objdump -M intel -d solve.elf //view the shellcode
hd solve.bin
strace ./solve.elf
```

```

