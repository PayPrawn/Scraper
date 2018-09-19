firststructure = 'a'
secondstructure = ['m', 's', 'w']
thirdstructure = ['h','j','s']

twoletterwordarray = []
threeletterwordarray = []
spacing = (20 * ' ')
seperator = ('\n' + (spacing) + '|')
len_secondstructure = len(secondstructure)
len_thirdstructure = len(thirdstructure)
final = ''


print('\n\n')


#working code


for i in range(len_secondstructure):
    twoletterword = firststructure + secondstructure[i]
    twoletterwordarray.append(twoletterword)
for i in range(len_thirdstructure):
    threeletterword = thirdstructure[i] + firststructure + secondstructure[0]
    threeletterwordarray.append(threeletterword)

for i in range(len_secondstructure):
    final = final + twoletterwordarray[i] + spacing

print(final)


print('\n\n')


#testing area
