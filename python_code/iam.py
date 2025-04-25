import boto3

# Create an IAM client
client = boto3.client('iam')

# Define a function named create_group that takes a group name as a parameter.
def create_group(DevopsAdmins):
    # Create an IAM group using the create_group method of the IAM client.
    # The method requires the 'GroupName' parameter, which is set to the provided 'DevopsAdmins'.
    iam_response = client.create_group(GroupName=DevopsAdmins)

    # Extract the GroupId from the response to identify the created IAM group.
    group_id = iam_response['Group']['GroupId']

    # Print a message indicating the successful creation of the IAM group.
    print(f"Creating group: {group_id}")



# Create a user
# Define a function named create_user that takes a parameter UserName
def create_user(Sammy):
    # Use the IAM client to create a new IAM user with the specified username
    user_response = client.create_user(UserName=Sammy)

    # Extract the UserId from the response, assuming it is available in the 'UserId' key
    user_id = user_response['User']['UserId']

    # Print a message indicating that the user creation was successful, along with the user's ID
    print(f"Creating user: {user_id}")


def add_user_to_group(DevopsAdmin, Sammy):
   add_response = client.add_user_to_group(GroupName=DevopsAdmin, UserName=Sammy)
   add_user_to_group_id = add_response['Group']['User']['Add_user_to_group_id']
   print(f"add user to group: {add_user_to_group_id}")


def add_user_to_group(DevopsAdmin, Sammy, client):
    
        # Assuming the 'add_user_to_group' method is correct, but you may need to adjust it based on the actual API client you are using.
        add_response = client.add_user_to_group(GroupName=DevopsAdmin, UserName=Sammy)

        # Assuming the response structure contains 'Group' and 'User', and 'Add_user_to_group_id' is nested within them.
        add_user_to_group_id = add_response['Group']['User']['Add_user_to_group_id']
        print(f"add user: {add_user_to_group_id}")





