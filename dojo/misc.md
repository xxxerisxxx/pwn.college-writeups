### Reading elf to cat out flag?
readelf -a /challenge/embryoio_level3 | grep interpret
/lib64/ld-linux-x86-64.so.2 /challenge/embryoio_level3 flag

### Number generator for Program Interaction modules
```
for x in range(1, 247):
    print(str(x) + " ", end="")
```

### Create symlink
ln -s /link/to/binary slink_nickname

Lvl68 alternative: ```./script.sh foo{1..334} nbtdcccras```

### Vim
yy //yank(copy)
p //paste
^ all in visual mode
:s/foo/bar/g //search foo, rplace w/ bar

Beef Stroganoff //Russian

### Error msgs
My current working directory is incorrect! It should be '/tmp/driqoc', but it is '/home/hacker'.

argv[247] should have a value of jiyiggsgfo

*you CANNOT mkdir /tmp/dir & cd /tmp/dir in the same line; has to be 2 separate lines >:P

argv[318] should have a value of lmuuituqtn
'297' environment variable should have a value of odtfhrheil

# Pwntools
### Level50-51 examples
p1=pwn.process(["/bin/cat"]) #Pipes
p2=pwn.process(glob.glob("embryo"), stdout=p2.stdin) #Pipe to stdin
print(p2.readall().decode()) #Bytestring
