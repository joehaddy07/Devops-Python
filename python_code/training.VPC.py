import boto3

def create_instances(ImageId, InstanceType, SecurityGroupIds, KeyName, MaxCount=1, MinCount=1):
    # Create an EC2 resource
    ec2 = boto3.resource('ec2')

    # Launch instances
    response = ec2.create_instances(
        ImageId=ImageId,
        InstanceType=InstanceType,
        SecurityGroupIds=SecurityGroupIds,
        KeyName=KeyName,
        MaxCount=MaxCount,
        MinCount=MinCount
    )

    # Get the instance ID from the response
    #instance_id = response[0].id: The response is a list of instances (even if you are creating only one instance). 
    #The [0] indexes into this list to get the details of the first (and only) instance created. 
    #The id attribute is then accessed to retrieve the unique identifier (instance ID) of the created instance.
    instance_id = response[0].id
    print(f"Instance ID already created: {instance_id}")

    # Check if the instance already exists
    filter = [{'Name': 'instance-id', 'Values': [instance_id]}]
    existing_instances = list(ec2.instances.filter(Filters=filter))

    if existing_instances:
        print("Instance already exists")
    else:
        print("Instance does not exist")

    # Create tags for the instance
    ec2.create_tags(Resources=[instance_id], Tags=[{'Key': 'Name', 'Value': 'MyInstance'}])

# Example usage:
ImageId = 'ami-xxxxxxxxxxxxxxxxx'  # Replace with your AMI ID
InstanceType = 't2.micro'
SecurityGroupIds = ['sg-xxxxxxxxxxxxxxxxx']  # Replace with your security group ID
KeyName = 'your-key-pair-name'  # Replace with your key pair name

# Call the function with the required parameters
create_instances(ImageId, InstanceType, SecurityGroupIds, KeyName)
