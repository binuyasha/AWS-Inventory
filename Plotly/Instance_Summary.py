#Instance Summary Plotly

import boto3
import collections
import datetime
import csv
from time import gmtime, strftime

date_fmt = strftime("%Y_%m_%d", gmtime())
regions=['us-east-1', 'eu-west-1', 'ap-southeast-1']
account = 'IOPreview'
html_out_file = "Instance_html_Summary_With_Plotly_Chart_3.html"



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
		az1 = 'us-east-1b'
		az2 = 'us-east-1c'
		az3 = 'us-east-1d'
		data = 'usdata'
	elif reg == 'eu-west-1':
		az1 = 'eu-west-1a'
		az2 = 'eu-west-1b'
		az3 = 'eu-west-1c'
		data = 'eudata'
	elif reg == 'ap-southeast-1':
		az1 = 'ap-southeast-1a'
		az2 = 'ap-southeast-1b'
		az3 = 'NA'
		data = 'sgdata'
	
	reg,InstanceStateOn, InstanceStateOff, az1_count, az2_count, az3_count, WindowsOS, OtherOS, General_Purpose, Compute_Optimised, Memory_Optimized, Storage_Optimized, Accelerated_Computing, GPU_Optimized, Bare_Metal, Micro = Instance_summary(reg)
	html_file_handle=open(html_out_file, "a")
	html_file_handle.write("""<table border="0" style="height: 264px; width: 0%; border-collapse: collapse; border-style: hidden; margin-left: auto; margin-right: auto;" height="97">
				<tbody>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 22px;"><strong>AZ1</strong>("""+az1+"""):</td>
				<td style="width: 5%; height: 22px;"><strong style="color: #06f968;">"""+str(az1_count)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;"><strong>AZ2</strong> ("""+az2+"""):</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(az2_count)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;"><strong>AZ3</strong> ("""+az3+"""):</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(az3_count)+"""</strong></td>
				</tr>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 21px;">Windows Instances:</td>
				<td style="width: 5%; height: 21px;"><strong style="color: #06f968;">"""+str(WindowsOS)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Other OS Instances:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(OtherOS)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">General_Purpose:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(General_Purpose)+"""</strong></td>
				</tr>
				<tr style="height: 21px;">
				<td style="width: 21.6946%; height: 21px;">Compute_Optimised:</td>
				<td style="width: 5%; height: 21px;"><strong style="color: #06f968;">"""+str(Compute_Optimised)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Memory_Optimized:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(Memory_Optimized)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Storage_Optimized:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(Storage_Optimized)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Accelerated_Computing:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(Accelerated_Computing)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Micro:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(Micro)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">GPU_Optimized:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(GPU_Optimized)+"""</strong></td>
				</tr>
				<tr style="height: 20px;">
				<td style="width: 21.6946%; height: 20px;">Bare_Metal:</td>
				<td style="width: 5%; height: 20px;"><strong style="color: #06f968;">"""+str(Bare_Metal)+"""</strong></td>
				</tr>
				</tbody>
				</table>
				</td>
						<script>

									var """+str(data)+""" = [{
									y: ["""+str(az1_count)+""","""+str(az2_count)+""","""+str(az3_count)+"""],
									x: ['AZ1', 'AZ2', 'AZ3'],
									type: 'bar'
										}];
						</script>
				""")
	html_file_handle.close()
	
	
def Instance_summary(reg):
	
	
	if reg == 'us-east-1':
		az1 = 'us-east-1b'
		az2 = 'us-east-1c'
		az3 = 'us-east-1d'
	elif reg == 'eu-west-1':
		az1 = 'eu-west-1a'
		az2 = 'eu-west-1b'
		az3 = 'eu-west-1c'
	elif reg == 'ap-southeast-1':
		az1 = 'ap-southeast-1a'
		az2 = 'ap-southeast-1b'
		az3 = 'NA'
	
	
	az1_count = 0
	az2_count = 0
	az3_count = 0
	
	InstanceStateOn = 0
	InstanceStateOff = 0
	WindowsOS = 0
	OtherOS = 0
	General_Purpose = 0
	Compute_Optimised = 0
	Memory_Optimized = 0
	Storage_Optimized = 0
	Accelerated_Computing = 0
	GPU_Optimized = 0
	Bare_Metal = 0
	Micro = 0
	  
	  
	

	ec2con = boto3.client('ec2',region_name=reg)


	reservations = ec2con.describe_instances().get('Reservations',[])
	instances = sum(
		[
			[i for i in r['Instances']]
			for r in reservations
		], [])
	instanceslist = len(instances)


	
	General_Purpose_List = ["t2.nano","t2.micro","t2.small","t2.medium","t2.large","t2.xlarge","t2.2xlarge","t3.nano","t3.micro","t3.small","t3.medium","t3.large","t3.xlarge","t3.2xlarge","m4.large","m4.xlarge","m4.2xlarge","m4.4xlarge","m4.10xlarge","m4.16xlarge","m5.large","m5.xlarge","m5.2xlarge","m5.4xlarge","m5.12xlarge","m5.24xlarge","m5d.large","m5d.xlarge","m5d.2xlarge","m5d.4xlarge","m5d.12xlarge","m5d.24xlarge","m1.small "," m1.medium "," m1.large "," m1.xlarge "," m3.medium "," m3.large "," m3.xlarge "," m3.2xlarge"]

	Compute_Optimised_List = ["c4.large "," c4.xlarge "," c4.2xlarge "," c4.4xlarge "," c4.8xlarge "," c5.large "," c5.xlarge "," c5.2xlarge "," c5.4xlarge "," c5.9xlarge "," c5.18xlarge "," c5d.xlarge"," c5d.2xlarge "," c5d.4xlarge "," c5d.9xlarge "," c5d.18xlarge","c1.medium "," c1.xlarge "," cc2.8xlarge "," c3.large "," c3.xlarge "," c3.2xlarge "," c3.4xlarge "," c3.8xlarge"]

	Memory_Optimized_List = ["r4.large "," r4.xlarge "," r4.2xlarge "," r4.4xlarge "," r4.8xlarge "," r4.16xlarge "," r5.large "," r5.xlarge "," r5.2xlarge "," r5.4xlarge "," r5.12xlarge "," r5.24xlarge "," r5d.large "," r5d.xlarge "," r5d.2xlarge "," r5d.4xlarge "," r5d.12xlarge "," r5d.24xlarge "," x1.16xlarge "," x1.32xlarge "," x1e.xlarge "," x1e.2xlarge "," x1e.4xlarge "," x1e.8xlarge "," x1e.16xlarge "," x1e.32xlarge "," z1d.large "," z1d.xlarge "," z1d.2xlarge "," z1d.3xlarge "," z1d.6xlarge "," z1d.12xlarge","m2.xlarge "," m2.2xlarge "," m2.4xlarge "," cr1.8xlarge "," r3.large "," r3.xlarge "," r3.2xlarge "," r3.4xlarge "," r3.8xlarge"]

	Storage_Optimized_List = ["d2.xlarge "," d2.2xlarge "," d2.4xlarge "," d2.8xlarge "," h1.2xlarge "," h1.4xlarge "," h1.8xlarge "," h1.16xlarge "," i3.large "," i3.xlarge "," i3.2xlarge "," i3.4xlarge "," i3.8xlarge "," i3.16xlarge","hs1.8xlarge "," i2.xlarge "," i2.2xlarge "," i2.4xlarge "," i2.8xlarge",]

	Accelerated_Computing_List = ["f1.2xlarge "," f1.4xlarge "," f1.16xlarge "," g3s.xlarge "," g3.4xlarge "," g3.8xlarge "," g3.16xlarge "," p2.xlarge "," p2.8xlarge "," p2.16xlarge "," p3.2xlarge "," p3.8xlarge "," p3.16xlarge",]

	GPU_Optimized_List = ["g2.2xlarge","g2.8xlarge"]
	Bare_Metal_List = ["i3.metal"]
	Micro_List = ["t1.micro"]





	for instance in instances:
		InstanceState = instance['State']['Name']
		if InstanceState == 'running':
			InstanceStateOn +=1
		else:
			InstanceStateOff +=1
		InstanceType = instance['InstanceType']
		print(InstanceType)
		if (InstanceType in General_Purpose_List):
			General_Purpose = General_Purpose + 1
			
		elif (InstanceType in Compute_Optimised_List):
			Compute_Optimised =Compute_Optimised+1
			
		elif (InstanceType in Storage_Optimized_List):
			Storage_Optimized =Storage_Optimized+1
			
		elif (InstanceType in Memory_Optimized_List):
			Memory_Optimized =Memory_Optimized+1
		elif (InstanceType in Micro_List):
			Micro =Micro+1
			
		elif (InstanceType in Accelerated_Computing_List):
			Accelerated_Computing =Accelerated_Computing+1
		elif (InstanceType in GPU_Optimized_List):
			GPU_Optimized =GPU_Optimized+1
		elif (InstanceType in Bare_Metal_List):
			Bare_Metal =Bare_Metal+1
		
		
		
		InstanceAvailabilityZone = instance['Placement']['AvailabilityZone']
		if InstanceAvailabilityZone == az1:
			az1_count +=1
		elif InstanceAvailabilityZone == az2:
			az2_count +=1
		elif InstanceAvailabilityZone == az3:
			az3_count +=1
		
			
		try:
			tagscount = len(instance['Tags'])
		except:
			tagscount = 0
		temp = 0
		
		OSPlatform = ""	
		while temp < tagscount:
			if instance['Tags'][temp]['Key'] == 'OS':
				OSPlatform = instance['Tags'][temp]['Value']
			temp += 1
		
		if  OSPlatform == 'Windows':
			WindowsOS +=1
		else:
			OtherOS +=1
	print(General_Purpose)
	print(Compute_Optimised)
	print(Storage_Optimized)
	print(Micro)
	filepath ='IOPreview_'+reg+'_Instance_Summary_' + date_fmt + '.csv'
	filename ='IOPreview_'+reg+'_Instance_Summary_' + date_fmt + '.csv'

	csv_file = open(filepath,'w+')
	csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n"%("Region","InstanceStateOn"," InstanceStateOff","az1_count"," az2_count"," az3_count"," WindowsOS"," OtherOS"," General_Purpose"," Compute_Optimised"," Memory_Optimized"," Storage_Optimized"," Accelerated_Computing"," GPU_Optimized"," Bare_Metal"," Micro"))

	csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n"% (reg,InstanceStateOn, InstanceStateOff, az1_count, az2_count, az3_count, WindowsOS, OtherOS, General_Purpose, Compute_Optimised, Memory_Optimized, Storage_Optimized, Accelerated_Computing, GPU_Optimized, Bare_Metal, Micro))
	csv_file.flush()
	
	return reg,InstanceStateOn, InstanceStateOff, az1_count, az2_count, az3_count, WindowsOS, OtherOS, General_Purpose, Compute_Optimised, Memory_Optimized, Storage_Optimized, Accelerated_Computing, GPU_Optimized, Bare_Metal, Micro;
	
	
def Write_html_footer():
	html_file_handle = open(html_out_file, "a")
	html_file_handle.write("""
		</tr>
		</tbody>
		</table>
		</div>
	<script>
		var layout = {
										  //title: 'Instance Spread',
										  xaxis: {
											title: 'Availability Zones',
											titlefont: {
											  family: 'Courier New, monospace',
											  size: 18,
											  color: '#7f7f7f'
											}
										  },
										  yaxis: {
											title: 'Instance Count',
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