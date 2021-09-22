from plot_from_excel import excel_plotter2 as fun2
import numpy as np

#the u0-initial value of angular momentum and t-time period of observation of rotation are determined by observation of meta data sheet properly

#for rotation along z-axis
plot_z = fun2('z_axis.xls',3,np.array([-0.622136354,-11.25114346,-19.92152596]),np.linspace(7.51,8.05,1000))
#for rotation along y-axis
plot_y = fun2('y_axis_correct.xls',3,np.array([-2.939576387,-34.90266418,0.657467783]),np.linspace(1.77,2.48,1000))

plot_y2= fun2('y_axis_correct.xls',4,np.array([-0.755261362,-32.4691391,-1.448037148]),np.linspace(5.9,6.71,1000))
#for rotation along x-axis
plot_x = fun2('x_axis.xls',2,np.array([24.87822533,1.106050849,3.684197664]),np.linspace(17.6,17.9,1000))
 

'''
OUTPUT for error analyis and comparision:

Theoretical Avg. of L for z_axis.xls = 11634.902462601893
Theoretical Avg of K for z_axis.xls= 121929.32139387296
Theoretical Avg. of L for y_axis_correct.xls = 3905.0508043407017
Theoretical Avg of K for y_axis_correct.xls = 65395.671766336054
Theoretical Avg. of L for y_axis_correct.xls 2 = 3491.12317623781
Theoretical Avg of K for y_axis_correct.xls 2= 55437.466025535985
Theoretical Avg. of L for x_axis.xls = 12128.36118904402
Theoretical Avg of K for x_axis.xls= 152497.6366366573
'''
