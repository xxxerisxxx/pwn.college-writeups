argv[555] = 'somestring'

https://www.geeksforgeeks.org/bash-scripting-for-loop/

https://linuxize.com/post/bash-for-loop/

# Level30
stdout needs to be a pipe
```/challenge/interactive_30 | rev > /tmp/temp```

## Level37
Basic redirect to stdout
```
import pwn

cat = pwn.process("cat")

proc = pwn.process("/challenge/interaction_level37",stdout=cat.stdin)

print(cat.recvall(2).decode())

proc.interactive()
```

# Level41
Asking to compile a c program
Fork
Redirect stdout to another process

C: looks just like stock Level30 dojo
``` ./41 | cat > /tmp/temp ```

# Level48

![48](https://user-images.githubusercontent.com/45490952/151486697-b22af2c5-878e-46e3-b3b5-c5cf395b1664.png)

# Level56
C program needs argv[0] to be /tmp/wewngt
argv[0] pass in differently from path to execute

C:
```
int pid = fork();
if(pid==0) {
		static char *argv[] = {"/tmp/wewngt"};
		execv("/tmp/wewngt", argv);
		exit(127);
	
	}
```
