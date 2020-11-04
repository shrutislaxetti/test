#!/bin/bash

## Application installation ##

#Install java and git
sudo yum install -y java
sudo yum install -y git

#Create a directory under /tmp
if [! -d "/tmp/codedeploy"]
then
  mkdir /tmp/codedeploy
fi

INCLUDE_PKGS='vim wget audit git ruby'
# Update OS packages and install includes
sudo yum clean all
sudo yum -y install $INCLUDE_PKGS
sudo yum -y update

cd /home/ec2-user
wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
sudo service codedeploy-agent status

sleep 10
