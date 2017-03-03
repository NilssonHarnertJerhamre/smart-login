from pynput import keyboard

class Preprocess:

	def preprocess(self, input):

		processed_data = []

		idx = -1
		for e in input:
			idx += 1
			char = ''

			if e.char == keyboard.Key.enter:
				break
			if e.type.value == 1:
				char = e.char
			if e.type.value == 2:
				continue

			for e_ in input[idx+1:]:
				if e_.type.value == 2 and e_.char == char:
					end = e_
					break
			for e_ in input[idx+1:]:
				if e_.type.value == 1:
					next = e_
					break
			
			'''
			for index, s in enumerate(input):
				if s is e:
					print 'e pos\t' + str(index)
			for index, s in enumerate(input):
				if s is next:
					print 'next pos\t' + str(index)
			'''
			
			processed_data.append(end.time - e.time) 	# H
			processed_data.append(next.time - e.time) 	# DD
			processed_data.append(next.time - end.time) # UD
			
			#print char
			#print str(end.time - e.time) + '\t' + str(next.time - e.time) + '\t' + str(next.time - end.time)

		return processed_data