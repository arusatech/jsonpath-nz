import json
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

xmlData = """

"""
import jsonpath_nz as jnz
import json
payload = jnz.xml_to_json("tests/test.xml", namespace=False)
print(type(payload))
dictPayload = jnz.flatten_dict(json.loads(payload), preserve_dict_values=False)
jnz.jprint(dictPayload)







