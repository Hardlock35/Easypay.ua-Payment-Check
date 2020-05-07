import requests

receiptID = "804611978" #number of the receipt/payment
amount = "3480" #paid amount of money

#making an GET request to API of easypay
response = requests.get('https://api.easypay.ua/api/payment/getReceipt',params={"receiptId": receiptID , "amount": amount, "contentType": "application/json"},
headers= {"accept": "application/pdf", "appid": "13afe22f-9ca1-472a-9322-9baf3f03aaf1", "content-type": "application/json; charset=UTF-8"}
)

if str(response) == "<Response [200]>":
    print("payment worked") #you can paste your code here that should start if the payment DO work
else:
    print("payment didnt worked") #you can paste your code here that should start if the payment DOES NOT work