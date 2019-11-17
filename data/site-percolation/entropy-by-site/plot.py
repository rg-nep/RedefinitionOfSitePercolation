import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import glob
import json
from datetime import datetime

sns.set()
length = 100

signature="sq_lattice_site_percolation_periodic__";

files = glob.glob(signature + "*")
ensembles = 0
data = None
for file in files:
	print(file)
	with open(file) as f:
		line = f.readline()
		head = json.loads(line[1:])
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
	index=np.linspace(0, X.shape[0]-1, 2000, dtype=int)
	plt.plot(x[index], X[:,1][index], label='L={}'.format(L))


plt.legend()
plt.show()