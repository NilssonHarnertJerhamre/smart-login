from preprocess import *
from listener import *
import os
clear = lambda: os.system('cls')

while 0:
	clear()
	print 'smart login (pw .tie5Roanl)\n'
	print '1.\tlogin'
	print '2.\tcreate profile'

	print 'esc\texit'
	ans = raw_input('choice: ')

	print ans

pp = Preprocess()
l = Listener()

events = l.listen()
times = pp.preprocess(events)
print times