import csv

infile = open('info_security.txt', 'r')
csvfile = csv.reader(infile, delimiter = ' ')

encryption = {'A':'!', 'a':'@', 'B':'#', 'b':'$', 'C':'%'}

