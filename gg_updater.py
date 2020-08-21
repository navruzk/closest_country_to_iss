from web3 import Web3
import requests
import json
import time

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545", request_kwargs={"timeout": 60}))

def country_code_finder(latitude, longitude):

    place = None
    for b in range(10):
        b = b / 10
        long = str(float(latitude) + b)

        for a in range(10):
            a = a / 10
            lat = str(float(longitude) + a)

            try:
                coordinates = lat + ', ' + long
                location = locator.reverse(coordinates)
                place = location.raw['address']['country_code'].lower()
            except:
                continue

            if len(place) == 2:
                return place

        if type(place) == type(None):
            return place = 'nc'

with open("address_credential.json", "r") as json_data:
    credential_address = json.load(json_data)

oracle_address = credential_address["oracle_address"]
account = credential_address["owner_address"]
private_key = credential_address["private_key"]

with open("../build/contracts/GeographyGenius.json", "r") as outfile:
    geographygenius_json = json.load(outfile)

oracle_instance = w3.eth.contract(
    address=oracle_address, abi=geographygenius_json["abi"],
)

if __name__ == "__main__":

    while True:

        url = "http://api.open-notify.org/iss-now.json"

        iss_json = eval(requests.get(url).text)

        long = iss_json["iss_position"]["longitude"]
        lat = iss_json["iss_position"]["latitude"]

        country = country_code_finder(lat, long)

        nonce = w3.eth.getTransactionCount(account)
        oracle_tx = oracle_contract_instance.functions.updateData(
            long, lat, country
        ).buildTransaction(
            {"gas": 222222, "gasPrice": w3.toWei("1", "gwei"), "nonce": nonce,}
        )

        signed_txn = w3.eth.account.sign_transaction(oracle_tx, private_key=private_key)
        tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)

        print("Updated the contract")
        print("Sleeping now")
        time.sleep(60 * 5)
