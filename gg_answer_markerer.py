from web3 import Web3
import requests
import json
import time

## here could be used infure link for connection to any testnet
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545", request_kwargs={"timeout": 60}))

with open("address_credential.json", "r") as json_data:
    credential_address = json.load(json_data)

token_address = credential_address["token_address"]
oracle_address = credential_address["oracle_address"]
account = credential_address["owner_address"]
private_key = credential_address["private_key"]

with open("../build/contracts/GeographyGenius.json", "r") as outfile:
    geographygenius_json = json.load(outfile)

oracle_contract_instance = w3.eth.contract(
    address=oracle_adress, abi=geographygenius_json["abi"],
)

with open("../build/contracts/GeographyGeniusToken.json", "r") as outfile:
    geographygeniustoken_json = json.load(outfile)

token_contract_instance = w3.eth.contract(
    address=token_address, abi=geographygeniustoken_json["abi"],
)

if __name__ == "__main__":

    checked_submissions = []

    while True:

        true_answer = oracle_contract_instance.functions.getCountryName().call(
            {"from": account}
        )

        submission_list = oracle_contract_instance.functions.getSubmissionList().call(
            {"from": account}
        )
        submission_list = [id for id in submission_list if id not in checked_submissions]

        reward = 1000

        for requestee_id in pendinglists:

            answered_list.append(requestee_id)

            extracted_answer = oracle_contract_instance.functions.getSubmissionInfo_answer(
                requestee_id
            ).call(
                {"from": account}
            )
            extracted_address = oracle_contract_instance.functions.getSubmissionInfo_address(
                requestee_id
            ).call(
                {"from": account}
            )

            if extracted_answer == true_answer:

                nonce = w3.eth.getTransactionCount(account)
                transfer_function = token_contract_instance.functions.transfer(
                    extracted_address, reward
                )
                token_tx = transfer_function.buildTransaction(
                    {"gas": 222222, "gasPrice": w3.toWei("1", "gwei"), "nonce": nonce,}
                )
                signed_txn = w3.eth.account.sign_transaction(
                    token_tx, private_key=private_key
                )
                tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
                print("Reward sent!")
