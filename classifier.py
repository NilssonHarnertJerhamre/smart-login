from sklearn.neighbors import KNeighborsClassifier
import numpy as np


class Classifier:

	def __init__(self):
		self.train_on_data()

	def train_on_data(self):
		file = open("data.txt", "r")
		n_users = 50
		output = []
		labels = []

		for line in file.readlines()[1:]:
			line = line.strip().split()
			labels.append(line[0])
			line.pop(0)
			output.append(np.array(line).astype(np.float))
		file.close()

		self.neigh = KNeighborsClassifier(n_neighbors=5)
		self.neigh.fit(output, labels)

	def predict_user(self, input_data, user):
		print input_data
		predicted_user = self.neigh.predict([input_data])
		print predicted_user

		if predicted_user == user:
			return True
		else:
			return False




#print (neigh.predict([[0.0591, 0.1274, 0.0683, 0.0705, 0.1085, 0.0380, 0.0763, 0.0887, 0.0124, 0.0531, 0.2647, 0.2116, 0.0520, 0.3469, 0.2949, 0.1138, 0.1568, 0.0430, 
#.0953, 0.2474, 0.1521, 0.0932, 0.1210, 0.0278, 0.1376, 0.0892, -0.0484, 0.1109, 0.2298, 0.1189]]))



# s018
#0.0591, 0.1274, 0.0683, 0.0705, 0.1085, 0.0380, 0.0763, 0.0887, 0.0124, 0.0531, 0.2647, 0.2116, 0.0520, 0.3469, 0.2949, 0.1138, 0.1568, 0.0430, 
#0.0953, 0.2474, 0.1521, 0.0932, 0.1210, 0.0278, 0.1376, 0.0892, -0.0484, 0.1109, 0.2298, 0.1189


