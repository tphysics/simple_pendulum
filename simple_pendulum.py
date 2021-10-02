import numpy as np
import matplotlib.pyplot as plt

def rk4step(f, t, x, dt):
	k1 = f(t,x)
	k2 = f(t+dt/2, x+k1*dt/2)
	k3 = f(t+dt/2, x+k2*dt/2)
	k4 = f(t+dt, x+k3*dt)
	return x+(dt*(k1+2*k2+2*k3+k4)/6)

def coupled_ode(t,x):
	#return np.array([x[1],-4*(np.pi**2)*x[0]]) #test
	return np.array([x[1],-4*(np.pi**2)*np.sin(x[0])])

ti=0
tf=4
dt=1e-2
t=np.arange(ti,tf,dt)
param=np.array([2,8,12.5,12.6,12.8,14])
fig, ax = plt.subplots(3,2)
fig.suptitle('"Simple" Pendulum')
k=0; l=0

for y in param:

	Sol=np.array([[0,y]])

	for i in np.arange(0,t.size-1,1):
		nextSol=rk4step(coupled_ode, t[i], Sol[i],dt)
		Sol=np.append(Sol, np.array([nextSol]), axis=0)

	idx = np.argwhere(np.diff(np.sign(Sol[:,0]))).flatten()
	if len(idx)==1:
		period=0
	else: period = t[idx[2]]-t[idx[1]]

	ax[k,l].plot(t,Sol[:,0])
	if l==0:
		ax[k,l].set_title(r'Librations with Period=%1.2f$\times T_0$, d($\phi$)/dt = %1.1f'%(period,y))
	else: ax[k,l].set_title(r'Circulations, d($\phi$)/dt = %1.1f'%(y))
	ax[k,l].set_xlabel(r'$\tau$')
	ax[k,l].set_ylabel(r'$\phi(\tau)$ (rad)')

	k=k+1
	if k>2:
		k=0
		l=l+1
plt.subplots_adjust(hspace=0.7)
plt.show()