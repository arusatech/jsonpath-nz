import json
import sys
import os

def ar_print(data, load=False, marshall=True, indent=2):
    '''To print the data in a readable format'''
    def _stringify_val(data):
        if isinstance(data, dict):
            return {k: _stringify_val(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [_stringify_val(v) for v in data]
        elif isinstance(data, (str, int, float)):
            return data
        return str(data)

    _data = _stringify_val(data) if marshall else data
    try:
        _d = (
            json.dumps(json.loads(_data), indent=indent) if load else
            json.dumps(_data, indent=indent)
        )
    except:
        _d = _data

    print(_d)
    
    
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


import jsonpath_nz as jnz

jsonPayload = {
  "store": {
    "book": [
      {},
      {
        "category": "Fiction",
        "author": "Yakub Mohammad"
      },
      {
        "price": "100",
        "title": "The Great Gatsby"
      }
    ],
    "local": "False"
  },
  "channel": "online",
  "loanProductData": {
    "gsePropertyType": "HUDA"
  },
  "applications": [
    {
      "propertyUsageType": "Primary"
    }
  ],
  "closingCost": {
    "gfe2010": {
      "gfe2010Fees": [
        {
          "gfe2010FeeParentType": "Section801",
          "gfe2010FeeType": "Line820",
          "borPaidAmount": "100.01"
        },
        {
          "gfe2010FeeParentType": "Section801",
          "gfe2010FeeType": "Line821",
          "selPaidAmount": "0"
        },
        {
          "gfe2010FeeParentType": "Section801",
          "gfe2010FeeType": "Line822",
          "paidToName": "Title"
        },
        {
          "gfe2010FeeParentType": "Section800",
          "gfe2010FeeType": "Line802e",
          "totalFeeAmount2015": "number"
        }
      ]
    }
  },
  "companyInfo": {
    "customFields": {
      "fields": [
        {
          "fieldName": "Other Tiers",
          "value": "integer"
        },
        {
          "fieldName": "Texas A(6)",
          "value": "boolean"
        }
      ]
    }
  },
  "customModelFields": {
    "provideBestCaseScenario": "boolean"
  }
}

EXT = {"gfe2010Fees": ["gfe2010FeeParentType", "gfe2010FeeType"], 'fields': ['fieldName']}
result = jnz.parse_dict(jsonPayload, extend=EXT)

ar_print(result)
