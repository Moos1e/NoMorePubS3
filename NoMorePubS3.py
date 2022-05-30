import boto3
import botocore
import time

s3 = boto3.resource('s3')
client = boto3.client('s3')

session = boto3.Session(
    aws_access_key_id=<key>,
    aws_secret_access_key=<secret>
)
s3 = boto3.client('s3')

#List Buckets
def listBuckets():
    import boto3
    s3 = boto3.resource('s3')
    print("The following buckets are associated with the target accounts.\n")
    for bucket in s3.buckets.all():
        print("* "+bucket.name+" *")
    time.sleep(2)
    return bucket.name

bucket = listBuckets()


#Allow User to Select Bucket and Inspect 
target = input("What bucket would you like to inspect?\n Insert bucket name here --> ")

 
try:
    access = s3.get_public_access_block(Bucket='moosepub')
    print (access)
except botocore.exceptions.ClientError as a:
    if a.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
        print('\t no Public Access')
    else:
        print("unexpected error: %s" % (e.response))

#Disable Public Access
time.sleep(2)
print("\n*** Disabling Public Access To " +target+ " ***")
time.sleep(4)
time.sleep(2)
print("\n*** Ensuring all other buckets are made private ***")
time.sleep(2)

def main():
    # Create the boto Session from the profile stored on the host
    mySesh = boto3.Session(profile_name=target)
    s3client = mySesh.client('s3')
    # Get the list of all your buckets
    allbuckets = s3client.list_buckets()
    # Iterate over the list
    for bucket in allbuckets['Buckets']:
        try:
            # This will set the public block settings
            s3client.put_public_access_block(
                Bucket=bucket['Name'],
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': True,
                    'RestrictPublicBuckets': True
                }
            )
        except:
            # How to handle an error goes here
            pass

#Advise User that Buckets are no longer public

print("\nBuckets with the AWS environment are no longer public. Please sign into your AWS account and review contents and purpose of all S3 buckets" )
