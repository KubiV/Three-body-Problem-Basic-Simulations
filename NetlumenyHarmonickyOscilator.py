#Jakub Vavra, 2020/21
import matplotlib.pyplot as plt
import csv
import numpy as np

#------------------VARIABLES------------------#

m = 1
k = 1
dt = 0.01
x = 1
t_t = 9.5

#--------------------------------------------#
#--------------------------------------------#
t = 0

n = t_t/dt
n = round(n)

fun = (-k)/m
a_i = fun*x

x_i = x
v = 0
f_0 = 0

x_2 = x

position = []
position2 = []
velocity = []
acceleration = []
time = []

#--------------------------------------------#

f = open("NetlumenyHarmonickyOscilator.csv", "w", newline="") #"a" to add to file or "w" for rewrite

for interval in range(n):
    
    position.append(x)
    position2.append(x_2)
    velocity.append(v)
    acceleration.append(a_i)
    time.append(t)
    
    x = x+v*dt+(1/2)*a_i*(dt**2)
    a = fun*x
    v = v+(1/2)*(a_i+a)*dt
    
    a_i = a
    t = t+dt
    
    x_2 = x_i*np.cos(np.sqrt(abs(k)/m)*t+f_0)
    
    tup1 = (t, x, x_2)
    writer = csv.writer(f)
    writer.writerow(tup1)
    
f.close()

#--------------------------------------------#

xax = np.random.randint(low=0, high=50, size=int(t_t))
yax = np.random.randint(low=0, high=50, size=int(x))

plt.plot(time, position, "bo", markersize=5)
plt.plot(time, position2, "r")
#plt.plot(time, velocity, "g")
#plt.plot(time, acceleration, "b")

plt.title("Netlumený harmonický oscilátor, m =%1.2f, k =%1.2f, dt =%1.3f" %(m, k, dt) )
plt.xlabel("Čas [s]")
plt.ylabel("pozice")
plt.legend(["Numerické řešení", "Analytické řešení", "Rychlost z num.", "Zrychlení z num."])

plt.grid(which='major', color='#666666', linestyle='-')
#plt.xticks(np.arange(0, len(xax)+1, 1))
#plt.yticks(np.arange(0, max(yax), 1)
#plt.axis('equal')

plt.show()