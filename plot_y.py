from plot_from_excel import excel_plotter as fun
from Rk4_simulation import RungKutta4 
import numpy as np
import matplotlib.pyplot as plt

#the u0-initial value of angular momentum and t-time period of observation of rotation are determined by observation of meta data sheet properly


#for rotation axis on z-axis trial 1
plot_z1= fun('z_axis.xls',1,np.array([2.053143501,-10.242589,-19.11958122]),np.linspace(7.49,8.0,1000))

#for rotation axis on z-axis trial 2
plot_z2=fun('z_axis.xls',2,np.array([7.679538727,-6.173224449,-20.18884087]),np.linspace(19.00,19.7,1000))

#for rotation axis on y-axis 
plot_y2 = fun('y_axis_correct.xls',2,np.array([-0.207851395,-32.14644623,-1.479987144]),np.linspace(5.89,6.71,1000))

plot_y1 = fun('y_axis_correct.xls',1,np.array([-2.630726576,-34.06024933,0.621257782]),np.linspace(1.76,2.48,1000))


#for rotation axis on x-axis
plot_x = fun('x_axis.xls',1,np.array([24.87822533,1.106050849,3.684197664]),np.linspace(17.60120584,17.9,1000))





