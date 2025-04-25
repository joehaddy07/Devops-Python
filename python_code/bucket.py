import boto3 #This line imports the Boto3 library, allowing you to interact with AWS services using Python.

client = boto3.client('s3')#creates an S3 client object. This object allows you to make API calls to interact with and manage your S3 buckets and objects.
response = client.create_bucket( ## creating a bucket with the name 'joe12dit'
    Bucket='joe12dit'
)

# Open a file for writing (creates the file if it doesn't exist)
file_name = "my_file.txt"  # Change this to the desired file name
with open('my_file.txt', "w") as file:
    file.write("This is my file to be uploaded to the s3 bucket")
    file.write("my first file to be uploaded")
# The file is automatically closed when the 'with' block is exited

client.upload_file(Filename='myfile.text', #  file name
                   Bucket='joe12dit', # Bucket name
                   Key='test-up') # the key to the file name.


client.download_file(Filename='mydownloadfile.text', # file name that needs to download in the bucket. It doesn't necessary need to have the same name with the upload file.
                   Bucket='joe12dit', # Bucket name
                   Key='test-up') # the key to the file name.
with open('mydownloadfile.text','r') as file: # creating a file with the file name myfile.text with a 'r' read permisson


#A presigned URL, short for "pre-signed URL," is a URL that grants temporary access to a specific resource on a web server, 
# typically an object in a storage service like Amazon S3.
 url = client.generate_presigned_url(ClientMethod= 'get_object', #This methods allow you to make API requests 
                                      Params={'Bucket':'joe12dit',# Bucket name
                                           'Key':'test-up'},# the key to the file name.
                                             ExpiresIn=5*60) # the duration of the temperary url = 5 min * 60 sec
 
 #Here's how it works:A user or an application with the necessary permissions generates 
 #a presigned URL using the storage service's API or SDK. They specify the resource they want to access, the HTTP method 
 #(e.g., GET, PUT, DELETE), and an expiration time for the URL.
 #Once the presigned URL expires, it can no longer be used to access the resource, enhancing security and access control.

 client.delete_object(Bucket='joe12dit', 
                      Key='test-up') # delete file. bucket name and key to the file
 
 #client.delete_bucket(Bucket='joe12dit') # to delete bucket



 print(response)