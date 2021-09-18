from Rk4_simulation import RungKutta4 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def excel_plotter(excel_file,sheet,u0,t1):
	data = pd.read_excel(excel_file, sheet_name=sheet,header= None, skiprows=1)
	data.columns = ['Time (s)', 'Gyroscope x (rad/s)','Gyroscope y (rad/s)', 'Gyroscope z (rad/s)','Absolute (rad/s)']



	t = data['Time (s)']
	x = data['Gyroscope x (rad/s)']
	y = data['Gyroscope y (rad/s)']
	z = data['Gyroscope z (rad/s)']
	'''L = data['y']
	K = data['y2']'''

	def D(u,t1):
	
	#C1,C2,C3 are Constants here cause we analytically calculated the Inertia so we just declare here
		C1 =-0.994379
		C2 =0.974025
		C3 =0.64741
		return np.array([C1*u[1]*u[2], C2*u[2]*u[0], C3*u[1]*u[0]])

	out = RungKutta4(D,u0,t1)
	plt.plot(t1,out[:,0],'g')
	plt.plot(t1,out[:,1],'b')
	plt.plot(t1,out[:,2],'r')


	plt.plot(t, x, 'g--', label = 'x-axis' )
	plt.plot(t, y, 'b--', label = 'y-axis')
	plt.plot(t, z, 'r--', label= 'z-axis')

	plt.legend(loc ='upper left')
	plt.xlabel('Time (s)')
	plt.ylabel('Angular velocity (rad/s)')
	plt.grid()
	plt.show()



	'''plt.plot(t,L, 'g--')
	plt.grid()
	plt.show()
	plt.plot(t,K, 'r--')
	plt.grid()
	plt.show()'''

def excel_plotter2(excel_file,sheet):
	data = pd.read_excel(excel_file, sheet_name=sheet,header= None, skiprows=1)
	data.columns = ['Time (s)', 'Gyroscope x (rad/s)','Gyroscope y (rad/s)', 'Gyroscope z (rad/s)','Absolute (rad/s)', 'y','y2']

	t = data['Time (s)']
	L = data['y']
	K = data['y2']


	plt.plot(t,L, 'g--')
	plt.legend(loc ='upper left')
	plt.xlabel('Time (s)')
	plt.ylabel('Angular Momentum ($\mu J s)')
	plt.grid()
	plt.show()
	
	plt.plot(t,K, 'r--')
	plt.legend(loc ='upper left')
	plt.xlabel('Time (s)')
	plt.ylabel('Kinetic Energy ($\mu J)')
	plt.grid()
	plt.show()
	








'''excel_file = 'z_axis.xls'
z_data = pd.read_excel(excel_file, sheet_name=2,header= None,skiprows=1)
z_data.columns = ['Time (s)', 'Gyroscope x (rad/s)','Gyroscope y (rad/s)', 'Gyroscope z (rad/s)','Absolute (rad/s)']



t = z_data['Time (s)']
x = z_data['Gyroscope x (rad/s)']
y = z_data['Gyroscope y (rad/s)']
z = z_data['Gyroscope z (rad/s)']

plt.plot(t, x, 'g--', label = 'x-axis' )
plt.plot(t, y, 'b--', label = 'y-axis')
plt.plot(t, z, 'r--', label= 'z-axis')

plt.legend(loc ='upper left')
plt.xlabel('Time (s)')
plt.ylabel('Angular velocity (rad/s)')
plt.show()'''



