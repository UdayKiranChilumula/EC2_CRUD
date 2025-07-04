import boto3
import json
import sys

# Load config
with open('requirements.json') as file:
    config = json.load(file)

region = config['region']
ec2 = boto3.client('ec2', region_name=region)

operation = sys.argv[1]  # operation: create, start, stop, terminate

def create_instance():
    response = ec2.run_instances(
        ImageId=config['ami_id'],
        InstanceType=config['instance_type'],
        KeyName=config['key_name'],
        MaxCount=1,
        MinCount=1,
        NetworkInterfaces=[{
            'AssociatePublicIpAddress': True,
            'DeviceIndex': 0,
            'SubnetId': config['subnet_id'],
            'Groups': [config['security_group_id']]
        }],
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': config['tag_name']}]
        }]
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Created EC2 Instance with ID: {instance_id}")

def start_instance():
    ec2.start_instances(InstanceIds=[config['instance_id']])
    print(f"Started EC2 Instance: {config['instance_id']}")

def stop_instance():
    ec2.stop_instances(InstanceIds=[config['instance_id']])
    print(f"Stopped EC2 Instance: {config['instance_id']}")

def terminate_instance():
    ec2.terminate_instances(InstanceIds=[config['instance_id']])
    print(f"Terminated EC2 Instance: {config['instance_id']}")

if operation == 'create':
    create_instance()
elif operation == 'start':
    start_instance()
elif operation == 'stop':
    stop_instance()
elif operation == 'terminate':
    terminate_instance()
else:
    print(f"Invalid operation: {operation}")
