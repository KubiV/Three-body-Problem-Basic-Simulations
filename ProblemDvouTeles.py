#Jakub Vavra, 2020/21
import matplotlib.pyplot as plt
import csv
import numpy as np

#--------------------------------------------#
                #VARIABLES
#--------------------------------------------#

k = 6.674*((10)**(-11))

m = 5.972*((10)**(24))
r = 6378000
 
dt = 60
t_t = 550000
n = 200

t_0 = 0
x_0 = 1500000
y_0 = 0
z_0 = 10000000
vx_0 = 200
vy_0 = 6400
vz_0 = 640

#--------------------------------------------#
#--------------------------------------------#

x = x_0
y = y_0
z = z_0
vx = vx_0
vy = vy_0
vz = vz_0
t = t_0

n = (t_t)/dt
n = round(n)

km = k*m

fun = (-km/((x**2+y**2+z**2)**(3/2)))
a_ix = fun*x
a_iy = fun*y
a_iz = fun*z

#--------------------------------------------#

positionx = []
positiony = []
positionz = []
velocityx = []
velocityy = []
velocityz = []
accelerationx = []
accelerationy = []
accelerationz = []
time = []

#--------------------------------------------#
f = open("ProblemDvouTeles.csv", "w", newline="") #"a" to add to file or "w" for rewrite

writer = csv.writer(f)
tup1 = ("Time", "X", "Y", "Z")
writer.writerow(tup1)

for interval in range(n):
    
    positionx.append(x)
    positiony.append(y)
    positionz.append(z)
    velocityx.append(vx)
    velocityy.append(vy)
    velocityz.append(vz)
    accelerationx.append(a_ix)
    accelerationy.append(a_iy)
    accelerationz.append(a_iz)
    time.append(t)
    
    writer = csv.writer(f)
    tup2 = (t, x, y, z)
    writer.writerow(tup2)
    
    x = x+vx*dt+(1/2)*a_ix*(dt**2)
    y = y+vy*dt+(1/2)*a_iy*(dt**2)
    z = z+vz*dt+(1/2)*a_iz*(dt**2)
    fun = (-km/((x**2+y**2+z**2)**(3/2)))
    ax = fun*x
    ay = fun*y
    az = fun*z
    vx = vx+(1/2)*(a_ix+ax)*dt
    vy = vy+(1/2)*(a_iy+ay)*dt
    vz = vz+(1/2)*(a_iz+az)*dt
    
    a_ix = ax
    a_iy = ay
    a_iz = az
    
    t = t+dt
    
f.close()

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

_u,_v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
_x = r*np.cos(_u)*np.sin(_v)
_y = r*np.sin(_u)*np.sin(_v)
_z = r*np.cos(_v)
ax.plot_surface(_x, _y, _z, cmap="Blues")

#--------------------------------------------#
    
ax.plot(positionx, positiony, positionz, color="b")
ax.scatter(positionx[-1], positiony[-1], positionz[-1], color="b", marker="o",s=100)

ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')
ax.set_zlabel('Z [m]')

ax.set_box_aspect([1,1,1])
set_axes_equal(ax) 
plt.show()
