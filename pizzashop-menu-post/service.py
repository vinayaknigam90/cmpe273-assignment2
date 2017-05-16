# -*- coding: utf-8 -*-
import boto3
import json
from botocore.exceptions import ClientError

def handler(event, context):
  try:
    res=boto3.resource('dynamodb', region_name='us-west-2') 
    table = res.Table('menu')
    sequence = '["selection", "size"]'
    event['sequence'] = json.loads(sequence)
    table.put_item(Item=event)
    response = {}
    return response
  except Exception as e:
    return e.message
