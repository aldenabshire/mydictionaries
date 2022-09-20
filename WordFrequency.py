import csv 

infile = open('sometext.txt', 'r')
csvfile = csv.reader(infile, delimiter = ' ')

dictionary = dict()

for word in infile:
    
    words = word.split(" ")

    for word in words:

        if word in dictionary:
            
            dictionary[word] = dictionary[word] + 1

        else:

            dictionary[word] = 1

print(dictionary)

    
