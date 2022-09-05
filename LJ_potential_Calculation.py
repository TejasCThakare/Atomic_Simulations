import numpy as np
import matplotlib.pyplot as plt

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
l3=[]
lj1=[]
lj2=[]
lj3=[]
ljj3=[]

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
            xr=p1[i][0] - p1[l][0]
            yr=p1[i][1] - p1[l][1]
            zr=p1[i][2] - p1[l][2]

            dist1 = np.sqrt(((xr) ** 2) + ((yr) ** 2) + ((zr) ** 2))
            l1.append(dist1)

            dist_pbc = np.sqrt(((xr- 8 * round(xr / 8)) ** 2)+((yr - 8 * round(yr / 8)) ** 2)+((zr - 4 * round(xr / 4)) ** 2))
            l2.append(dist_pbc)


# LJ without PBC
l1.sort()
s=len(l1)
for i in range(0,s):
    a1 = (l1[i])**6
    a2=a1**2
    lja=((1/a2)-(1/a1))*4
    lj1.append(lja)

# LJ with PBC
l2.sort()
s1=len(l2)
for j in range(0,s1):
    b1 =(l2[j])**6
    b2=b1**2
    ljb=((1/b2)-(1/b1))*4
    lj2.append(ljb)


# LJ with PBC with cutoof
l2.sort()
s2=len(l2)
ljct = ((1 / (cutoff**12)) - (1 / (cutoff**6))) * 4
for k in range(0,s2):
    if l2[k]<cutoff:
        l3.append(l2[k])
        c1 = (l3[k]) ** 6
        c2 = c1 ** 2
        ljc = (((1 / c2) - (1 / c1)) * 4)
        ljjc = (((1 / c2) - (1 / c1)) * 4)-ljct
        lj3.append(ljc)
        ljj3.append(ljjc)

# Plot for lj w/o pbc
plt.title("U(r) Vs r w/o PBC")
plt.xlabel("r")
plt.ylabel("U(r)")
plt.xlim(0.7, 5.0)
plt.ylim(-1.5, 5.0)
plt.plot(l1, lj1, color="green")
plt.show()


# Plot for lj w pbc
plt.title("U(r) Vs r with PBC")
plt.xlabel("r")
plt.ylabel("U(r)")
plt.xlim(0.7, 5.0)
plt.ylim(-1.5, 5.0)
plt.plot(l2, lj2, color="green")
plt.show()

# Plot for lj w pbc with cutoff
plt.title("U(r) Vs r with PBC and cutoff")
plt.xlabel("r")
plt.ylabel("U(r)")
plt.xlim(0.7, 5.0)
plt.ylim(-1.5, 5.0)
plt.plot(l3, lj3, color="green",label="LJ")
plt.plot(l3, ljj3, color="red",label="LJ+U(cutoff)")
plt.legend()
plt.show()

# Calculating surface energy
sumLJ=sum(lj1)
sumLJpbc=sum(lj2)
se=sumLJpbc-sumLJ
print("surface energy",se)
