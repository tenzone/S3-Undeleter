import boto3

#setup AWS session, mine uses my ~/.aws/credentials configuration. If you need to hard code credentials, dont
session = boto3.Session()
s3 = session.client('s3')

# Define bucket name and prefix(directory path) if needed

bucketname = 'yourBucketHere'
prefix = 'BucketPrefixPath'

#paginator allows us to work with more than the default (500) or max (1000) results from the aws API
paginator = s3.get_paginator('list_object_versions')
pages = paginator.paginate(Bucket = bucketname, Prefix = prefix)

#This loop goes over all the paginated pages of results, and extracts the key for the files that have DeleteMarkers. It then gets the versionID of the delete marker and deletes it, therefore restoring the files
#Note, the print statement is just to show me how many results in each page have a delete marker, also lets me know the script is running and not frozen

for page in pages:
    if 'DeleteMarkers' in page:
        print(len(page['DeleteMarkers'])) 
        delmark = page['DeleteMarkers']
        to_Delete = []
        for marker in delmark:
            to_Delete.append({'VersionId':marker['VersionId'],'Key': marker['Key']})
        s3.delete_objects(Bucket = bucketname, Delete = {'Objects':to_Delete})
