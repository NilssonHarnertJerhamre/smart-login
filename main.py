from profile import *
from preprocess import *
from listener import *
from classifier import *
import os

datafile = 'data.txt'
phrase = '.tie5roanl'
clear = lambda: os.system('cls')

p = Profile(datafile)
pp = Preprocess()
l = Listener()
c = Classifier()

def login():
	user = raw_input('user: ')
	events = l.listen(phrase)
	input = ''
	for e in events:
		if e.type is Type.key_pressed and isinstance(e.char, unicode):
			input += e.char.encode('utf-8')

	if input != phrase:
		raw_input('wrong phrase <enter to continue>')
		return

	times = pp.preprocess(events)

	# do AI
	# display result

	#p.add_data(user, times)

	raw_input('<enter to continue>')

def create_profile():
	user = raw_input('user: ')

	if p.profile_exists(user):
		raw_input('profile already exists <enter to continue>')
		return

	training_times = []

	i = 0
	while i < 3:
		print 'type the phrase ('+str(i+1)+' of 3 times)'
		events = l.listen(phrase)
		
		s = ''
		for e in events:
			if e.type is Type.key_pressed and isinstance(e.char, unicode):
				s += e.char.encode('utf-8')

		if s != phrase:
			print 'wrong phrase!'
			continue
		times = pp.preprocess(events)
		training_times.append(times)
		i+=1

	for t in training_times:
		p.add_data(user, t)

while 1:
	#clear()
	print 'smart login\n'
	print '1.\tlogin'
	print '2.\tcreate profile'
	print 'q.\tquit'

	ans = raw_input('choice: ')

	if ans == '1':
		login()
	elif ans == '2':
		create_profile()
	elif ans == 'q': #quit
		break