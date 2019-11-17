import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import glob
import json
from datetime import datetime

sns.set()

length = 100

signature="sq_lattice_site_percolation_periodic__";


comments="""<p>	<H(p,L)>	<P1(p,L)>	<P2(p,L)>
p = occupation probability
T = temperature = 1-p 
H(p,L) = Entropy = sum( - u_i * log(u_i))
P1(p,L) = Order parameter = (number of bonds in largest cluster) / (total number of bonds)
P2(p,L) = Order parameter = (number of bonds in spanning or wrapping cluster) / (total number of bonds)
C(p,L) = Specific heat = -T dH/dT
X(p,L) = Susceptibility = dP/dp 
u_i = (number of bonds in the i-th cluster) / (total number of bonds)"""

def get_datetime():
	tm = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
	return tm

def for_a_single_length(length):
	files = glob.glob(signature + "{}*".format(length))
	ensembles = 0
	data = None
	for file in files:
		print(file)
		with open(file) as f:
			line = f.readline()
			head = json.loads(line)
			L=int(head['length'])
			En=int(head['ensemble_size'])
			ensembles += En
			pass
		X = np.loadtxt(file, skiprows=1)
		print(X.shape)
		print(X.shape[0])
		print(X.shape[1])
		print(X[0,:])
		# exit(0)
		# x = X[:,0]
		# index=np.linspace(10, X.shape[0]-10, 5000, dtype=int)
		# plt.plot(x[index], X[:,1][index], label='L={}'.format(L))
		# plt.plot(x[index], X[:,2][index], label='L={}'.format(L))
		# plt.plot(x[index], X[:,3][index], label='L={}'.format(L))
		if data is None:
			data = X*En
			pass
		else:
			data += X*En
			pass
		
		pass
	filename = "./avg/" + signature + "entropy_order_L{}".format(length) + "_avg.txt"

	data /= ensembles

	index=np.linspace(10, data.shape[0]-10, 5000, dtype=int)
	x = np.linspace(1/(length*length), 1, data.shape[0])
	print(x[0])
	print(x[-1])
	plt.plot(x[index], data[:,1][index], label='L={}'.format(L))
	plt.plot(x[index], data[:,2][index], label='L={}'.format(L))
	plt.plot(x[index], data[:,3][index], label='L={}'.format(L))



	print(filename)
	plt.legend()
	head['ensemble_size'] = ensembles
	head['datetime'] = get_datetime()
	headstr = json.dumps(head)
	headstr += "\n"
	headstr += comments
	print(headstr)
	print(x.reshape((-1, 1)))
	np.savetxt(filename, np.c_[x.reshape((-1, 1)), data[:,1:]], fmt='%1.6e', header=headstr)
	pass


for L in range(100, 450, 50):
	print("*********L=", L)
	for_a_single_length(L)
	plt.show()
	# break