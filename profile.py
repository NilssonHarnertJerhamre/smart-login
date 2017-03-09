import numpy as np

class Profile:

	data = np.array([np.zeros(30, dtype=float)], dtype=float)
	labels = np.array(['test'], dtype=str)

	def __init__(self, datafile):
		self.datafile = datafile

		print 'loading training data...'

		file = open(datafile, "r")

		for line in file.readlines()[1:]:
			line = line.strip().split()
			self.data = np.append(self.data, [np.array(line[1:]).astype(np.float)], axis=0)
			self.labels = np.append(self.labels, [np.array(line[0]).astype(np.str)], axis=0)	
		file.close()

	def profile_exists(self, user):
		if user in self.labels:
			return True
		else:
			return False

	def add_data(self, user, data):
		with open(self.datafile, 'a') as file:
			self.data = np.append(self.data, [np.array(data).astype(np.float)], axis=0)
			self.labels = np.append(self.labels, [np.array(user).astype(np.str)], axis=0)	
			s = '\n' + user + '\t' + '\t'.join(str(x) for x in data)
			file.write(s)
		file.close()
