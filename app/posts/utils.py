import boto3
import urllib


def add_image(file, folder):
    s3_client = boto3.client('s3')
    path = 'darlene/' + folder + '/' + file.filename
    s3_client.put_object(Bucket="projectbit", Key=path, Body=file)
    url = 'https://projectbit.s3-us-west-1.amazonaws.com/darlene/' + folder + '/' + file.filename
    image = urllib.parse.quote(url, "\./_-:")
    return image