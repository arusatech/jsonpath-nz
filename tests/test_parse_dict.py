import json
import sys
import os

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
          "selPaidAmount": "0",
          "borPaidAmount": "100.01"
        },
        {
          "gfe2010FeeParentType": "Section801",
          "gfe2010FeeType": "Line822",
          "paidToName": "Title",
          "borPaidAmount": "100.01"
        },
        {
          "gfe2010FeeParentType": "Section800",
          "gfe2010FeeType": "Line802e",
          "totalFeeAmount2015": "number",
          "borPaidAmount": "100.01"
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
# EXT = {"gfe2010Fees": ["gfe2010FeeParentType"], 'fields': ['fieldName']}
result = jnz.parse_dict(jsonPayload, extend=EXT)

jnz.jprint(result)
