#Finding CSV ROW and COLUMN count


import csv
import webbrowser

with open('C:/Users/kwfp376/Documents/Temp/Webpage/AZCLOUD_N.Virginia_RDS_List_2018_06_28.csv') as csv_file:
	reader = csv.reader(csv_file)
	for linenum, line in enumerate(reader):
		if linenum == 0:
			colcount= (len(line))
			#print (colcount)
	csv_file.seek(0)
	rowcount = len(list(reader))
	#print (rowcount)
	#print (colcount)
	csv_file.seek(0)
	print ('<table border="1" style="border-collapse: collapse; width: 100%;"><tbody><tr style="background-color: #edccb8;">')
	for row in reader:
		for c in range(colcount):
			print ("<td >"+row[c]+"</td>")
		print('</tr><tr style="background-color: #def9ef;">')
	print ("</tr></tbody></table>")
	html = """
			<table >
			<tbody>
			<tr>
			<td >Name</td>
			<td >Age</td>
			<td >Sal</td>
			</tr>
			<tr>
			<td >Bob</td>
			<td >30</td>
			<td >10</td>
			</tr>
			</tbody>
			</table>
			"""
		
'''	
	#colcount = 0
	for linenum, line in enumerate(reader):
		if linenum == 0:
			colcount= (len(line))
			print ("Columns:"+str(colcount))
			
	csv_file.seek(0)		
	rowcount = len(file_content)
	#print ("columns:"+str(colcount))
	print ("Rows:"+str(rowcount))
'''
'''
	for row in range(rowcount):
		for col in range(colcount):
			print (file_content[row][col])
'''