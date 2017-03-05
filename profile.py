import numpy as np

class Profile:

	data = []
	labels = []


	def __init__(self, datafile):
		self.datafile = datafile

		print 'loading training data...'

		file = open(datafile, "r")
		for line in file.readlines()[1:]:
			line = line.strip().split()
			
			self.data.append(line[1:])
			self.labels.append(line[0])	
		file.close()

	def profile_exists(self, user):

		if user in self.labels:
			return True
		else:
			return False

	def add_data(self, user, data):
		with open(self.datafile, 'a') as file:
			self.data.append(data)
			self.labels.append(user)
			s = '\n' + user + '\t' + '\t'.join(str(x) for x in data)
			file.write(s)
		file.close()
