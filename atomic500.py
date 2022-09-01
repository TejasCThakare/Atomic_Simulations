import csv
import numpy as np

# Now, We will generate the x,y,z coordinates of n gas molecules
s0=input("enter number of molecules  n = " )
n=int(s0)
cutoff=float(input("Enter the cutoff value = "))
s1=np.random.random_sample((n,3,1))

#Initialising empty lists
p=[]
d=[]
dd=[]
l1=[]
l2=[]

# Generating gas molecules in the box of dimension 16 by 16 by 8
for i in range(0,n):
    for j in range(0,3):
        for k in range(0,1):
            p.append((s1[i][j][k])*16)

#Scaling the z-coordinates
for i in range(2,(n*3)+(n-1),4):
    o=p[i]*0.5

    #inserting the scaled z-coordinate in ith index of list p
    p.insert(i,o)

# deleting the extra unscaled z-coordinate in list p
del p[3:(n*3)+n:4]

#Reshaping the 1D p list to 2D list
p1=list(np.reshape(p,(n,3)))

#Now, To calc distance between consecutive pair
for i in range(0,(n)):

    for l in range(1,(n)):
        if i==l:
            continue
        elif i>l:
            continue

        else:
            dist0 = (((p1[i][0] - p1[l][0]) ** 2) + ((p1[i][1] - p1[l][1]) ** 2) + ((p1[i][2] - p1[l][2]) ** 2))
            dist1 = np.sqrt(dist0)
            l1.append(i)
            l1.append(l)
            l1.append(dist1)

            # Applyig cuttoff
            if dist1>cutoff:
                d.append(p1[i][0])
                d.append(p1[i][1])
                d.append(p1[i][2])

                d.append(p1[l][0])
                d.append(p1[l][1])
                d.append(p1[l][2])
            else:
                dd.append(p1[i][0])
                dd.append(p1[i][1])
                dd.append(p1[i][2])

                dd.append(p1[l][0])
                dd.append(p1[l][1])
                dd.append(p1[l][2])



qqq0=len(dd) #calculating length of the list which contains every atom including repeated one which has distance < cutoff

print("\n The molecules having distance less that cutoff ,repeated \n")
d0=np.reshape(dd,(int(qqq0//3),3))


#now, removing duplicate lists appeared in 2d list d0 without changing an order. credit: Stack overflow
seen = set()
freshh2o = []
for item in d0:
    t = tuple(item)
    if t not in seen:
       freshh2o.append(item)
       seen.add(t)


qqq1=len(d)#calculating length of the list which contains every molecules including repeated one which has distance > cutoff

print("\n The molecules having distance greater that cutoff ,repeated \n")
d01=np.reshape(d,(int(qqq1//3),3))

#now, removing duplicate lists appeared in 2d list d01 without changing an order. credit: Stack overflow
seen1 = set()
freshh2o1 = []
for item1 in d01:
    t11 = tuple(item1)
    if t11 not in seen:
       freshh2o1.append(item1)
       seen1.add(t11)

#make a final new[] list for storing those water molecules which has distance less than cutoff ,
new=[]
for rr in d01:
    if rr not in d0:
        new.append(rr)
# n0=len(new)
# new1=np.reshape(new,((int(n0//3)),3))
seen11 = set()
freshh2o11 = []
for item11 in new:
    t111 = tuple(item11)
    if t111 not in seen11:
       freshh2o11.append(item11)
       seen11.add(t111)

#----------------------------------------------------------------------------------------------
# Storing the General Gas molecules in text file

n01=len(p1)
fc=open('data.txt','w')
fc.write(str(n01)+'\n')
fc.write('gas'+'\n')
one=1

#storing gas molecules int text file
for rr1 in range(0,len(p1)):
    fc.write('%4.2f\t%4.2f\t%4.2f\t%4.2f\n' % (one,p1[rr1][0],p1[rr1][1],p1[rr1][2]))
fc.close()

# ------------------------------------------------

# Storing the gas molecules after applying the cutoff
n0=len(freshh2o11)
f=open('data_dist_cutoff.txt','w')
f.write(str(n0)+'\n')
f.write('dist cutoff'+'\n')
one=1

#storing gas molecules int text file after applying the cutoff
for r1 in range(0,len(freshh2o11)):
    f.write('%4.2f\t%4.2f\t%4.2f\t%4.2f\n' % (one,freshh2o11[r1][0],freshh2o11[r1][1],freshh2o11[r1][2]))
f.close()

#-----------------------------------------------------------------------------------------

print("\n Coordinates of atoms x,y,z \n")
for row in p1:
    print(* row)


print("\n The distance pair are\n ")
l2=np.reshape(l1,(len(l1)//3,3))
for di in l2:
    print(*di)

print("\n The final sorted molecules coordinates are \n")
for rrr in freshh2o11:
    print(*rrr)
