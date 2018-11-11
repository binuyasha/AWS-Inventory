#Instance Summary Plotly

import boto3
import collections
import datetime
import csv
from time import gmtime, strftime

date_fmt = strftime("%Y_%m_%d", gmtime())
regions=['us-east-1', 'eu-west-1', 'ap-southeast-1']
account = 'IOPreview'
html_out_file = "Volume_html_Summary_With_Plotly_Chart_3.html"



def Write_html_headder():
	
	html_file_handle = open(html_out_file, "w")
	html_file_handle.write("""<!doctype html>
		<html>

		<head>
			<script src="Lib\plotly-latest.min.js"></script>
			<script src="""+"Lib\numeric.min.js"+"""></script>
		</head>
		
		<body>
		<style>
		
		
		</style>
			
			<div style="width: 100%; overflow: hidden;">
				<table border="0" style="border-collapse: collapse; width: 100%;border-style: hidden;">
				<tbody>
				<tr>
				<td style="width: 33.3333%;text-align: center;"><strong>US East (N. Virginia)</strong></td>
				<td style="width: 33.3333%;text-align: center;"><strong>EU (Ireland) </strong></td>
				<td style="width: 33.3333%;text-align: center;"><strong>Asia Pacific (Singapore)</strong> </td>
				</tr>
				<tr>
				<td style="width: 33.3333%;"> <div id="myDiv"><!-- Plotly chart will be drawn inside this DIV --></div></td>
				<td style="width: 33.3333%;"><div id="myDiv1"><!-- Plotly chart will be drawn inside this DIV --></div></td>
				<td style="width: 33.3333%;"><div id="myDiv2"><!-- Plotly chart will be drawn inside this DIV --></div></td>
				</tr>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 33.3333%; height: 20px;">
				<div id="myDiv"></div>
				</td>
				<td style="width: 33.3333%; height: 20px;">
				<div id="myDiv1"></div>
				</td>
				<td style="width: 33.3333%; height: 20px;">
				<div id="myDiv2"></div>
				</td>
				</tr>
				<tr style="height: 17px;">
				<td style="width: 33.3333%; height: 25px; text-align: center;">
				<div id="myDiv"><hr /><strong><strong>US</strong></strong><hr /></div>
				</td>
				<td style="width: 33.3333%; height: 25px; text-align: center;">
				<div id="myDiv1"><hr /><strong><strong>Ireland</strong></strong><hr /></div>
				</td>
				<td style="width: 33.3333%; height: 25px; text-align: center;">
				<div id="myDiv2"><hr /><strong><strong>Singapore</strong></strong><hr /></div>
				</td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 33.3333%; height: 20px;">
				""")
	html_file_handle.close()

def Write_html_body(reg):

	if reg == 'us-east-1':
		data = 'usdata'
	elif reg == 'eu-west-1':
		data = 'eudata'
	elif reg == 'ap-southeast-1':
		data = 'sgdata'
	
	reg,io1_count, gp2_count, st1_count,sc1_count, In_Use_State, Available_State, Not_Encrypted_Count,	Encrypted_Count, Size_0_100, Size_100_500, Size_500_More= Volume_summary(reg)
	html_file_handle=open(html_out_file, "a")
	html_file_handle.write("""<table border="0" style="height: 264px; width: 0%; border-collapse: collapse; border-style: hidden; margin-left: auto; margin-right: auto;" height="97">
				<tbody>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"><strong>Provisioned_IOPS_SSD</strong>:</td>
				<td style="width: 5%; height: 22px;"><strong style="color: #06f968;">"""+str(io1_count)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;"><strong>General Purpose SSD</strong>:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(gp2_count)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;"><strong>Throughput_Optimized_HDD</strong>:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(st1_count)+"""</strong></td>
				</tr>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 21px;">Cold HDD:</td>
				<td style="width: 5%; height: 21px;"><strong style="color: #06f968;">"""+str(sc1_count)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Attached Volumes:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(In_Use_State)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Unattached Volumes:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(Available_State)+"""</strong></td>
				</tr>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 21px;">Volumes Encrypted:</td>
				<td style="width: 5%; height: 21px;"><strong style="color: #06f968;">"""+str(Encrypted_Count)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Volumes Not Encrypted:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(Not_Encrypted_Count)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">100GB to 500GB:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(Size_0_100)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">500GB to 1TB:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(Size_100_500)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">More than 1TB:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(Size_500_More)+"""</strong></td>
				</tr>
				</tbody>
				</table>
				</td>
						<script>

									var """+str(data)+""" = [{
									y: ["""+str(Size_0_100)+""","""+str(Size_100_500)+""","""+str(Size_500_More)+"""],
									x: ['0GB to 100GB', '100GB to 500GB', 'More than 500GB'],
									type: 'bar'
										}];
						</script>
				""")
	html_file_handle.close()
	
	
def Volume_summary(reg):
		
	io1_count = 0
	gp2_count = 0
	st1_count = 0
	sc1_count = 0
	In_Use_State = 0
	Available_State = 0
	Not_Encrypted_Count = 0
	Encrypted_Count = 0
	Size_0_100 =0
	Size_100_500 = 0
	Size_500_More = 0
	
	
	ec2con = boto3.client('ec2',region_name=reg)
	ec2volumes = ec2con.describe_volumes().get('Volumes',[])


	volumes = sum(
		[
			[i for i in r['Attachments']]
			for r in ec2volumes
		], [])
	
	volumeslist = len(ec2volumes)
	if volumeslist > 0:
		for volume in ec2volumes:
			Voltype = volume['VolumeType']
			if Voltype == "io1":
				io1_count = io1_count + 1
			elif Voltype == "gp2":
				gp2_count = gp2_count +1
			elif Voltype == "st1":
				st1_count = st1_count + 1
			elif Voltype == "sc1":
				sc1_count = sc1_type + 1
				
			
			Vol_State=volume['State']
			if Vol_State == "in-use":
				In_Use_State = In_Use_State + 1
			elif Vol_State == "available":
				Available_State = Available_State +1
			
			Encrypted = volume['Encrypted']
			if Encrypted == False :
				Not_Encrypted_Count = Not_Encrypted_Count + 1
			elif Encrypted == True :
				Encrypted_Count = Encrypted_Count + 1
			Size = volume['Size']
			if Size > 0 and Size < 100:
				Size_0_100 = Size_0_100 + 1
			elif Size > 100 and Size < 500:
				Size_100_500 = Size_100_500 + 1
			elif Size > 500:
				Size_500_More = Size_500_More + 1
				
			
		
		
		
	
	filepath ='IOPreview_'+reg+'_Volume_Summary_' + date_fmt + '.csv'
	filename ='IOPreview_'+reg+'_Volume_Summary_' + date_fmt + '.csv'

	csv_file = open(filepath,'w+')
	csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n"%("Region","io1_count", "gp2_count", "st1_count","sc1_count", "In_Use_State", "Available_State", "Not_Encrypted_Count",	"Encrypted_Count", "Size_0_100", "Size_100_500", "Size_500_More"))

	csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n"% (reg,io1_count, gp2_count, st1_count,sc1_count, In_Use_State, Available_State, Not_Encrypted_Count,	Encrypted_Count, Size_0_100, Size_100_500, Size_500_More))
	csv_file.flush()
	
	return reg,io1_count, gp2_count, st1_count,sc1_count, In_Use_State, Available_State, Not_Encrypted_Count,	Encrypted_Count, Size_0_100, Size_100_500, Size_500_More;
	
	
def Write_html_footer():
	html_file_handle = open(html_out_file, "a")
	html_file_handle.write("""
		</tr>
		</tbody>
		</table>
		</div>
	<script>
		var layout = {
										  //title: 'Volume Size',
										  xaxis: {
											title: 'Volume Size',
											titlefont: {
											  family: 'Courier New, monospace',
											  size: 18,
											  color: '#7f7f7f'
											}
										  },
										  yaxis: {
											title: 'Volume Count',
											titlefont: {
											  family: 'Courier New, monospace',
											  size: 18,
											  color: '#7f7f7f'
											}
										  },
											width: 450,  // or any new width
											height: 450
										};
								

							Plotly.newPlot('myDiv', usdata, layout,{displayModeBar: false});
							Plotly.newPlot('myDiv1', eudata, layout,{displayModeBar: false});
							Plotly.newPlot('myDiv2', sgdata, layout,{displayModeBar: false});

				  
						</script>


						</body>

						</html>""")
	html_file_handle.close()
	
	

Write_html_headder()

for reg in regions:
	if reg != "us-east-1":
		html_file_handle = open(html_out_file, "a")
		html_file_handle.write("<td>")
		html_file_handle.close()
		Write_html_body(reg)
	elif reg == "us-east-1":
		Write_html_body(reg)

Write_html_footer()