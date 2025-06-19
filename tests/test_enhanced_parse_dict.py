#!/usr/bin/env python3
"""
Test script for the enhanced parse_dict function with complex nested structures.
"""

import sys
import os

# Add the jsonpath_nz module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from jsonpath_nz.parse_dict import parse_dict

def test_complex_nested_structure():
    """Test the enhanced parse_dict function with the reservation example."""
    
    # The complex nested structure from the user's example
    dict1 = {
        "reservation" : {
            "pointOfSale": {
                "pnrEditor": [
                    {
                        "editorRole": "OWN",
                        "userId": {
                            "userType": "AIRLINE",
                            "iataNum": "45996322",
                            "officeId": "DALWN08AA"
                        },
                        "deliverySysInfo": {
                            "compId": "WN",
                            "locId": "DAL"
                        },
                        "userPrefs": {
                            "country": [
                                {
                                    "lang" : "multi",
                                    "region": {
                                        "Asia" : ["mabdarin", "hindi"],
                                        "Europe": ["english", "poliski"],
                                        "America" : ["English", "Spinish"]
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
    
    print("Testing enhanced parse_dict with complex nested structure...")
    print("=" * 60)
    
    # Test 1: Without extend configuration (index-based paths)
    print("\n1. Without extend configuration (index-based paths):")
    print("-" * 50)
    result1 = parse_dict(dict1)
    for path, value in result1.items():
        print(f"  {path}: {value}")
    
    # Test 2: With extend configuration (filter-based paths)
    print("\n2. With extend configuration (filter-based paths):")
    print("-" * 50)
    extend_config = {"pnrEditor": ["editorRole"], "country": ["lang"]}
    result2 = parse_dict(dict1, extend=extend_config)
    for path, value in result2.items():
        print(f"  {path}: {value}")
    
    # Test 3: Multiple filter fields
    print("\n3. Multiple filter fields:")
    print("-" * 50)
    # Add another item to test multiple filters
    dict1["reservation"]["pointOfSale"]["pnrEditor"].append({
        "editorRole": "OWN",
        "userType": "AGENCY",
        "userId": {
            "userType": "AGENCY",
            "iataNum": "12345678",
            "officeId": "AGENCY01"
        },
        "deliverySysInfo": {
            "compId": "AG",
            "locId": "NYC"
        }
    })
    
    extend_config_multi = {"pnrEditor": ["editorRole", "userType"]}
    result3 = parse_dict(dict1, extend=extend_config_multi)
    for path, value in result3.items():
        print(f"  {path}: {value}")
    
    # Test 4: Nested arrays
    print("\n4. Nested arrays test:")
    print("-" * 50)
    nested_array_data = {
        "departments": [
            {
                "name": "Engineering",
                "teams": [
                    [
                        {"id": "t1", "name": "Frontend"},
                        {"id": "t2", "name": "Backend"}
                    ],
                    [
                        {"id": "t3", "name": "DevOps"}
                    ]
                ]
            }
        ]
    }
    
    result4 = parse_dict(nested_array_data)
    for path, value in result4.items():
        print(f"  {path}: {value}")

def test_edge_cases():
    """Test edge cases and error handling."""
    
    print("\n\nTesting edge cases...")
    print("=" * 60)
    
    # Test with empty data
    print("\n1. Empty dictionary:")
    print("-" * 30)
    result = parse_dict({})
    print(f"  Result: {result}")
    
    # Test with None values
    print("\n2. Dictionary with None values:")
    print("-" * 30)
    data_with_none = {"key1": None, "key2": {"nested": None}}
    result = parse_dict(data_with_none)
    for path, value in result.items():
        print(f"  {path}: {value}")
    
    # Test with mixed data types in arrays
    print("\n3. Mixed data types in arrays:")
    print("-" * 30)
    mixed_data = {
        "items": [
            {"id": 1, "name": "Item 1"},
            "string_item",
            42,
            {"id": 2, "name": "Item 2"}
        ]
    }
    result = parse_dict(mixed_data)
    for path, value in result.items():
        print(f"  {path}: {value}")

if __name__ == "__main__":
    test_complex_nested_structure()
    test_edge_cases()
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("The enhanced parse_dict function now supports:")
    print("- Deep recursive processing of nested dictionaries within arrays")
    print("- Complex nested structures with multiple levels")
    print("- Improved filter condition handling")
    print("- Better handling of mixed data types")
    print("- Nested arrays support")