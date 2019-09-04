import hashlib
import json

reward = 10.0

# the First block of the blockchain
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transaction': [],
    'nonce': 23
}

blockchain = [genesis_block]

# A list that manages all the outstanding transactions in the blockchain
open_transactions = []

owner = 'Fotis'

def hash_block(block):
    return hashlib.sha256(json.dumps(block).encode()).hexdigest()

# Essentially checks if the hash created fulfills the given difficulty criteria 
def valid_proof(transactions, last_hash, nonce):
    guess = (str(transactions) + str(last_hash) + str(nonce)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    print(guess_hash)
    
    return guess_hash[0:2] == '00'

def pow():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    nonce = 0

    while not valid_proof(open_transactions, last_hash, nonce):
        nonce += 1
    return nonce

# Extracting the last element of the blockchain list
def get_last_value():
    return (blockchain[-1])

def add_value(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)

''' 
Extracts the last block and puts in in last_block,
hashes the last block, 
extract nonce via pow(), 
award the miner with reward_transaction, 
append reward_transaction to the open_transaction list, 
with the new approved nonce we have a new block which helps us get the metadata of the new block,
append the new block to the blockchain 
'''
def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    nonce = pow()
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': reward
    }
    open_transactions.append(reward_transaction)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transaction': open_transactions,
        'nonce': nonce
    }

    blockchain.append(block)

def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Enter your transaction amount: '))

    return tx_recipient, tx_amount

def get_user_choice():
    user_input = input("Please give your choice here: ")

    return int(user_input)

def print_block():

    for block in blockchain:
        print("Here is your block")
        print(block)

while True:
    print("Choose an option")
    print("Choose 1 for adding a new transaction")
    print("Choose 2 for mining a new block")
    print("Choose 3 for printing the blockchain")
    print("Choose anything else if you want to quit")

    user_choice = get_user_choice()

    if user_choice == 1:
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_value(recipient, amount=amount)
        print(open_transactions)

    elif user_choice == 2:
        mine_block()

    elif user_choice == 3:
        print_block()
    
    else: 
        break


