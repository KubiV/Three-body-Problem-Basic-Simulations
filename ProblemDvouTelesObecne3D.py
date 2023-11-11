#Jakub Vavra, 5.C, 2020/21
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

dt = 100
t_t = 9000000#2.7*(10**6)
t_0 = 0

x1 = 0
y1 = 0
z1 = 0
vx1 = 0
vy1 = 0
vz1 = 0

x2 = 363000000
y2 = 0
z2 = 0
vx2 = 0
vy2 = 1080
vz2 = 0

#--------------------------------------------#
#--------------------------------------------#

t = t_0
n = (t_t)/dt
n = round(n)

x = x2-x1
y = y2-y1
z = z2-z1

fun1 = k*(m2/(x**2+y**2+z**2)**(3/2))
fun2 = -k*(m1/(x**2+y**2+z**2)**(3/2))

a_ix1 = fun1*x
a_iy1 = fun1*y
a_iz1 = fun1*z
a_ix2 = fun2*x
a_iy2 = fun2*y
a_iz2 = fun1*z

barx = (m1*x1+m2*x2)/(m1+m2)
bary = (m1*y1+m2*y2)/(m1+m2)
barz = (m1*z1+m2*z2)/(m1+m2)
barvx = (m1*vx1+m2*vx2)/(m1+m2)
barvy = (m1*vy1+m2*vy2)/(m1+m2)
barvz = (m1*vz1+m2*vz2)/(m1+m2)

c = np.sqrt(y**2+x**2+z**2)
dr = c-r1-r2
if dr <= 0:
    print("collision")

positionx1 = []
positiony1 = []
positionz1 = []
positionx2 = []
positiony2 = []
positionz2 = []
velocityx1 = []
velocityy1 = []
velocityz1 = []
velocityx2 = []
velocityy2 = []
velocityz2 = []
accelerationx1 = []
accelerationy1 = []
accelerationz1 = []
accelerationx2 = []
accelerationy2 = []
accelerationz2 = []
barycenterx = []
barycentery = []
barycenterz = []
time = []

f = open("ProblemDvouTeles3D.csv", "w", newline="") #"a" to add to file or "w" for rewrite

writer = csv.writer(f)
tup1 = ("Time", "X1", "Y1", "Z1", "X2", "Y2", "Z2")
writer.writerow(tup1)

for interval in range(n):
    
    positionx1.append(x1)
    positiony1.append(y1)
    positionz1.append(z1)
    positionx2.append(x2)
    positiony2.append(y2)
    positionz2.append(z2)
    velocityx1.append(vx1)
    velocityy1.append(vy1)
    velocityz1.append(vz1)
    velocityx2.append(vx2)
    velocityy2.append(vy2)
    velocityz2.append(vz2)
    accelerationx1.append(a_ix1)
    accelerationy1.append(a_iy1)
    accelerationz1.append(a_iz1)
    accelerationx2.append(a_ix2)
    accelerationy2.append(a_iy2)
    accelerationz2.append(a_iz2)
    barycenterx.append(barx)
    barycentery.append(bary)
    barycenterz.append(barz)
    time.append(t)
    
    writer = csv.writer(f)
    tup2 = (t, x1, y1, z1, x2, y2, z2)
    writer.writerow(tup2)

    x1 = x1+vx1*dt+(1/2)*a_ix1*(dt**2)
    y1 = y1+vy1*dt+(1/2)*a_iy1*(dt**2)
    z1 = z1+vz1*dt+(1/2)*a_iz1*(dt**2)
    x2 = x2+vx2*dt+(1/2)*a_ix2*(dt**2)
    y2 = y2+vy2*dt+(1/2)*a_iy2*(dt**2)
    z2 = z2+vz2*dt+(1/2)*a_iz2*(dt**2)
    x = x2-x1
    y = y2-y1
    z = z2-z1
    
    fun1 = k*(m2/(x**2+y**2+z**2)**(3/2))
    fun2 = -k*(m1/(x**2+y**2+z**2)**(3/2))

    ax1 = fun1*x
    ay1 = fun1*y
    az1 = fun1*z
    ax2 = fun2*x
    ay2 = fun2*y
    az2 = fun2*z
    
    vx1 = vx1+(1/2)*(a_ix1+ax1)*dt-barvx
    vy1 = vy1+(1/2)*(a_iy1+ay1)*dt-barvy
    vz1 = vz1+(1/2)*(a_iz1+az1)*dt-barvz
    vx2 = vx2+(1/2)*(a_ix2+ax2)*dt-barvx
    vy2 = vy2+(1/2)*(a_iy2+ay2)*dt-barvy
    vz2 = vz2+(1/2)*(a_iz2+az2)*dt-barvz
    
    a_ix1 = ax1 
    a_iy1 = ay1
    a_iz1 = az1
    a_ix2 = ax2
    a_iy2 = ay2
    a_iz2 = az2

    t = t+dt
    
    barx = (m1*x1+m2*x2)/(m1+m2)
    bary = (m1*y1+m2*y2)/(m1+m2)
    barz = (m1*z1+m2*z2)/(m1+m2)
    barvx = (m1*vx1+m2*vx2)/(m1+m2)
    barvy = (m1*vy1+m2*vy2)/(m1+m2)
    barvz = (m1*vz1+m2*vz2)/(m1+m2)
    
    c = np.sqrt(y**2+x**2+z**2)
    dr = c-r1-r2
    if dr <= 0:
        print("collision at", t, "s")
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
ax = fig.gca( projection='3d', adjustable='box')

ax.plot(positionx1, positiony1, positionz1, color="b", label="První těleso")
ax.plot(positionx2, positiony2, positionz2, color="r", label="Druhé těleso")
ax.plot(barycenterx, barycentery, barycenterz, color="y", label="Těžiště soustavy")
#ax.scatter(positionx1[-1], positiony1[-1], positionz1[-1], color="b", marker="o",s=100)
#ax.scatter(positionx2[-1], positiony2[-1], positionz2[-1], color="r", marker="o",s=100)

plt.title("Problém dvou těles\n dt =%1.0fs, t_t=%1.0fs" %(dt, t_t))
plt.legend(loc="upper left")
ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [m]')

ax.set_box_aspect([1,1,1])
set_axes_equal(ax) 
plt.show()
