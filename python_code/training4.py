import boto3
import json
import logging
from datetime import datetime

logger=logging.getLogger()
logger.setLevel(logging.INFO)

ec2= boto3.client('ec2')

def lambda_handler(even,context):
    try:
        instance_id='xxx'

        snapshot_description= f"snapshot for instance {instance_id}-{datetime.now().strptime('%y-%m-%d %h-%m-%s')}"

        response = ec2.create_snapshot(Description=' snapshot_description.',VolumeId='vol-1234567890abcdef0',)
        ec2.create_tags(Resources=[response['SnapshotId']],
       Tags=[{'Key': 'string',
        'Value': 'Mysnapshot'
            },
        ]
      )

        logger.info(f"snapshot created {response['SnapshotId']} successfully")
    
    except Exception as e:
        logger.error(f"snapshot errors {str(e)}")
