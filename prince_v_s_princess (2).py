#program to help  prince to find his princess
#prepared by shoukkiya 02/10/2018
def Palace(n):
    while(i<=n):
        if(i==(int(n/2))+1):
            print("___________________");
            print("|___|\t|_#_|\t|___|");
        else :
            print("___________________");
            print("|___|\t|___|\t|___|");
        i=i+1;
n=3;
i=1;
print("\n\n----------------------------------- ");
print("\t \twelcome to palace round");
print("----------------------------------- ");
while(i<=n):
    if(i==(int(n/2))+1):
        print(" ____________________");
        print("|___|\t|___|\t|_*_|");
    else :
        print(" ____________________");
        print("|___|\t|___|\t|___|");
    i=i+1;
#Palace(5);
print("----------------------------------- ");
print("        _____      ");
print("    \t _#_ \t    ");
print("\t -|-         ");
print("\t / \        ");
print("----------------------------------- ");
print("\t \t\t \tprincess where are u !!!")
print("=======================================")

#to find out the princess
i=0;
j=0;
room=[[0,0,0],[0,0,0],[0,0,0]];
#for i in range(n):
    #for j in range(n):
        #print(room[i][j]);
    #print("\n");
rowp=int(input("enter the row position of princess "))
colp=int(input("enter the col position of princess "))
#cc
room[rowp][colp]=1;
#print (room)
#flag=0;
#for i in range(len(room)):
    #for k in range(len(room)):
        #if(room[i][j]==1):#checking whether there is princess
        #    rowp=i;
        #    colp=j;
        #    flag=1;
        #    break;
        #else :
        #    flag=0;
#if flag==1:
#    print("found her within in the Palace..")
#else:
#    print("can't find her in the palace....  ")
#finding positin of prince assume always center
rowpr=int(len(room)/2);
colpr=int(len(room)/2);
#finding the position of princess
print("----------------------------------- ");
print("         ,,,      ");
print("    \t ,*, \t    ");
print("\t ,|,         ");
print("\t / \        ");
print("----------------------------------- ");

if(rowp==rowpr):
    if(colp==colpr):
        print("i'am with u..");
    elif(colp-colpr<0):
        print("Left of u..");
    elif(colp-colpr>0):
        print("right of u..");
elif(colp==colpr):
    if(rowp-rowpr<0):
        print("Top of u..");
    elif(rowp-rowpr>0):
        print("bottom of u");
elif(rowp-rowpr<0):
    if(colp-colpr<0):
        print("TOP LEFT");
        print("\t \tDear prince come this way ---LEFT TOP");
        print("\t \t------------------");
        print("\t \t|   / \          |");
        print("\t \t|    |           |");
        print("\t \t|    |           |");
        print("\t \t|     <-----#    |");
        print("\t \t------------------");
    else :
        print("TOP RIGHT");
        print("\t \tDear prince come this way ---RIGHT TOP ");
        print("\t \t------------------");
        print("\t \t|         / \      |");
        print("\t \t|          |       |");
        print("\t \t|          |       |");
        print("\t \t|     #------>     |");
        print("\t \t-------------------")
else :
    if(colp-colpr>0):
        print("BOTTOM RIGHT");
        print("\t \tDear prince come this way---DOWN RIGHT ");
        print("\t \t------------------");
        print("\t \t|   #|            |");
        print("\t \t|    |            |");
        print("\t \t|   \ /           |");
        print("\t \t|    '----->      |");
        print("\t \t------------------");

    else :
        print("BOTTOM LEFT");
        print("\t \tDear prince come this way---DOWN LEFT ");
        print("\t \t------------------");
        print("\t \t|          #|    |");
        print("\t \t|           |    |");
        print("\t \t|          \ /   |");
        print("\t \t|    '<-----     |");
        print("\t \t------------------");
