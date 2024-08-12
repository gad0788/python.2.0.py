import boto3

def start_ec2_instance(instance_id):
    # Initialize a session using Amazon EC2
    ec2 = boto3.client('ec2')

    try:
        # Start the EC2 instance
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Starting instance {instance_id}...")

        # Wait for the instance to start
        waiter = ec2.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id])

        # Describe the instance to get its details
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]

        # Retrieve instance details
        public_ip = instance.get('PublicIpAddress', 'No Public IP')
        state = instance['State']['Name']
        name = 'No Name'
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                name = tag['Value']

        # Print the details
        print(f"Instance ID: {instance_id}")
        print(f"Name: {name}")
        print(f"State: {state}")
        print(f"Public IP: {public_ip}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # EC2 instance ID
    instance_id = 'i-046382b124df968a3'
    start_ec2_instance(instance_id)
