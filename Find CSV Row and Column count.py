#Finding CSV ROW and COLUMN count

import csv
import webbrowser
'''
with open('C:/Users/kwfp376/Documents/Temp/Webpage/resources.csv') as csv_file:
	reader = csv.reader(csv_file)
	for linenum, line in enumerate(reader):
		if linenum == 0:
			colcount= (len(line))
			print (colcount)
			
			
with open('C:/Users/kwfp376/Documents/Temp/Webpage/resources.csv') as csv_file:
	reader = csv.reader(csv_file)
	rowcount = len(list(reader))
	print (rowcount)
'''
with open('C:/Users/kwfp376/Documents/Temp/Webpage/Iopreview.csv') as csv_file:
	reader = csv.reader(csv_file)	
	line_count = 0
	for row in reader:
		for 
		#print (line_count)
		#if line_count == 0:
		print(row[1])