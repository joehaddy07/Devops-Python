import boto3
client = boto3.client('route53')
response = client.change_resource_record_sets(
    HostedZoneId='<www.edshopper.com>',
    ChangeBatch={
        'Comment': 'Automatic DNS update',
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': '<your_record_name>',
                    'Type': 'CNAME',
                    'TTL': 300,
                    'ResourceRecords': [
                        {
                            'Value': '<your_load_balancer_dns>'
                        },
                    ],
                }
            },
        ]
    }
)

