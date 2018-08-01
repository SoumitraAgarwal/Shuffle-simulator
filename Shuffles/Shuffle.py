import random

inital_deck = range(1,53)
f = open("../Data/init.txt", "w+")
for card in inital_deck:
	f.write(str(card) + '\n')
f.close()

# The overhand

card_threshold = 5;
for seconds in [3,6, 10]:
	
	overhand = inital_deck
	for iterations in range(seconds):
		
		length 	= 52
		split 	= length/2 + random.randint(0,10)

		while(length > card_threshold):
			list1 		= overhand[0:split]
			list2 		= overhand[split:length]
			overhand[0:length] 	= list2 + list1

			length 		= split
			split 		= length/2 + random.randint(0,length/5)
	
	f = open("../Data/overhand_" + str(seconds) + ".txt", "w+")
	for card in overhand:
		f.write(str(card) + '\n')
	f.close()


# The ruffle

for seconds in [2,4, 10]:
	
	ruffle = inital_deck
	for iterations in range(seconds):
		
		length 	= 52
		split 	= length/2 + random.randint(0,2)

		iterator_1 = 0;
		iterator_2 = split;

		temp = []
		while(iterator_2 < 52 or iterator_1 < split):

			stand = random.randint(1,4)
			if(iterator_1 + stand < split):
				temp += ruffle[iterator_1:iterator_1 + stand]
				iterator_1 += stand;

			elif(iterator_1 < split):
				temp += ruffle[iterator_1:split]
				iterator_1 = split

			else:
				temp += ruffle[iterator_2:52]
				iterator_2 = 52

			stand = random.randint(1,4)	
			if(iterator_2 + stand < 52):
				temp += ruffle[iterator_2:iterator_2 + stand]
				iterator_2 += stand

			elif(iterator_2 < 52):
				temp += ruffle[iterator_2:52]
				iterator_2 = 52

			else:
				temp += ruffle[iterator_1:split]
				iterator_1 = split

			# print(iterator_1, iterator_2, split, len(temp))
		ruffle = temp
	f = open("../Data/ruffle_" + str(seconds) + ".txt", "w+")
	for card in ruffle:
		f.write(str(card) + '\n')
	f.close()


# Smooshing

for seconds in [3,6, 10]:
	
	smooshing = inital_deck
	start 	= 0
	for iterations in range(seconds):
		
		while(start < 45):
			start_1		= start + random.randint(0,7)
			temp 		= smooshing[start]
			smooshing[start] =  smooshing[start_1]
			smooshing[start_1] = temp
			start = start_1

	f = open("../Data/smoosh_" + str(seconds) + ".txt", "w+")
	for card in overhand:
		f.write(str(card) + '\n')
	f.close()

