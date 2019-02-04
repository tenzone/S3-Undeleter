# S3-Undeleter
## Purpose:
Ever delete a bucket or path in a bucket by accident? I did. good thing i had versioning enabled. I was able to turn on versioning and see the "deleted objects"
The all had a new version called Deleted Marker. I learned that "undeleting" was just removing the Delete Marker from all the files.
The console would make this easy, for a few files, but for the tens of thousands I marked as deleted, i was looking at days of point and click. Enter this script

I am still learning python, so i figured it would be a good way to help that, and make my day(s) a little less repetitive for this task.

## Usage
Replace the bucket name and the prefix with the actual values, authenticate into your AWS environment, and run this Python3 script.
It should go through the bucket/prefix you had supplied and search for all Objects with a 'DeleteMarkers' value. It then removes that Marker.
