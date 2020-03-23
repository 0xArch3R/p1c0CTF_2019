# CanaRy

Ooh ... this one seems pretty fun

The binary in this challenge seems to have a **stack canary** and so, trying to simply overflow this buffer wont be easy as we are greeted with this message every time we corrupt the value of the canary with our input.
``` bash
arch3r@1nv4d3r:~/p1c0CTF_2019/C4naRy$ ./vuln
Please enter the length of the entry:
> 33
Input> aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
*** Stack Smashing Detected *** : Canary Value Corrupt!

```
hmmm... we'll have to try and leak the value of this canary and use it in our payload so that it lines up with the actual canary on the stack.

bruteforcing the canary one byte at a time will do the trick since we already know that it is 4 bytes long. 

### but... thats not all folks

this particular binary has a mitigation for overflow attacks 

Address Space Layout Randomization is a computer security technique which involves randomly positioning the base address of an executable and the position of libraries, heap, and stack, in a process's address space.

So we will have to run a loop until our address matches up with the address on the stack.

