from plot_from_excel import excel_plotter2 as fun2
import numpy as np

#the u0-initial value of angular momentum and t-time period of observation of rotation are determined by observation of meta data sheet properly

#for rotation along z-axis
plot_z = fun2('z_axis.xls',3,np.array([2.053143501,-10.242589,-19.11958122]),np.linspace(7.49,8.05,1000))
#for rotation along y-axis
plot_y = fun2('y_axis_correct.xls',3,np.array([-2.630726576,-34.06024933,0.621257782]),np.linspace(1.76,2.48,1000))
#for rotation along x-axis
plot_x = fun2('x_axis.xls',2,np.array([24.87822533,1.106050849,3.684197664]),np.linspace(17.60120584,17.9,1000))


'''
OUTPUT for error analyis and comparision:

Theoretical Avg. of L for z_axis.xls = 11200.632203696745
Theoretical Avg of K for z_axis.xls= 112629.6322522342
Theoretical Avg. of L for y_axis_correct.xls = 3769.9187593535694
Theoretical Avg of K for y_axis_correct.xls= 61955.62779785188
Theoretical Avg. of L for x_axis.xls = 12128.361098916259
Theoretical Avg of K for x_axis.xls= 152497.6354225009
'''