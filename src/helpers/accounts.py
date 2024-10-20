
from .settings import *

import json
from datetime import datetime

def add_account(username, password):
    try:
        # Open the file in read mode, handle if the file does not exist or is empty
        with open(acc_json_path, 'r') as file:
            try:
                accounts = json.load(file)
            except json.JSONDecodeError:
                # If file is empty or contains invalid JSON, initialize an empty list
                accounts = []
    except FileNotFoundError:
        # If the file is not found, initialize an empty list
        accounts = []

    # Create a new account dictionary
    new_account = {
        'username': username,
        'password': password,
        'role': "Student",
        'created_at': datetime.now().isoformat()
    }                                                   

    # Append the new account to the list
    accounts.append(new_account)

    # Write the updated list back to the file
    with open(acc_json_path, 'w') as file:
        json.dump(accounts, file, indent=4)

def verify_account(username, password):
    try:
        # Open the file in read mode, handle if the file does not exist or is empty
        with open(acc_json_path, 'r') as file:
            try:
                accounts = json.load(file)
            except json.JSONDecodeError:
                # If file is empty or contains invalid JSON, return False
                return False
    except FileNotFoundError:
        # If the file is not found, return False
        return False

    # Iterate over the accounts to find a matching account
    for account in accounts:
        if account['username'] == username and account['password'] == password:
            return True

    return False

def get_account(username, password):
    try:
        # Open the file in read mode, handle if the file does not exist or is empty
        with open(acc_json_path, 'r') as file:
            try:
                accounts = json.load(file)
            except json.JSONDecodeError:
                # If file is empty or contains invalid JSON, return None
                return None
    except FileNotFoundError:
        # If the file is not found, return None
        return None

    # Iterate over the accounts to find a matching account
    for account in accounts:
        if account['username'] == username and account['password'] == password:
            return account

    return None