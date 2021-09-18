import numpy as np
import matplotlib.pyplot as plt


#use the library form 5th sem computational course
def RungKutta4(f,u0,t):

    nt = len(t)

    nu = len(u0)
    u = np.zeros((nt,nu))

    u[0] = u0

    for k in range(nt-1):
        dt = t[k+1] - t[k]

        k1 = dt*f(u[k], t[k])
        k2 = dt*f(u[k]+k1/2, t[k]+dt/2)
        k3 = dt*f(u[k]+k2/2,t[k]+dt/2)
        k4 = dt*f( u[k]+k3,t[k]+dt)

        du = (k1 + 2*k2 + 2*k3 +k4)/6

        u[k+1] =u[k]+du 


    return u
'''
#Let d\omega/dt = D(u,t) where \omega= x,y,z =u = u[0],u[1],u[2]
def D(u,t):
	
	#C1,C2,C3 are Constants here cause we analytically calculated the Inertia so we just declare here
    C1 =-0.994379
    C2 =0.974025
    C3 =0.64741
    return np.array([C1*u[1]*u[2], C2*u[2]*u[0], C3*u[1]*u[0]])

#initial Conditions
t1 = np.linspace(0,0.4,1000)
u0 = np.array([24,1,3])

out = RungKutta4(D,u0,t1)
plt.plot(t1,out[:,0],'b')
plt.plot(t1,out[:,1],'g')
plt.plot(t1,out[:,2],'r')
plt.show()
'''


'''
def pend(y, t):
    b= 1
    c=2
    return np.array([y[1], -b*y[1] - c*np.sin(y[0])])

t5 = np.linspace(0,10,1000)

y0 = np.array([np.pi-0.1,0.0])
out2 = RungKutta4(pend,y0,t5)

plt.plot(t5,out2[:,0])
plt.show()
'''