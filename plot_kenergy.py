from plot_from_excel import excel_plotter2 as fun2
import numpy as np

#the u0-initial value of angular momentum and t-time period of observation of rotation are determined by observation of meta data sheet properly

#for rotation along z-axis
plot_z = fun2('z_axis.xls',3,np.array([2.053143501,-10.242589,-19.11958122]),np.linspace(7.49,8.0,1000))
#for rotation along y-axis
plot_y = fun2('y_axis_correct.xls',3,np.array([-2.630726576,-34.06024933,0.621257782]),np.linspace(1.76,2.48,1000))
#for rotation along x-axis
plot_x = fun2('x_axis.xls',2,np.array([24.87822533,1.106050849,3.684197664]),np.linspace(17.60120584,17.9,1000))
