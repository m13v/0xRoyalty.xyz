import json
from web3 import Web3

with open(r'python_test\SimpleCoin.json', 'r') as f:
    js = json.load(f) 

abi = js['abi']
bytecode = js['bytecode']

account_from = {
    'private_key': 'b105269e30d819fbb298f41690cf84ef0814fb47fabe22d41613e3d95e985a63',
    'address': '0x2969EBF3701549Da0AdA58e8C9C9E19363c58bab',
}
contract_address = '0xACCBC0C9Bb921e7AbD1680da92E417835E764EA6'

web3 = Web3(Web3.HTTPProvider('https://wallaby.node.glif.io/rpc/v0'))

Tracker = web3.eth.contract(address=contract_address, abi=abi)

projects = SimpleCoin.functions.allProjects().call()

print(projects)
exit()
# sendCoin(address receiver, uint amount)
nonce = web3.eth.get_transaction_count(account_from['address'])
if not nonce: nonce = 0
print(nonce)
send_tx = SimpleCoin.functions.sendCoin('0xACCBC0C9Bb921e7AbD1680da92E417835E764EA6', 950).build_transaction(
    {
        'from': account_from['address'],
        'nonce': nonce,
    }
)
tx_create = web3.eth.account.sign_transaction(send_tx, account_from['private_key'])
tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=400)
print(f'Tx successful with hash: { tx_receipt.transactionHash.hex() }')

balance = SimpleCoin.functions.getBalance('0x2969EBF3701549Da0AdA58e8C9C9E19363c58bab').call()

print(balance)