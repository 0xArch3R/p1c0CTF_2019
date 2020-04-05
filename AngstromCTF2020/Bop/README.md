## Bop it!

On taking a closer look at the souce code , the bug becomes pretty obvious.
```C
strncat(wrong, " was wrong. Better luck next time!\n", 35);
write(1, wrong, guessLen+35);
```

The binary takes input and writes it to stdout. Since fgets reads nullbytes but strncat stops after encountering the first null byte.
So, If we happen to give a lot of null bytes in our input. write() will have to print as many bytes and will end up leaking the flag..!
```bash
arch3r@1nv4d3r:~/git-repos/CTF-Writeups/AngstromCTF2020/Bop$ python exploit.py local NOPTRACE
[+] Starting local process './bop_it': pid 23218
[!] Skipping debug attach since context.noptrace==True
actf{this is not the flag}
```
