import random

prevID = 247888
custID = prevID+1 # customer ID for new customer is always 1 above the previous one.

newCustomer = {
    "firstName": "Bob",
    "secondName": "Muller",    #"Key":"Value"
    "DOB": "18/08/2001",
    "custID": str(custID),
    "joinDate": "14/03/2019"
}

for key in newCustomer:
    print(key,":",newCustomer[key]) # Prints key and Value

newCustomer["secondName"] = "Ben" # Changing secondName to "Ben"
print(newCustomer["secondName"])  # Prints the secondName of the newCustomer

newCustomer.update({"monthlyPay": 12.99}) # Adds new field with .update({"x":y})
print(newCustomer)