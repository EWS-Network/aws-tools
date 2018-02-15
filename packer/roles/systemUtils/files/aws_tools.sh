#!/bin/bash


pip --version || curl https://bootstrap.pypa.io/get-pip.py | python
pip install pip --upgrade
pip install awscli --upgrade
pip install boto3 --upgrade
pip install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-latest.tar.gz
find /usr/bin -name \"cfn-*\"  -exec  chmod +x {} +

