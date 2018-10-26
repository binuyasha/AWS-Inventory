#Finding CSV ROW and COLUMN count


import csv
import webbrowser

in_csvfile = "C:/Users/kwfp376/Documents/Temp/Webpage/IOPreview_files/IOPreview_Ireland_EBS_Snapshot_List_2018_10_22.csv"
out_htmlfile = "C:/Users/kwfp376/Documents/Temp/Webpage/IOPreview_files/IOPreview_Ireland_EBS_Snapshot_List_2018_10_22.html"


def csv_to_html (csvfile, htmlfile):

	with open(csvfile) as csv_file:
		reader = csv.reader(csv_file)
		for linenum, line in enumerate(reader):
			if linenum == 0:
				colcount= (len(line))
				
		csv_file.seek(0)
		rowcount = len(list(reader))

		csv_file.seek(0)
		html_file = open(htmlfile, "w")
		
		html_file.write('<table border="1" style="border-collapse: collapse; width: 100%;"><tbody><tr style="background-color: #edccb8;">')
		for row in reader:
			for c in range(colcount):
				html_file.write ("<td >"+row[c]+"</td>")
			html_file.write('</tr><tr style="background-color: #def9ef;">')
		html_file.write ("</tr></tbody></table>")

csv_to_html(in_csvfile, out_htmlfile)