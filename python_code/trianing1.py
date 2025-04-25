import boto3
import csv
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event,context):
    billing_bucket= event['record'][0]['s3']['bucket']['name']
    csv_file= event['record'][0]['s3']['object']['key']

    error_bucket= 'xxxx'

    obj= s3.get_object(Bucket='billing_bucket',Key='csv_file')
    data= obj['body'].read().decode('uft-8').splitlines()

    error_bucket= False

    valid_product_lines= ['Rice','Meat','Fruit']
    valid_currency_lines= ['USD','CAD','MXN']

    for row in csv.reader(data[1:], delimiter=','):
        print(f"{row}")

        date= row[6]
        product_lines= row[7]
        currency_lines= row[8]
        bill_amount= (row[9])

        try:
            datetime.strptime(date, '%y-%m-%d')
        except ValueError:
            error_found= True
            print(f"error found in record {row[0]}: incorrect date format {date}")

            if product_lines not in valid_product_lines:
                error_found= True
                print(f"error found in record {row[0]}: unreconized product line {valid_product_lines}")

                
            if currency_lines not in valid_currency_lines:
                    error_found= True
                    print(f"error found in record {row[0]}: unreconized currency lines {valid_currency_lines} ")

            if error_found:
                copy_source={ 
                'Bucket':billing_bucket,
                'key': csv_file
                }
        try:
            s3.meta.client.copy(copy_source, error_bucket, csv_file)
            print(f"move erronoeus file to: {error_bucket}")
            s3.object(billing_bucket, csv_file)
            print(f"delete oringal file from bucket")
        except Exception as e:
             print(f"error while moving file: {str(e)}")

        else:
             return{
                  'StatusCode':200,
                  'Body': 'No error found in csv'
             }     


        
                        

        
        
