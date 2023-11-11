#Jakub Vavra, 2020/21
import matplotlib.pyplot as plt
import csv
import numpy as np

#------------------VARIABLES------------------#

k = 0.171 
N = 1000
dt = 0.01
t_t = 15

#--------------------------------------------#
#--------------------------------------------#
t = 0

n = (t_t+dt)/dt
n = round(n)

number = []
time = []

#--------------------------------------------#

t_2 = np.linspace(0,t_t,n*100)
N_2 = N*np.exp((-k)*t_2)

#--------------------------------------------#

f = open("JadernyRozpad.csv", "w", newline="") #"a" to add to file or "w" for rewrite

for interval in range(n):
    
    number.append(N)
    time.append(t)
    
    tup1 = (t, N)
    writer = csv.writer(f)
    writer.writerow(tup1)

    derN = N*(-k) #derN stands for derivative of N, or more precisely an aproximation of derN
    N = N+dt*derN #new N out of previous N and time step with derN
    t = t+dt #new time value
    
f.close()
    
#--------------------------------------------#
    
plt.plot(time, number, "bo", markersize=2.5)
plt.plot(t_2,N_2, "r")

#plt.yscale("log")

plt.title("Jaderný rozpad, k =%1.2f, dt =%1.3f" %(k, dt) )
plt.xlabel("čas [s]")
plt.ylabel("počet")
plt.legend(["Numerické řešení", "Analytické řešení­"])

plt.show()