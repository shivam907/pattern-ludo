print("We are winners")
for i in range(0,6):
    for j in range(0,6):
        if(j==0 or j==4 or i==0 or i==4):
            print("* ",end='')
        else:
            print("  ",end='')
    print()

n=int(input("Enter value of n"))

for i in range(0,n):
    for j in range(0,i):
        print("* ",end='')
    print()
for i in range(0,n):
    for j in range(5,i,-1):
        print("* ",end='')
    print()

num = [1,2,3,4,5]
n=int(input("Enter value of n"))
for i in range(0,n):
    for j in range(5,i,-1):
        print("  ",end='')
    p=i+1
    for k in range(0,i+1):
        print(p,"",end='')
        p-=1
    for u in range(0,i):
        print(u+2,"",end='')
        # num[k]-=1
    print()

k=1
n=int(input("Enter value of n"))
for i in range(0,n+1):
    for j in range(0,i):
        print(k,' ',end='')
        k+=2
    print()
n=int(input("Enter value of n"))

for i in range(0,n+1):
    for j in range(n,i,-1):
        print('  ',end='')
    for k in range(0,i):
        if(i==0 or i==n or k==0):
            print('* ',end='')
        else:
            print('  ',end='')
    for k in range(1,i):
        if(i==n or k==i-1):
            print('* ',end='')
        else:
            print('  ',end='')
    print()

str=[65,66,67,68,69]
n=int(input("Enter value of n"))
for i in range(0,n+1):
    ko=0
    for j in range(0,i):
        c=chr(str[i-1]-ko)
        ko+=1
        print(c,' ',end='')

        # c=chr(int(c)-1)
        
    print()
str=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81]
ko=0
n=int(input("Enter value of n"))
for i in range(0,n+1):
    for q in range(n,i,-1):
        print('  ',end='')
    
    for j in range(0,i):
        c=chr(str[i-1]+ko)
        print(c,'',end='')

        ko+=1
        
        # c=chr(int(c)-1)
        
    print()

n=int(input("Enter value of n"))
for i in range(0,n+1):
    for j in range(0,i):
        print((j+1)*(j+1),' ',end='')
    print()

str=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81]
n=int(input("Enter value of n"))
pio=0
lef=""
for i in range(0,n+1):
    for syncu in range(n,i,-1):
        print('  ',end='')
    lef=""
    for j in range(0,i):
        c= chr(str[i]-1+pio)
        lef=lef+" "+c
        # print(c,'',end='') 
        pio+=1
    nes=""
    for ok in lef:
        nes=ok+nes
    print(nes,end='')
    pio=0
        # c=chr(int(c)+1)
    print()


n=int(input("Enter value of n"))
for i in range(0,n+1):
    for j in range(n+1,i,-1):
        print('  ',end='')
    for k in range(0,i):
        print(i,'',end='')
    
    for k in range(1,i):
        print(i,'',end='')
    print()
    
        
