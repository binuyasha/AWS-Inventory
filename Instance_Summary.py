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
	
Instance_summary()