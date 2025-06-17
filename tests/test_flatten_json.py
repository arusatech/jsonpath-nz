import sys
import os
import json

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)
from jsonpath_nz import merge_json, jprint, flatten_dict

jDict = {}
with open("tests/file3.json", "r") as f:
    # Read the file content first, then parse it
    content = f.read()
    jDict = json.loads(content)

# Print the flattened dictionary
jprint(flatten_dict(jDict))