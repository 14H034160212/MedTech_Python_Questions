# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 21:06:42 2019

@author: Bill Bao
"""
import json
from jsonschema import validate

# Load the json file
with open('work_test.json','r') as f:
    example_dict = json.load(f)
schema = {
        "type" : "object",
        "properties" : {
                "value" : {"type" : "number"},
                "time" : {"type" : "number"},
                },
        }

for example in example_dict:
    validate(instance=example, schema=schema)
