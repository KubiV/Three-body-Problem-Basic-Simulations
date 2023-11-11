#Jakub Vavra, 2020/21
import matplotlib.pyplot as plt
import csv
    
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

dt = 1
t_t = 1000000#2.7*(10**6)
t_0 = 0

x1 = 0
y1 = 0
vx1 = 0
vy1 = 0

x2 = 0
y2 = -363000000
vx2 = 1080
vy2 = 0

x3 = -6555000#3760000 366887000
y3 = 0#5370000
vx3 = 0#-100 -8900
vy3 = 10930#10920 6200 2598

#--------------------------------------------#
#--------------------------------------------#

t = t_0
n = (t_t)/dt
n = round(n)

#--------------------------------------------#

def calc_ax(mj, xi, yi, xj, yj):
    x = xi-xj
    y = yi-yj
    t = -k*(mj/(x**2+y**2)**(3/2))
    a = t*x
    return a

def calc_ay(mj, xi, yi, xj, yj):
    x = xi-xj
    y = yi-yj
    t = -k*(mj/(x**2+y**2)**(3/2))
    a = t*y
    return a

def collis(xi, yi, xj, yj, ri, rj):
    x = xj-xi
    y = yj-yi
    c = (y**2+x**2)**(1/2)
    dr = c-ri-rj
    if dr <= 0:
        print("collision (", ri,") with (", rj, ") at ", t, "s")
        return True

#--------------------------------------------#

a_ix1 = calc_ax(m2, x1, y1, x2, y2)+calc_ax(m3, x1, y1, x3, y3)
a_iy1 = calc_ay(m2, x1, y1, x2, y2)+calc_ay(m3, x1, y1, x3, y3)
a_ix2 = calc_ax(m3, x2, y2, x3, y3)+calc_ax(m1, x2, y2, x1, y1)
a_iy2 = calc_ay(m3, x2, y2, x3, y3)+calc_ay(m1, x2, y2, x1, y1)
a_ix3 = calc_ax(m1, x3, y3, x1, y1)+calc_ax(m2, x3, y3, x2, y2)
a_iy3 = calc_ay(m1, x3, y3, x1, y1)+calc_ay(m2, x3, y3, x2, y2)

collis(x1, y1, x2, y2, r1, r2)
collis(x1, y1, x3, y3, r1, r3)
collis(x2, y2, x3, y3, r2, r3)

positionx1 = []
positiony1 = []
positionx2 = []
positiony2 = []
positionx3 = []
positiony3 = []

#velocity3 = []
#time = []

f = open("ProblemTriTeles2D.csv", "w", newline="") #"a" to add to file or "w" for rewrite

writer = csv.writer(f)
tup1 = ("Time", "X1", "Y1", "X2", "Y2", "X3", "Y3")
writer.writerow(tup1)

for interval in range(n):
    
    positionx1.append(x1)
    positiony1.append(y1)
    positionx2.append(x2)
    positiony2.append(y2)
    positionx3.append(x3)
    positiony3.append(y3)
    
    #v3 = ((vx3**2)+(vy3**2))**(1/2)
    #velocity3.append(v3)
    #time.append(t)
    
    writer = csv.writer(f)
    tup2 = (t, x1, y1, x2, y2, x3, y3)
    writer.writerow(tup2)

    x1 = x1+vx1*dt+(1/2)*a_ix1*(dt**2)
    y1 = y1+vy1*dt+(1/2)*a_iy1*(dt**2)
    x2 = x2+vx2*dt+(1/2)*a_ix2*(dt**2)
    y2 = y2+vy2*dt+(1/2)*a_iy2*(dt**2)
    x3 = x3+vx3*dt+(1/2)*a_ix3*(dt**2)
    y3 = y3+vy3*dt+(1/2)*a_iy3*(dt**2)

    ax1 = calc_ax(m2, x1, y1, x2, y2)+calc_ax(m3, x1, y1, x3, y3)
    ay1 = calc_ay(m2, x1, y1, x2, y2)+calc_ay(m3, x1, y1, x3, y3)
    ax2 = calc_ax(m3, x2, y2, x3, y3)+calc_ax(m1, x2, y2, x1, y1)
    ay2 = calc_ay(m3, x2, y2, x3, y3)+calc_ay(m1, x2, y2, x1, y1)
    ax3 = calc_ax(m1, x3, y3, x1, y1)+calc_ax(m2, x3, y3, x2, y2)
    ay3 = calc_ay(m1, x3, y3, x1, y1)+calc_ay(m2, x3, y3, x2, y2)
    
    vx1 = vx1+(1/2)*(a_ix1+ax1)*dt
    vy1 = vy1+(1/2)*(a_iy1+ay1)*dt
    vx2 = vx2+(1/2)*(a_ix2+ax2)*dt
    vy2 = vy2+(1/2)*(a_iy2+ay2)*dt
    vx3 = vx3+(1/2)*(a_ix3+ax3)*dt
    vy3 = vy3+(1/2)*(a_iy3+ay3)*dt
    
    a_ix1 = ax1 
    a_iy1 = ay1
    a_ix2 = ax2
    a_iy2 = ay2
    a_ix3 = ax3
    a_iy3 = ay3
    
    t = t+dt
    
    col12 = collis(x1, y1, x2, y2, r1, r2)
    col13 = collis(x1, y1, x3, y3, r1, r3)
    col23 = collis(x2, y2, x3, y3, r2, r3)
    
    if col12 or col13 or col23 == True:   
        break
    
#--------------------------------------------#

plt.plot(positionx1, positiony1, color="b", marker="o", markersize=12, label="První těleso")
plt.plot(positionx2, positiony2, color="r", marker="o", markersize=12, label="Druhé těleso")
plt.plot(positionx3, positiony3, color="g", marker="o", markersize=12, label="Třetí těleso")

plt.title("Problém tří těles\n dt =%1.0fs, t_t=%1.0fs" %(dt, t_t))
plt.legend(loc="lower right")
plt.xlabel('X [m]')
plt.ylabel('Y [m]')

#plt.plot(time, velocity3, color="g", label="Rychlost třetího tělesa")
#plt.xlabel('Čas [s]')
#plt.ylabel('Rychlost [m/s]')

plt.axis("equal")
plt.show()

