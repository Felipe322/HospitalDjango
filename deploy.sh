#!/bin/bash
set -e
set -o pipefail

ip_pre="52.27.53.105"
dns_pre="ec2-52-27-53-105.us-west-2.compute.amazonaws.com"
repo="$gitlabSourceRepoName"

> ~/.ssh/known_hosts
ssh-keyscan  -H $dns_pre >> ~/.ssh/known_hosts
ssh-keyscan  -H $ip_pre >> ~/.ssh/known_hosts

cd ..
scp -r -i ~ubuntu/llave_aws.pem $repo ubuntu@$dns_pre:~/

ejecutar="$(cat <<-EOF
sudo mysqldump hospital2 > hospital2.sql
sudo apt-get update; apt-get install apache2 mariadb-server 
sudo cp $repo/hospital.conf /etc/apache2/sites-available/
virtualenv env_hospital
. env_hospital/bin/activate
cd $repo
pip install -r requirements.txt
rm deploy.sh Jenkinsfile hospital.conf
sudo systemctl restart apache2.service
EOF
)"

ssh -i ~ubuntu/llave_aws.pem ubuntu@$dns_pre "$ejecutar"