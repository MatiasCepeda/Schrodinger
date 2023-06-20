import numpy as np
import matplotlib.pyplot as plt

dx = 0.01 #Espaciado
x = np.arange(0, 3.5+dx, dx) #Eje x>=0
x_n = np.arange(0, 3.5+dx, dx) #Eje x<0

x_n = np.multiply(x_n,-1)
x_n = np.delete(x_n,0)
x_n = np.flip(x_n)
x_n = np.append(x_n,x) #Eje x

psi = np.zeros((len(x_n))) #funcion de onda
psi_min = np.zeros((len(x_n))) #funcion de onda para E_min

#Definimos nuestas condiciones iniciales

psi[0] = 0 #psi(0) es psi(a) donde a será el borde 
psi[1] = 0.00001
psi_min[0]=0
psi_min[1]=0.00001

m=1
hbar=1
w=1
alpha=0.01

E_min = 0 #autoenergia
E_max = 5
E = 0.3
max_pasos = 50
tolerancia = 0.0001
s = 0 #contador
n = 4 #Energia n
flag='R'

while s<max_pasos and flag=='R':
    E = 0.5*(E_min+E_max)
    n_count=0 #Contador de nodos
    for i in range(1,len(x_n)-2):
        psi[i+1] = 2*((m*dx**2)/(hbar**2)*(0.5*x_n[i]**2+0.5*alpha*x_n[i]**4-E)+1)*psi[i] - psi[i-1]
        if psi[i+1]*psi[i]<0:
            n_count+=1
    # print('iteracion',s,'=',n_count)
    for i in range(1,len(x_n)-2):
        psi_min[i+1] = 2*((m*dx**2)/(hbar**2)*(0.5*x_n[i]**2+0.5*alpha*x_n[i]**4-E_min)+1)*psi[i] - psi[i-1]
    if n_count<n:
        E_min=E
    elif n_count>n:
        E_max=E
    s+=1
    if n==n_count:
        if psi[len(x_n)-2]*psi_min[len(x_n)-2]>0:
            E_min=E
        elif psi[len(x_n)-1]*psi_min[len(x_n)-1]<0:
            E_max=E
        if np.abs(E_max-E_min)<=tolerancia:
            flag='G'
print('Auto energia E'+str(n),'=',E)

plt.figure()
plt.plot(x_n,psi_min,'b',x_n,psi,'r')
plt.grid()
plt.show()
