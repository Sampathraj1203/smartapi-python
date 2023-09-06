import json
import logging
import requests
import re
import uuid
import socket
from requests import get
from SmartConnect import SmartConnect  # Import the SmartConnect class

# Define the login function
def login_to_account():
    # Replace these with your actual credentials
    api_key = "pYlAqnVU"
    client_code = "s120761"
    password = "1203"
    totp = "3YROUBNKYEF4MLZZNYHHFHQLLY"  # Leave empty if TOTP is not required

    # Create an instance of the SmartConnect class
    smart_connect = SmartConnect(api_key=api_key)

    # Call the generateSession method with your credentials
    session_info = smart_connect.generateSession(client_code, password, totp)

    # Check the session_info to verify the login status
    if session_info['status'] == True:
        print("Login successful!")
        return session_info  # You can return the session information if needed
    else:
        print("Login failed. Error message:", session_info['message'])
        return None  # Return None in case of login failure

# Call the login function
login_result = login_to_account()

# Now you can use the 'login_result' if the login was successful
