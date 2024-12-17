import boto3
from boto3 import client
import os

client("s3", aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
