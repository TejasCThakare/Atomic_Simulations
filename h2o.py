import numpy as np
import csv

s = input("enter the number of molecules = ")
n = int(s)
cut = input("enter the cutoff distance = ")
cutoff = float(cut)

#initialise the lists
q = []
l1 = []
qq = []
d=[]
mo=[]
dd=[]

#Generate coordinates
for i_ in range(0, n):
    for j_ in range(0, 1):
        x1 = (np.random.rand(1)) * 10
        y1 = (np.random.rand(1)) * 10
        z1 = (np.random.rand(1)) * 10

        # Creating array of water molecules just for printing not saving in any file
        o = ["O", *x1, *y1, *z1]
        h1 = ["H", *x1 + 0.56, *y1 + 0.803, *z1]
        h2 = ["H", *x1 + 0.56, *y1 - 0.803, *z1]

        # for the calculation of distance
        o_ = [*x1, *y1, *z1]
        h1_ = [*x1 + 0.56, *y1 + 0.803, *z1]
        h2_ = [*x1 + 0.56, *y1 - 0.803, *z1]

        # appending water molecules list with string t
        q.append(o)
        q.append(h1)
        q.append(h2)

        # for the calculation of distance between consecutive pairs, we append water molecule list w/o string
        qq.append(o_)
        qq.append(h1_)
        qq.append(h2_)

# -----------------------------------------------------------------------------------------------------------

# Storing water molecules in text without cutoff on it
n01=len(qq)
fc=open('h2o_molecules.txt','w')
fc.write(str(n01)+'\n')
fc.write('h2o'+'\n')


for rr1 in range(0,len(qq),3):
    fc.write('%4.2s\t%4.2f\t%4.2f\t%4.2f\n' % ('O',qq[rr1][0],qq[rr1][1],qq[rr1][2]))
    fc.write('%4.2s\t%4.2f\t%4.2f\t%4.2f\n' % ('H', qq[rr1+1][0], qq[rr1+1][1], qq[rr1+1][2]))
    fc.write('%4.2s\t%4.2f\t%4.2f\t%4.2f\n' % ('H', qq[rr1+2][0], qq[rr1+2][1], qq[rr1+2][2]))

fc.close()

# -----------------------------------------------------------------------------------------------------------

#for the calculation of distance between consecutive pairs
for i in range(0, (3 * n), 3):
    for l in range(3, (3 * n), 3):
        if i == l:
            continue
        elif i > l:
            continue

        else:
            dist0 = (((qq[i][0] - qq[l][0]) ** 2) + ((qq[i][1] - qq[l][1]) ** 2) + ((qq[i][2] - qq[l][2]) ** 2))
            dist1 = np.sqrt(dist0)
            l1.append(i)
            l1.append(l)
            l1.append(dist1)


            #now, making list d of those water molecules which has distance greater than cutoff
            if dist1 > cutoff:
                d.append(qq[i][0])
                d.append(qq[i][1])
                d.append(qq[i][2])
                d.append(qq[i+1][0])
                d.append(qq[i+1][1])
                d.append(qq[i+1][2])
                d.append(qq[i+2][0])
                d.append(qq[i+2][1])
                d.append(qq[i+2][2])
                #for l
                d.append(qq[l][0])
                d.append(qq[l][1])
                d.append(qq[l][2])
                d.append(qq[l + 1][0])
                d.append(qq[l + 1][1])
                d.append(qq[l + 1][2])
                d.append(qq[l + 2][0])
                d.append(qq[l + 2][1])
                d.append(qq[l + 2][2])
            else:
                # now, making list dd of those water molecules which has distance less than cutoff
                dd.append(qq[i][0])
                dd.append(qq[i][1])
                dd.append(qq[i][2])
                dd.append(qq[i + 1][0])
                dd.append(qq[i + 1][1])
                dd.append(qq[i + 1][2])
                dd.append(qq[i + 2][0])
                dd.append(qq[i + 2][1])
                dd.append(qq[i + 2][2])
                # for l
                dd.append(qq[l][0])
                dd.append(qq[l][1])
                dd.append(qq[l][2])
                dd.append(qq[l + 1][0])
                dd.append(qq[l + 1][1])
                dd.append(qq[l + 1][2])
                dd.append(qq[l + 2][0])
                dd.append(qq[l + 2][1])
                dd.append(qq[l + 2][2])


            #list d and dd is 1D and contain repeated water molecules

# -------------------------------------------------------------------------------------------------------------
qqq0=len(dd)#calculating length of the list which contains every molecules including repeated one which has distance < cutoff

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


seen11 = set()
freshh2o11 = []
for item11 in new:
    t111 = tuple(item11)
    if t111 not in seen11:
       freshh2o11.append(item11)
       seen11.add(t111)

# ------------------------------------------------------------------------------


#saving general distance pairs in csv file
po = int(len(l1) // 3)
lo = np.reshape(l1, (po, 3))
fid = ["i", "j", "distance"]
with open("water_dist.csv", "w") as wad:
    w1d = csv.writer(wad)
    w1d.writerow(fid)
    w1d.writerows(lo)

#----------------------------------------------------------------------------------

#printing generated general water molecules in 2d array q without any condition

print("\n General list of generated Water moolecule : \n")
for rows in q:
    print(*rows)

# -----------------------------------------------------------------------------------------

#printing generated general distance pairs in 2d array lo
print("\n i, j ,distance matrix: \n")
lo0 = 0
for rowss in lo:
    lo0 += 1
    print(*rowss)
print("\nNo. of general Distance pairs is : \n", lo0)

# ------------------------------------------------------------------------------------------

# Storing the water molecules in text file with distance cutoff
n10=len(freshh2o11)
f=open('h2o_dist_cutoff.txt','w')
f.write(str(n10)+'\n')
f.write('h2o molecules after cutoff'+'\n')

for r11 in range(0,n10,3):
    f.write('%4.2s\t%4.2f\t%4.2f\t%4.2f\n' % ('O',freshh2o11[r11][0],freshh2o11[r11][1],freshh2o11[r11][2]))
    f.write('%4.2s\t%4.2f\t%4.2f\t%4.2f\n' % ('H', freshh2o11[r11+1][0], freshh2o11[r11+1][1], freshh2o11[r11+1][2]))
    f.write('%4.2s\t%4.2f\t%4.2f\t%4.2f\n' % ('H', freshh2o11[r11+2][0], freshh2o11[r11+2][1], freshh2o11[r11+2][2]))
f.close()

# ----------------------------------------------------------------------------------------------------------

#printing final and corrected list of water molecules with cutoff condition
print("new")
for rs in freshh2o11:
    print(*rs)






