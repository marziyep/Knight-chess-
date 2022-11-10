twodlist=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
print(f"{twodlist[0]} \n{twodlist[1]}\n{twodlist[2]}\n{twodlist[3]}\n{twodlist[4]}\n{twodlist[5]}\n{twodlist[6]}\n{twodlist[7]}")
print("----------------------------------------------------------------------------------------")

import random
random1=random.randint(0,7)
random2=random.randint(0,7)
twodlist[random1][random2]="x"
print(f"{twodlist[0]} \n{twodlist[1]}\n{twodlist[2]}\n{twodlist[3]}\n{twodlist[4]}\n{twodlist[5]}\n{twodlist[6]}\n{twodlist[7]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
def  horse(random1,random2):
        chosen1=[]
        chosen2=[]
        final=[]

        if random1+2<=7:
            chosen1.append(('down',2))
        if random1+1<=7:
            chosen1.append(('down',1))
        if random1-2>=0:
            chosen1.append(('up',2))
        if random1-1>=0:
            chosen1.append(('up',1))
        if random2+2<=7:
            chosen2.append(('right',2))
        if random2+1<=7:
            chosen2.append(('right',1))
        if random2-2>=0:
            chosen2.append(('left',2))
        if random2-1>=0:
            chosen2.append(('left',1))
        for (a,b) in chosen1:
            for (c,d) in chosen2:
                if int(b)+int(d)==3:
                    final.append([a,b,c,d])

        for (c, d) in chosen2:
            for (a, b) in chosen1:
                if int(b) + int(d) == 3:
                     final.append([c, d, a, b])

        print(final)

        for movement in final:
           if movement[0] in ['right','down']:
               movement[0]=1
           if movement[0] in ['up','left']:
               movement[0]=-1
           if movement[2] in ['right','down']:
               movement[2]=1
           if movement[2] in ['up','left']:
               movement[2]=-1

           if random1 + (movement[0] * movement[1])>7 or random2 + (movement[2] * movement[3])>7:

             twodlist[random1 + (movement[2] * movement[3])][random2 + (movement[0] * movement[1])] = 1
             twodlist[random1][random2]='x'
           else:
            twodlist[random1 + (movement[0] * movement[1])][random2 + (movement[2] * movement[3])] = 1
            twodlist[random1][random2] = 'x'
        print(f"{twodlist[0]} \n{twodlist[1]}\n{twodlist[2]}\n{twodlist[3]}\n{twodlist[4]}\n{twodlist[5]}\n{twodlist[6]}\n{twodlist[7]}")

horse(random1,random2)