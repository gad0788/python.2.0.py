import boto3

def list_ebs_volumes():
    # Initialize a session using Amazon EC2
    ec2 = boto3.client('ec2')

    # List all volumes
    response = ec2.describe_volumes()

    # Loop through each volume in the response and print details
    for volume in response['Volumes']:
        print(f"Volume ID: {volume['VolumeId']}")
        print(f"  State: {volume['State']}")
        print(f"  Size: {volume['Size']} GiB")
        print(f"  Volume Type: {volume['VolumeType']}")
        print(f"  Availability Zone: {volume['AvailabilityZone']}")
        print(f"  Encrypted: {volume['Encrypted']}")
        print(f"  Tags: {volume.get('Tags', 'No Tags')}")
        print("")

if __name__ == "__main__":
    list_ebs_volumes()
