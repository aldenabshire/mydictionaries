import csv

infile = open('info_security.txt', 'r')
outfile = open('encrypted.txt', 'w')
csvfile = csv.reader(infile, delimiter = ' ')

alphabet = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','.',':']

encryption = {}

codes = ['!','$','@','#','%','^','&','*','-','4','2,','9','<','>','?','/','~','`','.',',','=','+','12','8','90','21','45','100','32','21','45','11','15','17','18','19','23','93','92','95','98','96','102,','103', '105','107','110','123','143','156','176','312','14325','3242','2466243', '245543','2463453','357357','7695679']

a = 0

for letter in alphabet:

    encryption[letter] = codes[a]

    a += 1

for row in csvfile:

    for word in row:

        for letter in word:

            outfile.write(encryption[letter] + ' ')

#check dicitonary with encryption

print(encryption)  

outfile.close()

  

           



