#Instance Summary

import boto3
import collections
import datetime
import csv
from time import gmtime, strftime




def Instance_summary():
	date_fmt = strftime("%Y_%m_%d", gmtime())

	InstanceStateOn = 0
	InstanceStateOff = 0
	us_east_1a = 0
	us_east_1b = 0
	us_east_1c = 0
	us_east_1d = 0
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
	  
	reg='us-east-1'

	ec2con = boto3.client('ec2',region_name=reg)


	reservations = ec2con.describe_instances().get('Reservations',[])
	instances = sum(
		[
			[i for i in r['Instances']]
			for r in reservations
		], [])
	instanceslist = len(instances)


	#csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s \n"%('Running_Instance','Stopped_Instance','eu-west-1a','eu-west-1b','eu-west-1c','Total_instance','Windows_Instances','Other_Os_Instances'))

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
		if (InstanceType in General_Purpose_List):
			General_Purpose =+1
		elif (InstanceType in Compute_Optimised_List):
			Compute_Optimised=+1
		elif (InstanceType in Storage_Optimized_List):
			Storage_Optimized=+1
		elif (InstanceType in Memory_Optimized_List):
			Memory_Optimized =+1
		elif (InstanceType in Micro_List):
			Micro =+1
		elif (InstanceType in Accelerated_Computing_List):
			Accelerated_Computing =+1
		elif (InstanceType in GPU_Optimized_List):
			GPU_Optimized =+1
		elif (InstanceType in Bare_Metal_List):
			Bare_Metal =+1
		
		
		
		InstanceAvailabilityZone = instance['Placement']['AvailabilityZone']
		if InstanceAvailabilityZone == 'us-east-1a':
			us_east_1a +=1
		elif InstanceAvailabilityZone == 'us-east-1b':
			us_east_1b +=1
		elif InstanceAvailabilityZone == 'us-east-1c':
			us_east_1c +=1
		elif InstanceAvailabilityZone == 'us-east-1d':
			us_east_1d +=1
			
		try:
			tagscount = len(instance['Tags'])
		except:
			tagscount = 0
		temp = 0
			
		while temp < tagscount:
			if instance['Tags'][temp]['Key'] == 'OS':
				OSPlatform = instance['Tags'][temp]['Value']
			temp += 1
		
		if  OSPlatform == 'Windows':
			WindowsOS +=1
		else:
			OtherOS +=1

	filepath ='C:/Users/kwfp376/Documents/Temp/Webpage/IOPreview_files/IOPreview_N.Virginia_Instance_Summary_' + date_fmt + '.csv'
	filename ='IOPreview_N.Virginia_Instance_Summary_' + date_fmt + '.csv'

	csv_file = open(filepath,'w+')
	csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n"%("InstanceStateOn"," InstanceStateOff"," us_east_1a"," us_east_1b"," us_east_1c"," us_east_1d"," WindowsOS"," OtherOS"," General_Purpose"," Compute_Optimised"," Memory_Optimized"," Storage_Optimized"," Accelerated_Computing"," GPU_Optimized"," Bare_Metal"," Micro"))

	csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n"% (InstanceStateOn, InstanceStateOff, us_east_1a, us_east_1b, us_east_1c, us_east_1d, WindowsOS, OtherOS, General_Purpose, Compute_Optimised, Memory_Optimized, Storage_Optimized, Accelerated_Computing, GPU_Optimized, Bare_Metal, Micro))
	csv_file.flush()
	
	html_out_file = "C:/Users/kwfp376/Documents/Temp/Webpage/html/Instance_html_Summary_With_Chart.html"
	html_file_handle = open(html_out_file, "w")
	html_file_handle.write("""<!doctype html>
		<html>

		<head>
		<script src = "../Lib/Chart.bundle.min.js"></script>
		<link rel = "stylesheet" href = "../Lib/bootstrap.min.css">
		</head>
		
		<body>
		<style>
		hr { 
				display: block;
				margin-top: 0.5em;
				margin-bottom: 0.5em;
				margin-left: auto;
				margin-right: auto;
				border-style: inset;
				border-width: 2px;
			}
		
		</style>

			<div style = "background-color:lightblue; Width:100%; Height:100%; align:center">
				<div class="container" >
					<canvas id="myChart" ></canvas>
				</div>
			</div>
			<div>
				<div>
					<p></p>
					<p></p>
					<hr />
					<h2 style="text-align: center;"><strong>US Instance details</strong></h2>
					<hr />
					<p></p>
					<table border="0" style="height: 129px; width: 100.983%; border-collapse: collapse; border-style: hidden; margin-left: auto; margin-right: auto; float: center" height="97">
					<tbody>
					<tr style="height: 21px;">
					<td style="width: 21.6946%; height: 21px;"><strong>AZ1</strong> (us-east-1a): </td>
					<td style="width: 5%; height: 21px;"><strong style = "color:#06F968;">"""+str(us_east_1a)+"""</strong></td>
					<td style="width: 20.7169%; height: 21px;"><strong>AZ2</strong> (us-east-1b):</td>
					<td style="width: 5%; height: 21px;"> <strong style = "color:#06F968;">"""+str(us_east_1b)+"""</strong></td>
					<td style="width: 17.365%; height: 21px;"><strong>AZ3</strong> (us-east-1c):</td>
					<td style="width: 5%; height: 21px;"> <strong style = "color:#06F968;">"""+str(us_east_1c)+"""</strong></td>
					</tr>
					<tr style="height: 21px;">
					<td style="width: 21.6946%; height: 21px;">Windows Instances:</td>
					<td style="width: 11.6388%; height: 21px;"> <strong style = "color:#06F968;">"""+str(WindowsOS)+"""</strong></td>
					<td style="width: 20.7169%; height: 21px;">Other OS Instances: </td>
					<td style="width: 12.6165%; height: 21px;"><strong style = "color:#06F968;">"""+str(OtherOS)+"""</strong></td>
					<td style="width: 17.365%; height: 21px;">General_Purpose: </td>
					<td style="width: 15.9684%; height: 21px;"><strong style = "color:#06F968;">"""+str(General_Purpose)+"""</strong></td>
					</tr>
					<tr style="height: 21px;">
					<td style="width: 21.6946%; height: 21px;">Compute_Optimised: </td>
					<td style="width: 11.6388%; height: 21px;"><strong style = "color:#06F968;">"""+str(Compute_Optimised)+"""</strong></td>
					<td style="width: 20.7169%; height: 21px;">Memory_Optimized: </td>
					<td style="width: 12.6165%; height: 21px;"><strong style = "color:#06F968;">"""+str(Memory_Optimized)+"""</strong></td>
					<td style="width: 17.365%; height: 21px;">Storage_Optimized: </td>
					<td style="width: 15.9684%; height: 21px;"><strong style = "color:#06F968;">"""+str(Storage_Optimized)+"""</strong></td>
					</tr>
					<tr style="height: 20px;">
					<td style="width: 21.6946%; height: 20px;">Accelerated_Computing: </td>
					<td style="width: 11.6388%; height: 20px;"><strong style = "color:#06F968;">"""+str(Accelerated_Computing)+"""</strong></td>
					<td style="width: 20.7169%; height: 20px;">GPU_Optimized: </td>
					<td style="width: 12.6165%; height: 20px;"><strong style = "color:#06F968;">"""+str(GPU_Optimized)+"""</strong></td>
					<td style="width: 17.365%; height: 20px;">Bare_Metal: </td>
					<td style="width: 15.9684%; height: 20px;"><strong style = "color:#06F968;">"""+str(Bare_Metal)+"""</strong></td>
					</tr>
					<tr style="height: 20px;">
					<td style="width: 21.6946%; height: 20px;">Micro: </td>
					<td style="width: 11.6388%; height: 20px;"><strong style = "color:#06F968;">"""+str(Micro)+"""</strong></td>
					</tr>
					
					</tbody>
					</table>
					
				</div>
			</div>


		<script>


		var myChart = document.getElementById('myChart').getContext('2d');
		Chart.defaults.global.defaultFontFamily = 'Lato';
		Chart.defaults.global.defaultFontSize = '18';
		Chart.defaults.global.defaultFontColor = '#7777';

		var Chart = new Chart(myChart,{
			type: 'pie',
			data: {
				labels: ["us-east-1a", "us-east-1b", "us-east-1c"],
				datasets: [{
					fillColor: "#79D1CF",
					strokeColor: "#79D1CF",
					label: 'Instance Count',
					data: ["""+str(us_east_1a)+""","""+str(us_east_1b)+""","""+str(us_east_1c)+"""],
					
					backgroundColor: [
						'rgba(255,99,132,1)',
						'rgba(54, 162, 235, 1)',
						'rgba(255, 206, 86, 1)',
						
					],
					borderColor: [
						'rgba(255,99,132,1)',
						'rgba(54, 162, 235, 1)',
						'rgba(255, 206, 86, 1)',
						
					],
					borderWidth: 2,
					borderColor: '#777',
					hoverBorderWidth:3,
					hoverBorderColor: '#000'
			
				}]
			},
			options: {
				//responsive: true,
				//maintainAspectRatio: true,
				//showDatapoints: true,
				title:
					{
					display:true,
					text:'Instance Spread',
					fontSize: 25,
					},
				legend:
					{
					position: 'right',
					labels:
						{
							fontColor: '#000'
						}
					},
				layout:
					{
						padding:
							{
								left:0,
								right:50,
								bottom:0,
								top:0
							}
					},
				tooltips:
					{
						enabled:true,
						bodyFontSize: 15,
						titleFontSize:30
						
					},
					
				/*
				scales: 
					{
					yAxes: [
						{
						gridLines: 
							{
								display: true
							},
						ticks: 
							{
							beginAtZero:false
							}
						}
						]
					}
				*/
					}
				});
		</script>


		</body>

		</html>""")

Instance_summary()