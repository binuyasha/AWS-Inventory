#Instance Summary Plotly

import boto3
import collections
import datetime
import csv
from time import gmtime, strftime

date_fmt = strftime("%Y_%m_%d", gmtime())

sts = boto3.client('sts')
identity = sts.get_caller_identity()
ownerId = identity['Account']

regions=['us-east-1', 'eu-west-1', 'ap-southeast-1']
account = 'IOPreview'
html_out_file = "Snapshot_AMI_html_Summary_With_Chart.html"



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
				<td style="width: 50%;text-align: center;"><strong>Snapshot</strong></td>
				<td style="width: 50%;text-align: center;"><strong>AMI</strong></td>
				</tr>
				<tr>
				<td style="width: 50%;"> <div id="myDiv"><!-- Plotly chart will be drawn inside this DIV --></div></td>
				<td style="width: 50%;"><div id="myDiv1"><!-- Plotly chart will be drawn inside this DIV --></div></td>
				</tr>
				
				<tr style="height: 20px;">
				<td style="width: 50%; height: 20px;">
				<div id="myDiv"></div>
				</td>
				<td style="width: 50%; height: 20px;">
				<div id="myDiv1"></div>
				</td>
				</tr>
				<tr style="height: 17px;">
				<td style="width: 50%; height: 25px; text-align: center;">
				<div id="myDiv"><hr /><strong><strong>Snapshot</strong></strong><hr /></div>
				</td>
				<td style="width: 50%; height: 25px; text-align: center;">
				<div id="myDiv1"><hr /><strong><strong>AMI</strong></strong><hr /></div>
				</td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 50%; height: 20px;">
				""")
	html_file_handle.close()

def Write_html_body():

	for reg in regions:
		if reg == 'us-east-1':
			US = {}
			US['reg'],US['Snapshot_Count'],US['AMI_Snapshot_Count'],US['Other_Ami_count'],US['Windows_Ami_count'],US['CPM_Ami_Count'],US['AMI_Total_Count']= Snapshot_AMI_summary(reg)
		elif reg == 'eu-west-1':
			IR = {}
			IR['reg'],IR['Snapshot_Count'],IR['AMI_Snapshot_Count'],IR['Other_Ami_count'],IR['Windows_Ami_count'],IR['CPM_Ami_Count'],IR['AMI_Total_Count']= Snapshot_AMI_summary(reg)
		elif reg == 'ap-southeast-1':
			SG = {}
			SG['reg'],SG['Snapshot_Count'],SG['AMI_Snapshot_Count'],SG['Other_Ami_count'],SG['Windows_Ami_count'],SG['CPM_Ami_Count'],SG['AMI_Total_Count']= Snapshot_AMI_summary(reg)
	
	
	html_file_handle=open(html_out_file, "a")
	html_file_handle.write("""<table border="0" style="height: 264px; width: 0%; border-collapse: collapse; border-style: hidden; margin-left: auto; margin-right: auto;" height="97">
				<tbody>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"><strong>US</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Snapshots_registered_to_AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(US['AMI_Snapshot_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Total Snapshots:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(US['Snapshot_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"></td>
				</tr>
				
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 21px;"><strong>Ireland</strong></td>
				</tr>
				
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Snapshots_registered_to_AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(IR['AMI_Snapshot_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Total Snapshots:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(IR['Snapshot_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"></td>
				</tr>
				
				
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"><strong>Singapore</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Snapshots_registered_to_AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(SG['AMI_Snapshot_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Total Snapshots:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(SG['Snapshot_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"></td>
				</tr>
				
				
				</tbody>
				</table>
				</td>
				<td>
				
				
				<table border="0" style="height: 264px; width: 0%; border-collapse: collapse; border-style: hidden; margin-left: auto; margin-right: auto;" height="97">
				<tbody>
				
				
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"><strong>US</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Windows_OS_AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(US['Windows_Ami_count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Other_OS_AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(US['Other_Ami_count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">CPM Backup AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(US['CPM_Ami_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Total AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(US['AMI_Total_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"></td>
				</tr>
				
				
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 21px;"><strong>Ireland</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Windows_OS_AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(IR['Windows_Ami_count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Other_OS_AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(IR['Other_Ami_count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">CPM Backup AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(IR['CPM_Ami_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Total AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(IR['AMI_Total_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"></td>
				</tr>
				
				
				
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"><strong>Singapore</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Windows_OS_AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(SG['Windows_Ami_count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Other_OS_AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(SG['Other_Ami_count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">CPM Backup AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(SG['CPM_Ami_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Total AMI:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(SG['AMI_Total_Count'])+"""</strong></td>
				</tr>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"></td>
				</tr>
				
				
				</tbody>
				</table>
				</td>
				
						<script>

									var Snapshot_Data = [{
									values: ["""+str(US['Snapshot_Count'])+""","""+str(IR['Snapshot_Count'])+""","""+str(SG['Snapshot_Count'])+"""],
									labels: ['US', 'Ireland', 'Singapore'],
									type: 'pie'
										}];
									
									var AMI_Data = [{
									values: ["""+str(US['AMI_Total_Count'])+""","""+str(IR['AMI_Total_Count'])+""","""+str(SG['AMI_Total_Count'])+"""],
									labels: ['US', 'Ireland', 'Singapore'],
									type: 'pie'
										}];
						</script>
				""")
	html_file_handle.close()
	
	
def Snapshot_AMI_summary(reg):
	Snapshot_Count = 0
	AMI_Snapshot_Count = 0
	Other_Ami_count = 0
	Windows_Ami_count = 0
	CPM_Ami_Count = 0
	AMI_Total_Count = 0
	
	ec2con = boto3.client('ec2',region_name=reg)
	ec2snapshot = ec2con.describe_snapshots(OwnerIds=[
		ownerId,
	],).get('Snapshots',[])
	Snapshot_Count = len(ec2snapshot)
		
	if Snapshot_Count > 0:
		for snapshots in ec2snapshot:
			Description=snapshots['Description']
			if Description.find("CreateImage") == 0:
				AMI_Snapshot_Count = AMI_Snapshot_Count + 1
	
	filter = [{'Name' : 'owner-id', 'Values': [ownerId]}]
	images = ec2con.describe_images(Filters = filter)
	
	ami_list = images['Images']
	AMI_Total_Count = len(ami_list)
	
	for ami in ami_list:
		if 'Platform' in ami:
			if (ami['Platform']) == 'windows':
				Windows_Ami_count = Windows_Ami_count + 1
		Other_Ami_count = Other_Ami_count + 1
		
		if ami['Description'].find("CPM")== 0 or ami['Description'].find("cpm") == 0:
			CPM_Ami_Count = CPM_Ami_Count + 1
		
	'''filepath ='IOPreview_'+reg+'_Snapshot_And_AMI_Summary_' + date_fmt + '.csv'
	filename ='IOPreview_'+reg+'_Snapshot_And_AMI_Summary_' + date_fmt + '.csv'

	csv_file = open(filepath,'w+')
	csv_file.write("%s,%s,%s,%s,%s,%s \n"%("Region","io1_count", "gp2_count", "st1_count","sc1_count", "In_Use_State", "Available_State", "Not_Encrypted_Count",	"Encrypted_Count", "Size_0_100", "Size_100_500", "Size_500_More"))

	csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n"% (reg,io1_count, gp2_count, st1_count,sc1_count, In_Use_State, Available_State, Not_Encrypted_Count,	Encrypted_Count, Size_0_100, Size_100_500, Size_500_More))
	csv_file.flush()
	'''
	return reg,Snapshot_Count,AMI_Snapshot_Count,Other_Ami_count,Windows_Ami_count,CPM_Ami_Count,AMI_Total_Count;	
	
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
										  /*xaxis: {
											title: 'Regions',
											titlefont: {
											  family: 'Courier New, monospace',
											  size: 18,
											  color: '#7f7f7f'
											}
										  },
										  yaxis: {
											title: 'Count',
											titlefont: {
											  family: 'Courier New, monospace',
											  size: 18,
											  color: '#7f7f7f'
											}
										  },
										  */
											width: 450,  // or any new width
											height: 450
										};
								

							Plotly.newPlot('myDiv', Snapshot_Data, layout,{displayModeBar: false});
							Plotly.newPlot('myDiv1', AMI_Data, layout,{displayModeBar: false});
							

				  
						</script>


						</body>

						</html>""")
	html_file_handle.close()
	
	

Write_html_headder()
Write_html_body()
Write_html_footer()