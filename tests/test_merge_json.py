import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from jsonpath_nz import merge_json, jprint

# Example 1: Merging two dictionaries
dict1 = {
    "name": "John",
    "details": {
        "age": 30,
        "skills": ["Python", "Java", "dict1", {"d1": "dict1"}, {"dict1": [1, 2, 3]}]
    }
}

dict2 = {
    "name": "John",
    "details": {
        "location": "NYC",
        "skills": ["JavaScript", "SQL", "Python", "dict2", {"dict2": "dict2"}, {"dict2": [1, 2, 3]}]
    }
}

# # Simple merge
result1 = merge_json(dict1, dict2, extend=False)
jprint(result1)

# Extended merge (will combine lists intelligently)
result2 = merge_json(dict1, dict2, extend=True)
jprint(result2)

# Example 2: Merging JSON files
# result3 = merge_json("file1.json", "file2.json", extend=True)
# jprint(result3)
# # Example 3: Merging JSON files with extend=False
# result4 = merge_json("file1.json", "file2.json", extend=False)
# jprint(result4)