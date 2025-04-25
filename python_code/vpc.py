import boto3

# Specify your AWS credentials and region
aws_access_key_id = 'your_access_key'
aws_secret_access_key = 'your_secret_key'
region_name = 'your_region'

# Create a VPC
def create_vpc():
    ec2 = boto3.resource('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc.create_tags(Tags=[{"Key": "Name", "Value": "MyVPC"}])
    vpc.wait_until_available()
    
    return vpc

# Create a route table
def create_route_table(vpc_id):
    ec2 = boto3.resource('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    # Create public route table
    public_route_table = ec2.create_route_table(VpcId=vpc_id)
    
    # Create private route table 1
    private_route_table_1 = ec2.create_route_table(VpcId=vpc_id)
    
    # Create private route table 2
    private_route_table_2 = ec2.create_route_table(VpcId=vpc_id)

    return public_route_table, private_route_table_1, private_route_table_2

# Create an Internet Gateway
def create_internet_gateway(vpc):
    ec2 = boto3.resource('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    internet_gateway = ec2.create_internet_gateway()
    vpc.attach_internet_gateway(InternetGatewayId=internet_gateway.id)

    return internet_gateway

# Create subnets
def create_subnets(vpc, public_route_table, private_route_table_1, private_route_table_2):
    ec2 = boto3.resource('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    # Create public subnets
    public_subnet_1 = ec2.create_subnet(CidrBlock='10.0.1.0/24', VpcId=vpc.id, AvailabilityZone='us-east-1a')
    public_subnet_2 = ec2.create_subnet(CidrBlock='10.0.2.0/24', VpcId=vpc.id, AvailabilityZone='us-east-1b')
    
    # Associate public subnets with public route table
    public_route_table.associate_with_subnet(SubnetId=public_subnet_1.id)
    public_route_table.associate_with_subnet(SubnetId=public_subnet_2.id)

    # Create private subnets
    private_subnet_1 = ec2.create_subnet(CidrBlock='10.0.3.0/24', VpcId=vpc.id, AvailabilityZone='us-east-1a')
    private_subnet_2 = ec2.create_subnet(CidrBlock='10.0.4.0/24', VpcId=vpc.id, AvailabilityZone='us-east-1b')
    private_subnet_3 = ec2.create_subnet(CidrBlock='10.0.5.0/24', VpcId=vpc.id, AvailabilityZone='us-east-1a')
    private_subnet_4 = ec2.create_subnet(CidrBlock='10.0.6.0/24', VpcId=vpc.id, AvailabilityZone='us-east-1b')

    # Associate private subnets with private route tables
    private_route_table_1.associate_with_subnet(SubnetId=private_subnet_1.id)
    private_route_table_1.associate_with_subnet(SubnetId=private_subnet_2.id)
    
    private_route_table_2.associate_with_subnet(SubnetId=private_subnet_3.id)
    private_route_table_2.associate_with_subnet(SubnetId=private_subnet_4.id)

    return public_subnet_1, public_subnet_2, private_subnet_1, private_subnet_2, private_subnet_3, private_subnet_4

# Create a load balancer
def create_load_balancer(vpc, public_subnet_1):
    elbv2 = boto3.client('elbv2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    response = elbv2.create_load_balancer(
        Name='MyLoadBalancer',
        Subnets=[public_subnet_1.id],
        SecurityGroups=[],
        Scheme='internet-facing',
        Tags=[{'Key': 'Name', 'Value': 'MyLoadBalancer'}]
    )

    return response['LoadBalancers'][0]

# Create a NAT gateway
def create_nat_gateway(public_subnet, allocation_id):
    ec2 = boto3.resource('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    nat_gateway = ec2.create_nat_gateway(
        SubnetId=public_subnet.id,
        AllocationId=allocation_id
    )

    return nat_gateway

# Create an Elastic IP
def create_eip():
    ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    response = ec2.allocate_address(Domain='vpc')

    return response['AllocationId']

# Example usage
vpc = create_vpc()
public_route_table, private_route_table_1, private_route_table_2 = create_route_table(vpc.id)
internet_gateway = create_internet_gateway(vpc)
public_subnet_1, public_subnet_2, private_subnet_1, private_subnet_2, private_subnet_3, private_subnet_4 = create_subnets(vpc, public_route_table, private_route_table_1, private_route_table_2)
load_balancer = create_load_balancer(vpc, public_subnet_1)
nat_gateway = create_nat_gateway(public_subnet_1, create_eip())

