import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import glob
import json
from datetime import datetime

sns.set()

length = 100

signature="sq_lattice_site_percolation_periodic__entropy_by_site_";


comments="""<p>	<H(p,L)>
p = occupation probability
T = temperature = 1-p 
H(p,L) = Entropy = sum( - u_i * log(u_i))
C(p,L) = Specific heat = -T dH/dT
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
		x = X[:,0]
		y = X[:,1]
		# index=np.linspace(1, X.shape[0]-1, 5000, dtype=int)
		# plt.plot(x[index], y[index], label='L={}'.format(L))
		
		if data is None:
			data = y*En
			pass
		else:
			data += y*En
			pass
		
		pass
	
	filename = "./avg/" + signature + "L{}".format(length) + "_avg.txt"

	data /= ensembles
	print("data.shape ", data.shape)
	index=np.linspace(0, data.shape[0]-1, 5000, dtype=int)
	x = np.linspace(1/(length*length), 1, data.shape[0])
	print(x[0])
	print(x[-1])
	plt.plot(x[index], data[index], label='L={}'.format(L))
	
	
	print(filename)
	plt.legend()
	head['ensemble_size'] = ensembles
	head['datetime'] = get_datetime()
	headstr = json.dumps(head)
	headstr += "\n"
	headstr += comments
	print(headstr)
	print(x.reshape((-1, 1)).shape)
	print(data.reshape((-1, 1)).shape)
	np.savetxt(filename, np.c_[x.reshape((-1, 1)), data.reshape((-1, 1))], fmt='%1.6e', header=headstr)
	pass


for L in range(100, 450, 50):
	print("*********L=", L)
	for_a_single_length(L)
	plt.show()
	# break