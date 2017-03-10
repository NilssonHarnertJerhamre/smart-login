from sklearn.neighbors import KNeighborsClassifier
import numpy as np


class Classifier:

	n_neighbors = 5

	labels = []
	output = []

	def __init__(self, datafile):
		self.datafile = datafile
		self.load_data_from_file()
		self.train_on_data()

	def load_data_from_file(self):

		file = open(self.datafile, "r")
		output = []
		labels = []

		for line in file.readlines():
			line = line.strip().split()
			self.labels.append(line[0])
			line.pop(0)
			self.output.append(np.array(line).astype(np.float))
		file.close()
		
	def train_on_data(self):
		self.neigh = KNeighborsClassifier(n_neighbors=self.n_neighbors)
		self.neigh.fit(self.output, self.labels)

	def predict_user(self, input_data):
		return self.neigh.predict([input_data])

	def add_data(self, data, user):
		with open(self.datafile, 'a') as file:
			s = '\n' + str(user) + '\t' + '\t'.join(str(x) for x in data)
			file.write(s)
		file.close()

		self.labels.append(user)
		self.output.append(np.array(data).astype(np.float))

		self.train_on_data()

	def profile_exists(self, user):
		if user in self.labels:
			return True
		else:
			return False



#print (neigh.predict([[0.0591, 0.1274, 0.0683, 0.0705, 0.1085, 0.0380, 0.0763, 0.0887, 0.0124, 0.0531, 0.2647, 0.2116, 0.0520, 0.3469, 0.2949, 0.1138, 0.1568, 0.0430, 
#.0953, 0.2474, 0.1521, 0.0932, 0.1210, 0.0278, 0.1376, 0.0892, -0.0484, 0.1109, 0.2298, 0.1189]]))



# s018
#0.0591, 0.1274, 0.0683, 0.0705, 0.1085, 0.0380, 0.0763, 0.0887, 0.0124, 0.0531, 0.2647, 0.2116, 0.0520, 0.3469, 0.2949, 0.1138, 0.1568, 0.0430, 
#0.0953, 0.2474, 0.1521, 0.0932, 0.1210, 0.0278, 0.1376, 0.0892, -0.0484, 0.1109, 0.2298, 0.1189


