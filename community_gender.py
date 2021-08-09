#counts amount of words said by each person

import matplotlib.pyplot as plt
script = open("s1e1.txt")
name2words = {} #contains 
names = ["Jeff:", "Troy:", "Abed:", "Pierce:", "Duncan:", "Dean:", "Britta:", "Annie:", "Shirley:"]

#initalise all lines at zero
for name in names:
	name2words[name] = 0

current_name = "Dean:"
for line in script:
	line = line.rstrip()
	for word in line.split(" "):
		print(word)
		if word in names:
			current_name = word #current word
			
		else: #if word not in names
			#add tally to current person
			name2words[current_name] = name2words[current_name] + 1
print(name2words)


#draw PIE CHART

labels = "Jeff:", "Troy:", "Abed:", "Pierce:", "Duncan:", "Dean:", "Britta:", "Annie:", "Shirley:"

word_list = []
for name in name2words:
	word_list.append(name2words[name])
print(word_list)

fig1, ax1 = plt.subplots()
ax1.pie(word_list, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


