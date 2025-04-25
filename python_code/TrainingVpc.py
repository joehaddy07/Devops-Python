import boto3

# Initialize the EC2 client
ec2_client = boto3.client('ec2')

# Step 1: Create VPC
# 1. Creates a VPC with a specified CIDR block.
# A Virtual Private Cloud (VPC) is a virtual network dedicated to your AWS account.
def create_vpc(cidr_block):
     # Use the create_vpc method to create a VPC
    # The CidrBlock parameter specifies the IP range for the VPC. Here it is set to '10.0.0.0/16'.
    vpc_response = ec2_client.create_vpc(CidrBlock=cidr_block)
     # Extract the VpcId from the response
    vpc_id = vpc_response['Vpc']['VpcId']
      # Print a message indicating the successful creation of the VPC
    print(f'VPC created with ID: {vpc_id}')
    return vpc_id

# Step 2: Create Internet Gateway
#Creates an internet gateway and attaches it to the VPC.
def create_internet_gateway(vpc_id):
    # Use the create_internet_gateway method to create an internet gateway
    internet_gateway_response = ec2_client.create_internet_gateway()
    # Extract the Internet Gateway ID from the response
    internet_gateway_id = internet_gateway_response['InternetGateway']['InternetGatewayId']
    # Print the ID of the created Internet Gateway
    print(f'Internet Gateway created with ID: {internet_gateway_id}')

    # Step 3: Attach the internet gateway to the VPC
    ec2_client.attach_internet_gateway(InternetGatewayId=internet_gateway_id, VpcId=vpc_id)

    return internet_gateway_id

# Step 3: Create Route Tables
# Creates both public and private route tables associated with the VPC.
def create_route_table(vpc_id):
    # Public Route Table
    public_route_table = ec2_client.create_route_table(VpcId=vpc_id)
    public_rt_id = public_route_table['RouteTable']['RouteTableId']
    print(f'Public Route Table {public_rt_id} created')

    # Private Route Table
    private_route_table = ec2_client.create_route_table(VpcId=vpc_id)
    private_rt_id = private_route_table['RouteTable']['RouteTableId']
    print(f'Private Route Table {private_rt_id} created')

    return public_rt_id, private_rt_id


# Step 4: Create Subnets
# Creates public and private subnets in different availability zones.
def create_subnet(vpc_id, public_rt_id, private_rt_id):
    # Public Subnets
    public_subnet1 = ec2_client.create_subnet(CidrBlock='10.0.1.0/24', VpcId=vpc_id, AvailabilityZone='us-east-1a')
    public_subnet2 = ec2_client.create_subnet(CidrBlock='10.0.2.0/24', VpcId=vpc_id, AvailabilityZone='us-east-1b')

    print(f'Public Subnets created')

    # Private Subnets
    private_subnet1 = ec2_client.create_subnet(CidrBlock='10.0.3.0/24', VpcId=vpc_id, AvailabilityZone='us-east-1a')
    private_subnet2 = ec2_client.create_subnet(CidrBlock='10.0.4.0/24', VpcId=vpc_id, AvailabilityZone='us-east-1b')
    private_subnet3 = ec2_client.create_subnet(CidrBlock='10.0.5.0/24', VpcId=vpc_id, AvailabilityZone='us-east-1a')
    private_subnet4 = ec2_client.create_subnet(CidrBlock='10.0.6.0/24', VpcId=vpc_id, AvailabilityZone='us-east-1b')

    print(f'Private Subnets created')

    return public_subnet1['Subnet']['SubnetId'], public_subnet2['Subnet']['SubnetId'], private_subnet1['Subnet']['SubnetId'], private_subnet2['Subnet']['SubnetId'], private_subnet3['Subnet']['SubnetId'], private_subnet4['Subnet']['SubnetId']


# Step 5: Associate Route Tables with Subnets
# Associates the route tables with their respective subnets.
def associate_with_subnet(public_subnet1_id, public_subnet2_id, private_subnet1_id, private_subnet2_id, private_subnet3_id, private_subnet4_id, public_rt_id, private_rt_id):
    # Associate the public route table with the public subnets
    ec2_client.associate_route_table(SubnetId=public_subnet1_id, RouteTableId=public_rt_id)
    ec2_client.associate_route_table(SubnetId=public_subnet2_id, RouteTableId=public_rt_id)

    # Associate the private route table with the private subnets
    ec2_client.associate_route_table(SubnetId=private_subnet1_id, RouteTableId=private_rt_id)
    ec2_client.associate_route_table(SubnetId=private_subnet2_id, RouteTableId=private_rt_id)
    ec2_client.associate_route_table(SubnetId=private_subnet3_id, RouteTableId=private_rt_id)
    ec2_client.associate_route_table(SubnetId=private_subnet4_id, RouteTableId=private_rt_id)

    # Print a message indicating that route tables are associated with subnets
    print('Route Tables associated with Subnets')

# Step 6: Create NAT Gateway
# Creates a NAT gateway in the public subnet and associates it with an Elastic IP.
def create_nat_gateway(public_subnet1_id, eip_id):
    # Use the `create_nat_gateway` method of the EC2 client to create a NAT Gateway
    response = ec2_client.create_nat_gateway(AllocationId=eip_id, SubnetId=public_subnet1_id)
    # Extract the NAT Gateway ID from the response
    nat_gateway_id = response['NatGateway']['NatGatewayId']
     # Print a message indicating the successful creation of the NAT Gateway
    print(f'NAT Gateway {nat_gateway_id} created')
    return nat_gateway_id

# Step 7: Create Elastic IP
# Allocates an Elastic IP address.
def create_eip():
     # Use the allocate_address method to allocate a new Elastic IP address.
    response = ec2_client.allocate_address(Domain='vpc')
    # Extract the AllocationId from the response, which is a unique identifier for the Elastic IP address.
    eip_id = response['AllocationId']
     # Print a message indicating that the Elastic IP address has been created.
    print(f'Elastic IP {eip_id} created')
    return eip_id

# Main Function
# Calls each of the above functions in sequence to set up the entire VPC infrastructure.
def main():
    # Step 1
    vpc_id = create_vpc('10.0.0.0/16')

    # Step 2
    public_rt_id, private_rt_id = create_route_table(vpc_id)

    # Step 3
    igw_id = create_internet_gateway(vpc_id)

    # Step 4
    public_subnet1_id, public_subnet2_id, private_subnet1_id, private_subnet2_id, private_subnet3_id, private_subnet4_id = create_subnet(vpc_id, public_rt_id, private_rt_id)

    # Step 5
    associate_with_subnet(public_subnet1_id, public_subnet2_id, private_subnet1_id, private_subnet2_id, private_subnet3_id, private_subnet4_id, public_rt_id, private_rt_id)

    # Step 6
    eip_id = create_eip()

    # Step 7
    nat_gateway_id = create_nat_gateway(public_subnet1_id, eip_id)

    # Step 8
    ec2_client.associate_address(AllocationId=eip_id, NatGatewayId=nat_gateway_id)

    print('AWS VPC Setup Complete')
# Calls the main function when the script is executed.
if __name__ == '__main__':
    main()
