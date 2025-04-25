import boto3

client = boto3.client('s3')
client.create_bucket(Bucket='joe12dit') # creating a bucket with the name 'joe12dit'

with open('myfile.text','w') as file: # creating a file with the file name myfile.text with a 'w' write permisson
    file.write('this is the tex file for upload.') #this is the message in the file
client.upload_file(Filename='myfile.text', #  file name
                   Bucket='joe12dit', # Bucket name
                   Key='test-up') # the key to the file name.
client.download_file(Filename='mydownloadfile.text', # file name that needs to download in the bucket. It doesn't necessary need to have the same name with the upload file.
                   Bucket='joe12dit', # Bucket name
                   Key='test-up') # the key to the file name.
with open('mydownloadfile.text','r') as file: # creating a file with the file name myfile.text with a 'r' read permisson
    

 client.delete_object(Bucket='joe12dit', 
                      Key='test-up') # delete file. bucket name and key to the file
 
 #client.delete_bucket(Bucket='joe12dit') # to delete bucket



