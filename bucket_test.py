import boto3  # pip install boto3

# Let's use Amazon S3
s3 = boto3.resource("s3")

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Create an S3 access object

test_download = boto3.client("s3")

test_download.download_file(
    Bucket="dmc-first-bucket", Key="data/hello_world.txt", Filename="hello.txt"
)


#s3_client = boto3.client("s3")

#s3_client.upload_file(
#    Filename="hello_world.txt",
#    Bucket="dmc-first-bucket",
#    Key="hello.txt",
#)