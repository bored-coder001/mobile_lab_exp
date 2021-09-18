from plot_from_excel import excel_plotter as fun
from Rk4_simulation import RungKutta4 
import numpy as np
import matplotlib.pyplot as plt

plot_x = fun('x_axis.xls',1,np.array([24.87822533,1.106050849,3.684197664
]),np.linspace(17.60120584,17.9,1000))

plot_z1= fun('z_axis.xls',1,np.array([2.053143501,-10.242589,-19.11958122]),np.linspace(7.49,8.0,1000))

plot_z2=fun('z_axis.xls',2,np.array([7.679538727,-6.173224449,-20.18884087

]),np.linspace(19.00,19.7,1000))

plot_y = fun('y_axis_correct.xls',1,np.array([-2.630726576,-34.06024933,0.621257782]),np.linspace(1.76,2.48,1000))

#plot_y2 = fun('y_axis_correct.xls',2,np.array([-0.305831373,0.051700756,-0.045432236]),np.linspace([5.50029339,6.7,1000]))



