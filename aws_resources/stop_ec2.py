import boto3

def stop_ec2_instance(instance_id):
    # Initialize a session using Amazon EC2
    ec2 = boto3.client('ec2')

    try:
        # Stop the EC2 instance
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping instance {instance_id}...")

        # Wait for the instance to stop
        waiter = ec2.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[instance_id])

        # Describe the instance to get its current state
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]

        # Retrieve instance state
        state = instance['State']['Name']

        # Print the state
        print(f"Instance ID: {instance_id}")
        print(f"State: {state}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # EC2 instance ID
    instance_id = 'i-046382b124df968a3'
    stop_ec2_instance(instance_id)
