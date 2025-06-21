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
    "$.companyInfo.customFields.fields[?(@.fieldName == 'Texas A(6)')].value":  "boolean",
    
}

json_data_2 = {
    "$.reservation.pointOfSale.pnrEditor[0].editorRole": "OWN",
    "$.reservation.pointOfSale.pnrEditor[0].userId.userType": "AIRLINE",
    "$.reservation.pointOfSale.pnrEditor[0].userId.iataNum": "45996322",
    "$.reservation.pointOfSale.pnrEditor[0].userId.officeId": "DALWN08AA",
    "$.reservation.pointOfSale.pnrEditor[0].deliverySysInfo.compId": "WN",
    "$.reservation.pointOfSale.pnrEditor[0].deliverySysInfo.locId": "DAL",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[0].lang": "multi",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[0].region.Asia[0]": "mandarin",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[0].region.Asia[1]": "hindi",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[0].region.Europe[0]": "english",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[0].region.Europe[1]": "poliski",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[0].region.America[0]": "English",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[0].region.America[1]": "Spinish",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[1].lang": "single",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[1].region.Asia[0]": "mandarin",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[1].region.Asia[1]": "hindi",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[1].region.Europe[0]": "english",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[1].region.Europe[1]": "poliski",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[1].region.America[0]": "English",
    "$.reservation.pointOfSale.pnrEditor[0].userPrefs.country[1].region.America[1]": "Spinish"
}
# jnz.jprint(jnz.parse_jsonpath(json_data_2))

json_data_3 = {
    "$.reservation.pointOfSale.pnrEditor[?(@.editorRole == 'OWN')].userId.userType": "AIRLINE",
    "$.reservation.pointOfSale.pnrEditor[?(@.editorRole == 'OWN')].userId.iataNum": "45996322",
    "$.reservation.pointOfSale.pnrEditor[?(@.editorRole == 'OWN')].userId.officeId": "DALWN08AA",
    "$.reservation.pointOfSale.pnrEditor[?(@.editorRole == 'OWN')].deliverySysInfo.compId": "WN",
    "$.reservation.pointOfSale.pnrEditor[?(@.editorRole == 'OWN')].deliverySysInfo.locId": "DAL",
    "$.reservation.pointOfSale.pnrEditor[?(@.editorRole == 'OWN')].userPrefs.country[?(@.lang == 'multi')].region.Asia[0]": "mabdarin",
    "$.reservation.pointOfSale.pnrEditor[?(@.editorRole == 'OWN')].userPrefs.country[?(@.lang == 'multi')].region.Asia[1]": "hindi",
    "$.reservation.pointOfSale.pnrEditor[?(@.editorRole == 'OWN')].userPrefs.country[?(@.lang == 'multi')].region.Europe[0]": "english",
    "$.reservation.pointOfSale.pnrEditor[?(@.editorRole == 'OWN')].userPrefs.country[?(@.lang == 'multi')].region.Europe[1]": "poliski",
    "$.reservation.pointOfSale.pnrEditor[?(@.editorRole == 'OWN')].userPrefs.country[?(@.lang == 'multi')].region.America[0]": "English",
    "$.reservation.pointOfSale.pnrEditor[?(@.editorRole == 'OWN')].userPrefs.country[?(@.lang == 'multi')].region.America[1]": "Spinish"
}
json_data_4 = {
    "$.store.book[1].author": "Yakub Mohammad",
    "$.store.local": "False",
    "$.channel": "online",
    "$.loanApplication.borrower[?(@.firstName == 'John' && @.lastName == 'Doe')].contact": "9876543210",
    "$.loanApplication.borrower[?(@.firstName == 'John' && @.lastName == 'wright')].contact": "9876543211",
    "$.1ab.2bc.3cd[?(@.4de == 'XYZ')].5ef.6fg[?(@.7gh == 'multi (1)')].8ij[?(@.9jk == 'ABC')].10kl.11lm[0]": "mandarin (1)",
    "$.1ab.2bc.3cd[?(@.4de == 'XYZ')].5ef.6fg[?(@.7gh == 'multi (1)')].8ij[?(@.9jk == 'UVY')].10kl.11lm[1]": "hindi (2)"
}
jnz.jprint(jnz.parse_jsonpath(json_data_4, extend=EXT_1))


EXT_2 = {"gfe2010Fees": ["gfe2010FeeParentType", "gfe2010FeeType"], 'fields': ['fieldName']}
# payload = jnz.parse_jsonpath(manifest, extend=EXT_2)
# # jnz.jprint(payload)

# payload = jnz.parse_jsonpath(jsonpath_data, extend=EXT_1)
# jnz.jprint(payload)