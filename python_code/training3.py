import boto3
ec2 = boto3.client('ec2', region_name='us-east-1')

#Data input
ec2_list=ec2.describe_instances(InstanceIds=[])
ec2_1= ec2_list['Reservations'][0]['Instances'][0]['InstanceId']
ec2_2= ec2_list['Reservations'][0]['Instances'][1]['InstanceId']
ec2_3= ec2_list['Reservations'][0]['Instances'][2]['InstanceId']



#Bussiness logic
ec2.stop_instances(InstanceIds=[ ec2_1 ])
ec2.stop_instances(InstanceIds=[ ec2_2 ])
ec2.stop_instances(InstanceIds=[ ec2_3 ])



   