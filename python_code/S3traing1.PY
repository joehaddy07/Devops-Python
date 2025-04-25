import boto3

# Function to delete an object from S3
def delete_object(bucket_name, object_key):
    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        # Delete the object
        s3.delete_object(Bucket=bucket_name, Key=object_key)
        print(f"Object '{object_key}' deleted successfully from '{bucket_name}'.")
    except Exception as e:
        print(f"Error deleting object '{object_key}' from '{bucket_name}': {e}")

# Replace 'joe12dit' and 'test' with your actual bucket name and object key
delete_object('sammydec40', 'test')

# Function to delete an S3 bucket
def delete_bucket(bucket_name):
    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting bucket '{bucket_name}': {e}")

# Replace 'joe12dit' with your actual bucket name
delete_bucket('sammydec40')

