import json
import requests
import json
from web3 import Web3
import os
import w3storage
import requests
import logging

class Tracker:
    def __init__(self, contract_address, account_from, storage_api_key, abi) -> None:
        self.contract_address = contract_address
        self.account_from = account_from
        self.storage_api_key = storage_api_key
        self.abi = abi

    def connect(self):
        self.web3 = Web3(Web3.HTTPProvider('https://wallaby.node.glif.io/rpc/v0'))
        self.web3.eth.defaultAccount = self.account_from['address']
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.abi)

    def get_projects(self, ):
        projects = self.contract.functions.allProjects().call()
        return projects

    def add_project(self, name, repolink, cid):
        eth = self.web3.eth
        nonce = eth.get_transaction_count(self.account_from['address'])

        gas_estimate = self.contract.functions.add(name, repolink, cid).estimate_gas()
        print(f'Gas estimate to transact with setVar: {gas_estimate}')

        send_tx = self.contract.functions.add(name, repolink, cid).build_transaction(
            {
                'from': self.account_from['address'],
                'nonce': nonce
            }
        )
        tx_create = eth.account.sign_transaction(send_tx, self.account_from['private_key'])
        tx_hash = eth.send_raw_transaction(tx_create.rawTransaction)
        tx_receipt = eth.wait_for_transaction_receipt(tx_hash, timeout=400)
        return tx_receipt.transactionHash.hex()

    def update_cid(self, id, cid):
        eth = self.web3.eth
        nonce = eth.get_transaction_count(self.account_from['address'])
        send_tx = self.contract.functions.updateCid(id, cid).build_transaction(
            {
                'from': self.account_from['address'],
                'nonce': nonce
            }
        )
        tx_create = eth.account.sign_transaction(send_tx, self.account_from['private_key'])
        tx_hash = eth.send_raw_transaction(tx_create.rawTransaction)
        tx_receipt = eth.wait_for_transaction_receipt(tx_hash, timeout=400)
        return tx_receipt.transactionHash.hex()

    def call_rpc(self, method, params=None):
        url = "https://wallaby.node.glif.io/rpc/v0"
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            'jsonrpc': "2.0",
            'method': method,
            'params': params,
            'id': 1
          })
        
        res = requests.post(url, data=data, headers=headers)
        return res.json()
    

def get_repo_stat_page(repo, per_page, page):
    url = f"https://api.github.com/repos/{repo}/contributors?per_page={per_page}&page={page}"

    payload={}
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer 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'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

def get_repos(organization):
    url = f"https://api.github.com/orgs/{organization}/repos"
    payload={}
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer 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'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    repo_urls = [rep['full_name'] for rep in res]

    return repo_urls

def main():
    logging.level=logging.DEBUG

    orgs = [ {'name': 'Uniswap', 'github': 'https://github.com/Uniswap', 'volume': 625097885756.9067},
            {'name': 'Curve', 'github': 'https://github.com/curvefi', 'volume': 150521694077.0348},
            {'name': 'Sushiswap', 'github': 'https://github.com/sushiswap', 'volume': 49040293844.09633},
            {'name': 'Balancer', 'github': 'https://github.com/balancer-labs', 'volume': 28457489366.547653},
            {'name': 'DODO', 'github': 'https://github.com/DODOEX', 'volume': 23455259013.630615},
            {'name': '0x Native', 'github': 'https://github.com/0xProject', 'volume': 21874199433.42813},
            {'name': 'Synthetix', 'github': 'https://github.com/Synthetixio', 'volume': 10195971505.294567},
            {'name': '1inch Network', 'github': 'https://github.com/1inch', 'volume': 8013047105.629432},
            {'name': 'Bancor', 'github': 'https://github.com/bancorprotocol', 'volume': 6314867108.710405},
            #{'name': 'Shibaswap', 'github': 'https://github.com/sushiswap', 'volume': 5694971879.214641},
    ]
    with open(r'0xRoyalty.xyz\parser\Tracker.json', 'r') as f:
        js = json.load(f) 
    abi = js['abi']
    storage_api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDVjMTQwRTc4Y2VFQmQ2Njk3NkUxMzk0MjdFNTYwMzc1ODJDYjhiN2IiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2Njg4OTI3OTA4MTksIm5hbWUiOiIweFJveWFsdHkifQ.hYcfthHC-RBtHdDV28jdAksdiksfn370eRnZY5VHkak'
    contract_address = '0xcED7B64Dc3F4ef7a2FdcF9A1937FA389E37dc639'
    account_from = {
        'private_key': 'b105269e30d819fbb298f41690cf84ef0814fb47fabe22d41613e3d95e985a63',
        'address': '0x2969EBF3701549Da0AdA58e8C9C9E19363c58bab',
    }
 
    tracker = Tracker(contract_address, account_from, storage_api_key, abi)
    tracker.connect()

    #projects = tracker.get_projects()
    #print(projects)
    #exit()
    #priorityFee = tracker.call_rpc("eth_maxPriorityFeePerGas")
    #print(priorityFee)
    #exit()
    
#    tx = tracker.add_project("Uniswap", 'https://github.com/Uniswap', bytes('123', 'utf-8'))
#    print(tx)
    


    """
        for org in orgs:
            repos = [{'slug': rep} for rep in get_repos(org['github'][19:])]

            print(repos)

            for repo in repos:
                res = get_repo_stat_page(repos[0]['slug'], 100, 1)
                repo['stat'] = res
            
            org['repos'] = repos

        with open('repostat.json', 'w') as f:
            json.dump(orgs, f, indent=4, ensure_ascii=False)

    """ 
    with open(r'0xRoyalty.xyz\parser\repostat.json', 'r', encoding='utf-8') as f:
        orgs = json.load(f)
    
    w3 = w3storage.API(token=storage_api_key)

    for org in orgs:
        name = org['name']
        print(name)
        github = org['github']
        volume = org['volume']
        cid = w3.post_upload((f'{name}.json', json.dumps(org)))
        print('cid', cid)
        
        tx = tracker.add_project(name, github, bytes(cid, 'utf-8'))
        print('transaction', tx)
       
    
    
    projects = tracker.get_projects()
    print(projects)



if __name__ == "__main__":
    main()
    
"""
 const priorityFee = await callRpc("eth_maxPriorityFeePerGas")



    const simpleCoinContract = new ethers.Contract(contractAddr, SimpleCoin.interface, signer)
    console.log("Sending:", amount, "SimpleCoin to", toAccount)
    await simpleCoinContract.sendCoin(toAccount, amount, {
        gasLimit: 1000000000,
        maxPriorityFeePerGas: priorityFee
    })
"""