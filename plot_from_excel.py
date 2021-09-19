#calling all required libraries
from Rk4_simulation import RungKutta4 
from Rk4_simulation import energy
from Rk4_simulation import ang_momentum

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def excel_plotter(excel_file,sheet,u0,t1):
	data = pd.read_excel(excel_file, sheet_name=sheet,header= None, skiprows=1)
	data.columns = ['Time (s)', 'Gyroscope x (rad/s)','Gyroscope y (rad/s)', 'Gyroscope z (rad/s)','Absolute (rad/s)']

	#defining the data points
	t = data['Time (s)']
	x = data['Gyroscope x (rad/s)']
	y = data['Gyroscope y (rad/s)']
	z = data['Gyroscope z (rad/s)']

	def D(u,t1):
	
	#C1,C2,C3 are Constants here cause we analytically calculated the Inertia so we just declare here
		C1 =-0.994379
		C2 =0.974025
		C3 =0.64741
		return np.array([C1*u[1]*u[2], C2*u[2]*u[0], C3*u[1]*u[0]])

	#calling RK-4 function to operate the ODE above
	out = RungKutta4(D,u0,t1)
	
	#plotting theoretical line with proper labels
	plt.plot(t1,out[:,0],'palegreen',label = "theoretical omega_x")
	plt.plot(t1,out[:,1],'cornflowerblue',label = "theoretical omega_y")
	plt.plot(t1,out[:,2],'magenta',label = "theoretical omega_z")

	#plotting the defined data points from the meta data sheet
	plt.plot(t, x, 'g--', label = 'omega_x' )
	plt.plot(t, y, 'b--', label = 'omega_y')
	plt.plot(t, z, 'r--', label= 'omega_z')

	plt.legend(loc ='upper left')
	plt.xlabel('Time (s)')
	plt.ylabel('Angular velocity (rad/s)')
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=3)
	plt.grid()
	plt.show()


#calling the data sheet with calculated kinetic energy and angular momentum
def excel_plotter2(excel_file,sheet,u0,t1):
	data = pd.read_excel(excel_file, sheet_name=sheet,header= None, skiprows=1)
	data.columns = ['Time (s)', 'Gyroscope x (rad/s)','Gyroscope y (rad/s)', 'Gyroscope z (rad/s)','Absolute (rad/s)', 'y','y2']

	t = data['Time (s)']
	#here L- angular momentum and K- Kinetic energy
	L = data['y']
	K = data['y2']

	#defining the ODE equation as function
	def D(u,t1):
	
	#C1,C2,C3 are Constants here cause we analytically calculated the Inertia so we just declare here
		C1 =-0.994379
		C2 =0.974025
		C3 =0.64741
		return np.array([C1*u[1]*u[2], C2*u[2]*u[0], C3*u[1]*u[0]])
	
	#calling Rk-4 function to solve the above ODE 
	out2 = RungKutta4(D,u0,t1)	
	#calling Energy calculator function to calculate Kinetic energy taking in the result of RK-4 integration of its raw data	
	KE = energy(out2)
	ANG_MOM=ang_momentum(out2)

	plt.plot(t,L, 'g--',label='Angular Momentum')
	plt.plot(t1,ANG_MOM.transpose(),'r',label='Theoretical L')
	
	plt.legend(loc ='best')
	plt.xlabel('Time (s)')
	plt.ylabel('Angular Momentum (\mu J s)')
	plt.grid()
	plt.show()
	
	plt.plot(t,K, 'b--',label='Kinetic Energy')
	#as the solution obtained from the energy function is 1-D row it is not favourable for plotting with t in x-axis we use transpose to convert it into column vector
	plt.plot(t1,KE.transpose(),'r',label='Theoretical KE')
	plt.legend(loc ='best')
	plt.xlabel('Time (s)')
	plt.ylabel('Kinetic Energy (\mu J)')
	plt.grid()
	plt.show()
	



