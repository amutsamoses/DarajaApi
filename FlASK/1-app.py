import requests
from flask import Flask, render_template, request, jsonify
from requests.auth import HTTPBasicAuth
import json
import base64

app = Flask(__name__)

# safaricam API credentials
CONSUMER_KEY = "YxW0BxJusMAFYxy90TxzY6YdNkiIpMT5P3n3YBgaLbvHtiAr"
CONSUMER_SECRET = "Y4LnVdDv5cF5KSQhG4PnSrxJENFIQKddbc0ivPtkeIcCYZt7yYPq58bgbNziusIG"
MPESA_API_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
PROCESS_REQUEST_URL = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

# get access token
def get_access_token():
    response = requests.get(MPESA_API_URL, auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET))
    json_response = response.json()
    return json_response['access_token']

@app.route('/')
def index():
    return render_template('1-index.html')


@app.route('/submit', methods=['POST'])
def submit():
    phone_number = request.form['phone']

    # call the Daraja Api to process the transaction
    access_token = get_access_token()

    headers = {
        "Authorization": f'Bearer {access_token}',
        "Content-Type": "application/json"
    }

    Body = {
    "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQxMDA0MTgxNzUz",
    "Timestamp": "20241004181753",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": 254705549449,
    "PartyB": 174379,
    "PhoneNumber": 254705549449,
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X" 
    }

    response = requests.post(PROCESS_REQUEST_URL, headers=headers, data=json.dumps(Body))
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
 