#Mirrored triangle

r=int(input("Enter number of rows:"))
for i in range (1,r+1):
     for j in range (1,r+1):
          if(j<= r-1):
            print('' ,end='')
        else:
            print('$',end='')
    print()
              

