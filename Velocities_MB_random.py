import numpy as np
import matplotlib.pyplot as plt
import math

n_p=int(input("Enter the number of molecules/atoms = "))
n=n_p

# Storing random net velocities, assigned to particles in list v
v=[]

# Storing x,y,z random velocities component in text file for each atom/molecule
f=open('velocities_MB.txt','w')
f.write(str(n)+'\n')
f.write('vx,vy,vz'+'\n')
for i in range(0,n):
    vx=(np.random.randn())
    vy = (np.random.randn())
    vz = (np.random.randn())
    f.write('%4.2f\t%4.2f\t%4.2f\n' % (vx,vy,vz))
    vn=math.sqrt(vx**2+vy**2+vz**2)
    v.append(vn)

#     Sorting list v from lower to higher velocities
v.sort()

# Mapping random velocities to the MB distribution
g=[]
n0=[]
for j in range(0,n):
    s=(math.exp(-v[j]**2))*v[j]*v[j]*(4/n_p*np.sqrt(3.142))
    g.append(s)
    N=n_p*s
    n0.append(N)

total=sum(n0)

print("The Estimated total number of particles from plot", total)




# plotting
plt.title("MB Velocity Distribution")
plt.xlabel("Velocity")
plt.ylabel("f(v)")
plt.plot(v, g, color ="green")
plt.show()
