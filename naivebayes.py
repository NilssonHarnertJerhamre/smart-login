from sklearn.naive_bayes import GaussianNB
import numpy as np

file = open("data.txt", "r")
n_users = 50
output = []
labels = []
i = 0
for line in file.readlines()[1:]:
	line = line.strip().split()
	labels.append(line[0])
	line.pop(0)
	output.append(np.array(line).astype(np.float))
file.close()


clf = GaussianNB().fit(output, labels)

print clf.predict([[0.1491, 0.3979, 0.2488, 0.1069, 0.1674, 0.0605,0.1169, 0.2212, 0.1043, 0.1417, 1.1885, 1.0468, 
	0.1146, 1.6055, 1.4909, 0.1067, 0.7590, 0.6523, 0.1016, 0.2136, 0.1120, 0.1349, 0.1484, 0.0135, 0.0932, 0.3515,	
	0.2583, 0.1338, 0.3509,	0.2171]])

print clf.score([[0.1111, 0.3451, 0.2340, 0.0694, 0.1283, 0.0589, 0.0908, 0.1357, 0.0449, 0.0829, 1.1970, 1.1141, 
	0.0689, 0.7822, 0.7133, 0.1570, 0.7877, 0.6307, 0.1066, 0.1684, 0.0618, 0.1412, 0.2558, 0.1146, 0.1146, 0.2642, 
	0.1496, 0.0839, 0.2756, 0.1917]],['s016'])


