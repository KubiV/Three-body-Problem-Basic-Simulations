#Jakub Vavra, 2020/21
import matplotlib.pyplot as plt
import numpy as np

#------------------VARIABLES------------------#

g =  9.8
t_t = 5
xmin = 0

dt = 0.1

c = 10 # initial velocity
d = 0 # initial position

#--------------------------------------------#
#--------------------------------------------#
n = (t_t/dt)
n = round(n)

t = np.linspace(0,t_t)

y = -(1/2)*g*(t**2)+c*t+d
v = (-g)*t+c

velnum = []
posnum = []
timenum = []
vnum = c 
ynum = d
tnum = xmin

for interval in range(n):
    
    velnum.append(vnum)
    posnum.append(ynum)
    timenum.append(tnum)
    vnum = vnum + (-g)*dt
    ynum = ynum + vnum*dt
    tnum = tnum + dt
    
a = -g

plt.plot(t, y, "b")
plt.plot(t, v, "r")
plt.plot(timenum, posnum, "bo", markersize=2.5)
plt.plot(timenum, velnum, "ro", markersize=2.5)
plt.hlines(a, xmin, t_t, color="g")

plt.title("g=%1.2f, c=%1.2f, d=%1.2f, dt=%1.3f \n" %(g, c, d, dt) )
plt.xlabel("čas [s]")
plt.ylabel("výška [m]")
plt.legend(["y", "v", "y num", "v num", "a"])

#plt.axis("equal")
plt.show()