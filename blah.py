'''file = open("data.txt", "r")
output = []
for line in file.readlines():
	line = line.strip().split()
	line.pop(1)
	line.pop(1)
	line.pop(31)
	output.append(line)
file.close()
file = open("data.txt", "w")
for line in output:
	s = ''
	for data in line:
		s += data + '\t'
	s.strip()
	s+='\n'
	file.write(s)
file.close()'''