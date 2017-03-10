from profile import *
from preprocess import *
from listener import *
from classifier import *
from knn import *
import numpy as np
import os

datafile = 'data.txt'
phrase = '.tie5roanl'
samples_for_new_profile = 7
clear = lambda: os.system('cls')

pp = Preprocess()
l = Listener()
c = Classifier(datafile)

def login():
	user = raw_input('user: ')
	events = l.listen(phrase)
	input = ''
	for e in events:
		if e.type is Type.key_pressed and isinstance(e.char, unicode):
			input += e.char.encode('utf-8')

	if input != phrase:
		raw_input('wrong phrase \n<enter to continue>')
		return

	times = pp.preprocess(events)

	prediction = c.predict_user(times)

	print 'chosen profile is \'' + str(user) + '\' prediction was \'' + str(prediction[0]) + '\''

	if str(user) == str(prediction[0]):
		c.add_data(times, user)
		c.train_on_data()

	raw_input('<enter to continue>')

def create_profile():
	user = raw_input('user: ')

	if c.profile_exists(user):
		raw_input('profile already exists <enter to continue>')
		return

	training_times = []

	i = 0
	while i < samples_for_new_profile:
		print 'type the phrase ('+str(i+1)+' of '+str(samples_for_new_profile)+' times)'
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
		c.add_data(t, user)

while 1:
	clear()
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