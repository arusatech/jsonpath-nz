import json
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


import jsonpath_nz as jnz
payload = jnz.xml_to_json("tests/test.xml", namespace=False)
print(payload)