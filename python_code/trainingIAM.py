import boto3

def create_group(GroupName):
    client = boto3.client('iam')

    list_response = client.list_groups()
    existing_groups = [group['GroupName'] for group in list_response['Groups']]
    if GroupName not in existing_groups:
        client.create_group(GroupName=GroupName)
        print(f"Group '{GroupName}' created successfully")
    else:
        print(f"Group '{GroupName}' already exists")

    create_group('DevopsAdmin')

def create_user(UserName):
    client = boto3.client('iam')

    list_response = client.list_users()
    existing_users = [user['UserName'] for user in list_response['users']]
    if UserName not in existing_users:
        client.create_user(UserName=UserName)
        print(f"user'{UserName}' created successfully")
    else:
        print(f"user '{UserName}' already exists")
    create_user('sammy')



def add_user_to_group(GroupName, UserName):
    client = boto3.client('iam')
    # Use the add_user_to_group API directly
    add_response = client.add_user_to_group(GroupName=GroupName, UserName=UserName)
    # You can print or return any relevant information from the response
    print(f"User {UserName} added to group {GroupName}")
    # Example usage
    add_user_to_group('DevopsAdmin', 'sammy')






