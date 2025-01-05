import sys
import os
  
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


import jsonpath_nz as jnz
jsonpath_data = {
    "$.store.book[1].author": "Yakub Mohammad",
    "$.store.local": "False",
    "$.channel": "online",
    "$.loanApplication.borrower[?(@.firstName == 'John' && @.lastName == 'Doe')].contact": "9876543210",
    "$.loanApplication.borrower[?(@.firstName == 'John' && @.lastName == 'wright')].contact": "9876543211"
}
EXT_1 = {
    "borrower": ["firstName", "lastName"]
}

manifest = {
    "$.store.book[2].price" :"100",   
    "$.store.book[1].category" :"Fiction",
    "$.store.book[2].title" :"The Great Gatsby",
    "$.store.book[1].author" :"Yakub Mohammad",
    "$.store.local" :"False",
    "$.channel" :"online",
    "$.loanProductData.gsePropertyType" :"HUDA",
    "$.applications[0].propertyUsageType" :"Primary",
    "$.closingCost.gfe2010.gfe2010Fees[?(@.gfe2010FeeParentType == 'Section801' && @.gfe2010FeeType == 'Line820')].borPaidAmount" :"100.01",
    "$.closingCost.gfe2010.gfe2010Fees[?(@.gfe2010FeeParentType == 'Section801' && @.gfe2010FeeType == 'Line821')].selPaidAmount" :"0",
    "$.closingCost.gfe2010.gfe2010Fees[?(@.gfe2010FeeParentType == 'Section801' && @.gfe2010FeeType == 'Line822')].paidToName" :"Title",
    "$.closingCost.gfe2010.gfe2010Fees[?(@.gfe2010FeeParentType == 'Section800' && @.gfe2010FeeType == 'Line802e')].totalFeeAmount2015": "number",
    "$.companyInfo.customFields.fields[?(@.fieldName == 'Other Tiers,')].value": "integer",
    "$.customModelFields.provideBestCaseScenario": "boolean",
    "$.companyInfo.customFields.fields[?(@.fieldName == 'Texas A(6)')].value": 	"boolean",
    
}

EXT_2 = {"gfe2010Fees": ["gfe2010FeeParentType", "gfe2010FeeType"], 'fields': ['fieldName']}
payload = jnz.parse_jsonpath(manifest, extend=EXT_2)
jnz.jprint(payload)

payload = jnz.parse_jsonpath(jsonpath_data, extend=EXT_1)
jnz.jprint(payload)

