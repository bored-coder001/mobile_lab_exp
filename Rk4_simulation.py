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

    #return the increment of value with each step as an array     
    return u

#formulating equations of rigid body in free rotation

def D(u,t1):
    
    #C1,C2,C3 are Constants here cause we analytically calculated the Inertia so we just declare here
    C1 =-0.994379
    C2 =0.974025
    C3 =0.64741
    return np.array([C1*u[1]*u[2], C2*u[2]*u[0], C3*u[1]*u[0]])
#as it is non iterable as an array to be processed in Rungekutta from output we have to copy it to the plot function for RK function to directly operate

#function to calculate the Energy
def energy(u):
    
    #inertia value analytically calculated for POCO M2 PRO
    I1=479.838
    I2=103.755
    I3=580.896
    #the u is here the result obtained from RK4 define it as a 1D array
    E = np.array([0.5*(I1*u[:,0]**2+I2*u[:,1]**2+I3*u[:,2]**2)])
    return E

#function to calculate Angular momentum
def ang_momentum(u):
    #inertia value analytically calculated for POCO M2 PRO
    I1=479.838
    I2=103.755
    I3=580.896

    L= np.array([np.sqrt((I1*u[:,0])**2+(I2*u[:,1])**2+(I3*u[:,2])**2)])

    return L


