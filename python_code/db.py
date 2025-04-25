import boto3
import time

def create_db_cluster():
    # Specify DB cluster details
    cluster_identifier = 'your_cluster_identifier'
    master_username = 'joe'
    master_password = 'password123'
    db_instance_identifier = 'your_db_instance_identifier'
    db_instance_class = 'db.t2.micro'
    region = 'your_region'  # Update with your desired AWS region

    # Create an RDS client
    rds_client = boto3.client('rds')  # Fix: Corrected the client instantiation

    # Check if the DB cluster already exists
    try:
        rds_client.describe_db_clusters(DBClusterIdentifier=cluster_identifier)
        print(f"DB cluster '{cluster_identifier}' already exists.")
    except rds_client.exceptions.DBClusterNotFoundFault:
        # If the cluster doesn't exist, create it
        response = rds_client.create_db_cluster(
            DBClusterIdentifier=cluster_identifier,
            MasterUsername=master_username,
            MasterUserPassword=master_password,
            Engine='aurora',
            EngineVersion='5.7.mysql_aurora.2.08.3',  # Fix: Added a comma at the end
            DatabaseName='',  # Fix: Added a value
            DBSubnetGroupName='your_subnet_group_name',  # Update with your subnet group name
            AvailabilityZones=[f'{region}a', f'{region}b'],  # Update with your desired AZs
            EngineMode='serverless',  # Update with your desired engine mode
            EnableHttpEndpoint=True,  # Fix: Corrected the parameter name
            ScalingConfiguration={
                'AutoPause': True,
                'MaxCapacity': 2,
                'MinCapacity': 1
            },
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'MyDBCluster'
                },
            ]
        )
        print(f"DB cluster '{cluster_identifier}' created successfully.")

        # Wait for the DB cluster to become available
        while True:
            cluster_response = rds_client.describe_db_clusters(DBClusterIdentifier=cluster_identifier)  # Fix: Used a different variable name
            status = cluster_response['DBClusters'][0]['Status']
#This line extracts the status of the DB cluster from the response. 
# The status information is nested in the response, and it's the status of the first 
#(and in this case, the only) cluster in the list. The extracted status is stored in the variable.
            print(f"DB cluster status: {status}")

            # Check if the DB cluster is now 'available'.
            if status == 'available':
                print(f"DB cluster '{cluster_identifier}' is now available.")
                break

            time.sleep(60)  # wait for 60 seconds before checking again

# Call the function to create or check the existence of the DB cluster
create_db_cluster()
