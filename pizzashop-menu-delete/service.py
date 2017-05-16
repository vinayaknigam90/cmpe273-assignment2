# -*- coding: utf-8 -*-
import boto3
import json
from botocore.exceptions import ClientError

def handler(event, context):
  try:
    res=boto3.resource('dynamodb', region_name='us-west-2') 
    table = res.Table('menu')
    table.delete_item(Key={'menu_id': event['menu_id']})
    response = {}
    return response
  except Exception as e:
    return e.message
