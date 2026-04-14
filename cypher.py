import sys


if len(sys.argv)!=3:
    sys.exit(1)

keyfile=sys.argv[1]
plaintxtfile=sys.argv[2]

with open(keyfile,'r') as file:
    lines=[l.strip() for l in file if l.strip()!='']
n=int(lines[0].split()[0])
hillKey=[list(map(int,lines[i+1].split())) for i in range(n)]

with open(plaintxtfile,'r') as f:
    data=f.read()
letters=[c.lower() for c in data if c.isalpha()]
padding=(n - (len(letters)%n))%n

if padding:
    letters+=['x']*padding

def blockChunk(lst,size):
    for i in range(0,len(lst),size):
        yield lst[i:i+size]

ct=[]

for block in blockChunk(letters,n):
    numb=[ord(c)-97 for c in block]
    result=[0]*n
    for i in range(n):
        s=0
        for j in range(n):
            s+=hillKey[i][j]*numb[j]
        result[i]=s%26
    ct.extend([chr(x+97) for x in numb])

def printMatrix(m):
    print()
    print("Key matrix:")
    for row in m:
        line=''.join("{:4d}".format(x) for x in row)
        print(line)

def printBlock(title, array):
    print()
    print(title)
    for i in range(0,len(array),80):
        print(''.join(array[i:i+80]))


printMatrix(hillKey)
printBlock("Plaintext:", letters)
printBlock("Ciphertext:", ct)

'''=============================================================================
| I Max Kaplan (ma234101) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================='''