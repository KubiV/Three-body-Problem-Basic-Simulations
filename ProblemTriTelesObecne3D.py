#Jakub Vavra, 2020/21
import matplotlib.pyplot as plt
import csv
import numpy as np
    
#--------------------------------------------#
                #VARIABLES
#--------------------------------------------#

k = 6.674*(10**(-11))

m1 = 5.972*(10**24)
r1 = 6378000
m2 = 7.348*(10**22)
r2 = 1737000
m3 = 15000
r3 = 1.95

dt = 90
t_t = 1000000#2.7*(10**6)
t_0 = 0

x1 = 0
y1 = 0
z1 = 0
vx1 = 0
vy1 = 0
vz1 = 0

x2 = 0#363000000
y2 = -363000000
z2 = 0
vx2 = 1080
vy2 = 0#1080
vz2 = 0

x3 = -6555000#-6700000
y3 = 0
z3 = 0
vx3 = 0
vy3 = 10930#-9000
vz3 = 0

#--------------------------------------------#
#--------------------------------------------#

t = t_0
n = (t_t)/dt
n = round(n)

#--------------------------------------------#

def calc_ax(mj, xi, yi, zi, xj, yj, zj):
    x = xi-xj
    y = yi-yj
    z = zi-zj
    t = -k*(mj/(x**2+y**2+z**2)**(3/2))
    a = t*x
    return a

def calc_ay(mj, xi, yi, zi, xj, yj, zj):
    x = xi-xj
    y = yi-yj
    z = zi-zj
    t = -k*(mj/(x**2+y**2+z**2)**(3/2))
    a = t*y
    return a

def calc_az(mj, xi, yi, zi, xj, yj, zj):
    x = xi-xj
    y = yi-yj
    z = zi-zj
    t = -k*(mj/(x**2+y**2+z**2)**(3/2))
    a = t*z
    return a

def collis(xi, yi, zi, xj, yj, zj, ri, rj):
    x = xj-xi
    y = yj-yi
    z = zj-zi
    c = (y**2+x**2+z**2)**(1/2)
    dr = c-ri-rj
    if dr <= 0:
        print("collision (", ri,") with (", rj, ") at ", t, "s")
        return True

#--------------------------------------------#

a_ix1 = calc_ax(m2, x1, y1, z1, x2, y2, z2)+calc_ax(m3, x1, y1, z1, x3, y3, z3)
a_iy1 = calc_ay(m2, x1, y1, z1, x2, y2, z2)+calc_ay(m3, x1, y1, z1, x3, y3, z3)
a_iz1 = calc_az(m2, x1, y1, z1, x2, y2, z2)+calc_az(m3, x1, y1, z1, x3, y3, z3)
a_ix2 = calc_ax(m3, x2, y2, z2, x3, y3, z3)+calc_ax(m1, x2, y2, z2, x1, y1, z1)
a_iy2 = calc_ay(m3, x2, y2, z2, x3, y3, z3)+calc_ay(m1, x2, y2, z2, x1, y1, z1)
a_iz2 = calc_az(m3, x2, y2, z2, x3, y3, z3)+calc_az(m1, x2, y2, z2, x1, y1, z1)
a_ix3 = calc_ax(m1, x3, y3, z3, x1, y1, z1)+calc_ax(m2, x3, y3, z3, x2, y2, z2)
a_iy3 = calc_ay(m1, x3, y3, z3, x1, y1, z1)+calc_ay(m2, x3, y3, z3, x2, y2, z2)
a_iz3 = calc_az(m1, x3, y3, z3, x1, y1, z1)+calc_az(m2, x3, y3, z3, x2, y2, z2)

collis(x1, y1, z1, x2, y2, z2, r1, r2)
collis(x1, y1, z1, x3, y3, z3, r1, r3)
collis(x2, y2, z2, x3, y3, z3, r2, r3)

positionx1 = []
positiony1 = []
positionz1 = []
positionx2 = []
positiony2 = []
positionz2 = []
positionx3 = []
positiony3 = []
positionz3 = []

f = open("ProblemTriTeles3D.csv", "w", newline="") #"a" to add to file or "w" for rewrite

writer = csv.writer(f)
tup1 = ("Time", "X1", "Y1", "Z1", "X2", "Y2", "Z2", "X3", "Y3", "Z3")
writer.writerow(tup1)

for interval in range(n):
    
    positionx1.append(x1)
    positiony1.append(y1)
    positionz1.append(z1)
    positionx2.append(x2)
    positiony2.append(y2)
    positionz2.append(z2)
    positionx3.append(x3)
    positiony3.append(y3)
    positionz3.append(z3)
    
    writer = csv.writer(f)
    tup2 = (t, x1, y1, z1, x2, y2, z2, x3, y3, z3)
    writer.writerow(tup2)

    x1 = x1+vx1*dt+(1/2)*a_ix1*(dt**2)
    y1 = y1+vy1*dt+(1/2)*a_iy1*(dt**2)
    z1 = z1+vz1*dt+(1/2)*a_iz1*(dt**2)
    x2 = x2+vx2*dt+(1/2)*a_ix2*(dt**2)
    y2 = y2+vy2*dt+(1/2)*a_iy2*(dt**2)
    z2 = z2+vz2*dt+(1/2)*a_iz2*(dt**2)
    x3 = x3+vx3*dt+(1/2)*a_ix3*(dt**2)
    y3 = y3+vy3*dt+(1/2)*a_iy3*(dt**2)
    z3 = z3+vz3*dt+(1/2)*a_iz3*(dt**2)

    ax1 = calc_ax(m2, x1, y1, z1, x2, y2, z2)+calc_ax(m3, x1, y1, z1, x3, y3, z3)
    ay1 = calc_ay(m2, x1, y1, z1, x2, y2, z2)+calc_ay(m3, x1, y1, z1, x3, y3, z3)
    az1 = calc_az(m2, x1, y1, z1, x2, y2, z2)+calc_az(m3, x1, y1, z1, x3, y3, z3)
    ax2 = calc_ax(m3, x2, y2, z2, x3, y3, z3)+calc_ax(m1, x2, y2, z2, x1, y1, z1)
    ay2 = calc_ay(m3, x2, y2, z2, x3, y3, z3)+calc_ay(m1, x2, y2, z2, x1, y1, z1)
    az2 = calc_az(m3, x2, y2, z2, x3, y3, z3)+calc_az(m1, x2, y2, z2, x1, y1, z1)
    ax3 = calc_ax(m1, x3, y3, z3, x1, y1, z1)+calc_ax(m2, x3, y3, z3, x2, y2, z2)
    ay3 = calc_ay(m1, x3, y3, z3, x1, y1, z1)+calc_ay(m2, x3, y3, z3, x2, y2, z2)
    az3 = calc_az(m1, x3, y3, z3, x1, y1, z1)+calc_az(m2, x3, y3, z3, x2, y2, z2)
    
    vx1 = vx1+(1/2)*(a_ix1+ax1)*dt
    vy1 = vy1+(1/2)*(a_iy1+ay1)*dt
    vz1 = vz1+(1/2)*(a_iz1+az1)*dt
    vx2 = vx2+(1/2)*(a_ix2+ax2)*dt
    vy2 = vy2+(1/2)*(a_iy2+ay2)*dt
    vz2 = vz2+(1/2)*(a_iz2+az2)*dt
    vx3 = vx3+(1/2)*(a_ix3+ax3)*dt
    vy3 = vy3+(1/2)*(a_iy3+ay3)*dt
    vz3 = vz3+(1/2)*(a_iz3+az3)*dt
    
    a_ix1 = ax1 
    a_iy1 = ay1
    a_iz1 = az1
    a_ix2 = ax2
    a_iy2 = ay2
    a_iz2 = az2
    a_ix3 = ax3
    a_iy3 = ay3
    a_iz3 = az3
    
    t = t+dt
    
    col12 = collis(x1, y1, z1, x2, y2, z2, r1, r2)
    col13 = collis(x1, y1, z1, x3, y3, z3, r1, r3)
    col23 = collis(x2, y2, z2, x3, y3, z3, r2, r3)
    
    if col12 or col13 or col23 == True:   
        break
    
#--------------------------------------------#
#https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to
def set_axes_equal(ax: plt.Axes):
    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])
    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    _set_axes_radius(ax, origin, radius)
    
def _set_axes_radius(ax, origin, radius):
    x, y, z = origin
    ax.set_xlim3d([x - radius, x + radius])
    ax.set_ylim3d([y - radius, y + radius])
    ax.set_zlim3d([z - radius, z + radius])
#--------------------------------------------#
fig = plt.figure()
#ax = fig.gca( projection='3d', adjustable='box')
ax = fig.add_subplot(111, projection='3d')

plt.plot(positionx1, positiony1, positionz1, color="b", marker="o", label="První těleso")
plt.plot(positionx2, positiony2, positionz2, color="r", marker="o", label="Druhé těleso")
plt.plot(positionx3, positiony3, positionz3, color="g", marker="o", label="Třetí těleso")
ax.scatter(positionx1[-1], positiony1[-1], positionz1[-1], color="b", marker="o",s=100)
ax.scatter(positionx2[-1], positiony2[-1], positionz2[-1], color="r", marker="o",s=100)
ax.scatter(positionx3[-1], positiony3[-1], positionz3[-1], color="g", marker="o",s=100)

plt.title("Problém tří těles\n dt =%1.0fs, t_t=%1.0fs" %(dt, t_t))
plt.legend(loc="upper left")
ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [m]')

ax.set_box_aspect([1,1,1])
set_axes_equal(ax) 
plt.show()
