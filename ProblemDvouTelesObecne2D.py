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

dt = 100
t_t = 9000000#2.7*(10**6)
t_0 = 0

x1 = 0
y1 = 0
vx1 = 0
vy1 = 0

x2 = 363000000
y2 = 0
vx2 = 0
vy2 = 1080

#--------------------------------------------#
#--------------------------------------------#

t = t_0
n = (t_t)/dt
n = round(n)

x = x2-x1
y = y2-y1

fun1 = k*(m2/(x**2+y**2)**(3/2))
fun2 = -k*(m1/(x**2+y**2)**(3/2))

a_ix1 = fun1*x
a_iy1 = fun1*y
a_ix2 = fun2*x
a_iy2 = fun2*y

c = np.sqrt(y**2+x**2)
dr = c-r1-r2
if dr <= 0:
    print("collision")

barx = (m1*x1+m2*x2)/(m1+m2)
bary = (m1*y1+m2*y2)/(m1+m2)
barvx = (m1*vx1+m2*vx2)/(m1+m2)
barvy = (m1*vy1+m2*vy2)/(m1+m2)

positionx1 = []
positiony1 = []
positionx2 = []
positiony2 = []
barycenterx = []
barycentery = []

f = open("ProblemDvouTeles2D.csv", "w", newline="") #"a" to add to file or "w" for rewrite

writer = csv.writer(f)
tup1 = ("Time", "X1", "Y1", "X2", "Y2", "Xbar", "Ybar")
writer.writerow(tup1)

for interval in range(n):
    
    positionx1.append(x1)
    positiony1.append(y1)
    positionx2.append(x2)
    positiony2.append(y2)
    barycenterx.append(barx)
    barycentery.append(bary)
    
    writer = csv.writer(f)
    tup2 = (t, x1, y1, x2, y2, barx, bary)
    writer.writerow(tup2)

    x1 = x1+vx1*dt+(1/2)*a_ix1*(dt**2)
    y1 = y1+vy1*dt+(1/2)*a_iy1*(dt**2)
    x2 = x2+vx2*dt+(1/2)*a_ix2*(dt**2)
    y2 = y2+vy2*dt+(1/2)*a_iy2*(dt**2)
    x = x2-x1
    y = y2-y1
    
    fun1 = k*(m2/(x**2+y**2)**(3/2))
    fun2 = -k*(m1/(x**2+y**2)**(3/2))

    ax1 = fun1*x
    ay1 = fun1*y
    ax2 = fun2*x
    ay2 = fun2*y
    
    vx1 = vx1+(1/2)*(a_ix1+ax1)*dt-barvx
    vy1 = vy1+(1/2)*(a_iy1+ay1)*dt-barvy
    vx2 = vx2+(1/2)*(a_ix2+ax2)*dt-barvx
    vy2 = vy2+(1/2)*(a_iy2+ay2)*dt-barvy
    
    a_ix1 = ax1 
    a_iy1 = ay1
    a_ix2 = ax2
    a_iy2 = ay2
    
    t = t+dt
    
    barx = (m1*x1+m2*x2)/(m1+m2)
    bary = (m1*y1+m2*y2)/(m1+m2)
    barvx = (m1*vx1+m2*vx2)/(m1+m2)
    barvy = (m1*vy1+m2*vy2)/(m1+m2)
    
    c = np.sqrt(y**2+x**2)
    dr = c-r1-r2
    if dr <= 0:
        print("collision at", t, "s")
        break
        
#--------------------------------------------#

plt.scatter(positionx1, positiony1, color="b", marker="o", label="První těleso")
plt.scatter(positionx2, positiony2, color="r", marker="o", label="Druhé těleso")
plt.plot(barycenterx, barycentery, color="y", label="Těžiště soustavy")

plt.title("Problém dvou těles\n dt =%1.0fs, t_t=%1.0fs" %(dt, t_t))
plt.legend(loc="upper left")
plt.xlabel('X [m]')
plt.ylabel('Y [m]')

plt.axis("equal")
plt.show()