Overview of Code Functionality:
This Python code interacts with AWS EC2 service using the Boto3 library to achieve the following:

Identify Security Groups with SSH Open to the World:

It retrieves all security group rules and filters out security groups that have an SSH rule (port 22) open to the public internet (i.e., the source IP is 0.0.0.0/0).
Identify Running and Stopping EC2 Instances:

It retrieves all EC2 instances, filtering only those that are in a running or stopping state (ignoring those in the terminated state).
Match Instances with Insecure Security Groups:

It checks if any of these running or stopping instances are associated with security groups that have the SSH rule open to the world.
Terminate the Identified EC2 Instances:

If any instances are found that meet the criteria, it attempts to terminate them. If there are no such instances or an error occurs, it handles the exception gracefully by printing "No instances".

https://www.youtube.com/watch?v=QdZTgL1RyfM&t=603s

