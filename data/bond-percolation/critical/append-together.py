import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
import glob
import json
from datetime import datetime



length = 100

signature="sq_lattice_bond_percolation__periodic__critical_";

comments="""data at critical occupation probability or pc
<pc><sites in wrapping cluster><bonds in wrapping cluster>"""

def get_datetime():
	tm = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
	return tm

def for_a_single_length(length):
	files = glob.glob(signature + "L{}*".format(length))
	ensembles = 0
	data = None
	for file in files:
		print(file)
		with open(file) as f:
			line = f.readline()
			print(line)
			print(line.split(','))
			head = json.loads(line[1:])
			L=int(head['length'])
			pass
		X = np.loadtxt(file, skiprows=1)
		print(X.shape)
		print(X.shape[0])
		print(X.shape[1])

		if data is None:
			data = X
			pass
		else:
			data = np.append(data, X, axis=0)
			pass
		
		pass

	filename = "./avg/" + signature + "L{}".format(length) + "_.txt"

	print(data)
	# print(np.mean(data, axis=0))
	
	print(filename)
	
	print(data.shape)

	head['ensemble_size'] = data.shape[0]
	head['datetime'] = get_datetime()
	headstr = json.dumps(head)
	headstr += "\n"
	headstr += comments
	print(headstr)
	
	np.savetxt(filename, data, fmt=['%.6f', '%6d', '%6d'], header=headstr)
	pass


for L in range(100, 450, 50):
	print("*********L=", L)
	for_a_single_length(L)
	break
	