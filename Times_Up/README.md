# Times-Up

This challenge requires us to be fast ...

The binary generates a random mathematical expression and gives us the flag only if we give it back the answer within the time limit(which is really small).


So..  lets start scripting...

We simply need to read the input after "Challenge : " and use ```eval()``` to evaluate the string.

```bash
arch3r@1nv4d3r:~/Downloads$ python times.py 
[+] Starting local process './times-up': pid 2925
Setting alarm...
Solution? Congrats! Here is the flag!
CTF{fl4g}
[*] Process './times-up' stopped with exit code 0 (pid 2925)
```
