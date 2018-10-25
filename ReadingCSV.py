import csv
import webbrowser

with open('C:/Users/kwfp376/Documents/Temp/Webpage/Iopreview.csv') as csv_file:
	reader = csv.reader(csv_file)
	line_count = 0
	for row in reader:
		print (line_count)
		if line_count == 0:
			#print(', '.join(row))
			Account = row[1]
		elif line_count == 1:
			EC2_count = row[1]
		elif line_count == 2:
			EBS_count = row[1]
		elif line_count == 3:
			S3_count = row[1]
		elif line_count == 4:
			RDS_count = row[1]
		elif line_count == 5:
			Redshift_count = row[1]
		
		
		
		line_count +=1

#Name = "Babu"		
html_file_path = "C:/Users/kwfp376/Documents/Temp/Webpage/Inventory.html"		
html_file = open('Inventory.html', 'w')
message = """ <p style="text-align: right;">10/06/2018</p>
<p><span style="text-align: left; color: #0000ff;"><span style="text-decoration: underline;"><strong>AZ AWS Inventory Report</strong></span></span></p>
<p style="text-align: left;"><span style="text-decoration: underline;"><strong>Total AWS Resource Summary</strong></span></p>
<table style="width: 210px; height: 146px; border-color: #566573;">
<thead>
<tr style="background-color: #85c1e9;">
<td style="width: 43px; text-align: center;"><strong>S.No</strong></td>
<td style="width: 82px;"><strong>Resource</strong></td>
<td style="width: 63px;"><strong>Count</strong></td>
</tr>
</thead>
<tbody>
<tr style="background-color: #fdedec;">
<td style="width: 43px; text-align: center;">1</td>
<td style="width: 82px;">EC2</td>
<td style="width: 63px;">"""+EC2_count+"""</td>
</tr>
<tr>
<td style="width: 43px; text-align: center;">2</td>
<td style="width: 82px;">EBS</td>
<td style="width: 63px;">"""+EBS_count+"""</td>
</tr>
<tr style="background-color: #fdedec;">
<td style="width: 43px; text-align: center;">3</td>
<td style="width: 82px;">S3</td>
<td style="width: 63px;">"""+S3_count+"""</td>
</tr>
<tr>
<td style="width: 43px; text-align: center;">4</td>
<td style="width: 82px;">RDS</td>
<td style="width: 63px;">"""+RDS_count+"""</td>
</tr>
<tr style="background-color: #fdedec;">
<td style="width: 43px; text-align: center;">5</td>
<td style="width: 82px;">Redshift</td>
<td style="width: 63px;">"""+Redshift_count+"""</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>"""

html_file.write(message)
html_file.close()

