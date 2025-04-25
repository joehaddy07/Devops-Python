import boto3

ec2_client = boto3.client('ec2')

def delete_nat_gateway(nat_gateway_id):
    ec2_client.delete_nat_gateway(NatGatewayId=nat_gateway_id)
    print(f'NAT Gateway {nat_gateway_id} deleted')

def delete_eip(eip_allocation_id):
    ec2_client.release_address(AllocationId=eip_allocation_id)
    print(f'Elastic IP {eip_allocation_id} released')

def disassociate_route_tables(public_subnet1_id, public_subnet2_id, private_subnet1_id, private_subnet2_id, private_subnet3_id, private_subnet4_id):
    ec2_client.disassociate_route_table(AssociationId=public_subnet1_id)
    ec2_client.disassociate_route_table(AssociationId=public_subnet2_id)
    ec2_client.disassociate_route_table(AssociationId=private_subnet1_id)
    ec2_client.disassociate_route_table(AssociationId=private_subnet2_id)
    ec2_client.disassociate_route_table(AssociationId=private_subnet3_id)
    ec2_client.disassociate_route_table(AssociationId=private_subnet4_id)
    print('Route Tables disassociated from Subnets')

def delete_subnets(public_subnet1_id, public_subnet2_id, private_subnet1_id, private_subnet2_id, private_subnet3_id, private_subnet4_id):
    ec2_client.delete_subnet(SubnetId=public_subnet1_id)
    ec2_client.delete_subnet(SubnetId=public_subnet2_id)
    ec2_client.delete_subnet(SubnetId=private_subnet1_id)
    ec2_client.delete_subnet(SubnetId=private_subnet2_id)
    ec2_client.delete_subnet(SubnetId=private_subnet3_id)
    ec2_client.delete_subnet(SubnetId=private_subnet4_id)
    print('Subnets deleted')

def delete_route_tables(public_rt_id, private_rt_id):
    ec2_client.delete_route_table(RouteTableId=public_rt_id)
    ec2_client.delete_route_table(RouteTableId=private_rt_id)
    print('Route Tables deleted')

def detach_and_delete_igw(vpc_id, igw_id):
    ec2_client.detach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
    ec2_client.delete_internet_gateway(InternetGatewayId=igw_id)
    print(f'Internet Gateway {igw_id} detached and deleted')

def delete_vpc(vpc_id):
    ec2_client.delete_vpc(VpcId=vpc_id)
    print(f'VPC {vpc_id} deleted')





import boto3

def delete_bucket(bucket_name):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Delete all objects in the bucket
    response = s3.list_objects(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

    # Delete the bucket
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' deleted successfully.")

# Replace 'joe12dit' with your actual bucket name
delete_bucket('joe12dit')


import boto3

def delete_object(bucket_name, object_name):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Delete the object
    s3.delete_object(Bucket=bucket_name, Key=object_name)
    #print(f"Object '{object_name}' deleted from '{bucket_name}'.")

# Replace 'test' with your actual object name
#delete_object('joe12dit', 'test')


