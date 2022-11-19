import json
import requests

storage_api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDVjMTQwRTc4Y2VFQmQ2Njk3NkUxMzk0MjdFNTYwMzc1ODJDYjhiN2IiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2Njg4OTI3OTA4MTksIm5hbWUiOiIweFJveWFsdHkifQ.hYcfthHC-RBtHdDV28jdAksdiksfn370eRnZY5VHkak'

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
    orgs = [ {'name': 'Uniswap', 'github': 'https://github.com/Uniswap', 'volume': 625097885756.9067},
            {'name': 'Curve', 'github': 'https://github.com/curvefi', 'volume': 150521694077.0348},
            {'name': 'Sushiswap', 'github': 'https://github.com/sushiswap', 'volume': 49040293844.09633},
            {'name': 'Balancer', 'github': 'https://github.com/balancer-labs', 'volume': 28457489366.547653},
            {'name': 'DODO', 'github': 'https://github.com/DODOEX', 'volume': 23455259013.630615},
            {'name': '0x Native', 'github': 'https://github.com/0xProject', 'volume': 21874199433.42813},
            {'name': 'Synthetix', 'github': 'https://github.com/Synthetixio', 'volume': 10195971505.294567},
            {'name': '1inch Network', 'github': 'https://github.com/1inch', 'volume': 8013047105.629432},
            {'name': 'Bancor', 'github': 'https://github.com/bancorprotocol', 'volume': 6314867108.710405},
            #{'name': 'Shibaswap', 'github': 'https://github.com/KaalDhairya', 'volume': 5694971879.214641},
    ]
    for org in orgs:
        repos = [{'slug': rep} for rep in get_repos(org['github'][19:])]

        print(repos)

        for repo in repos:
            res = get_repo_stat_page(repos[0]['slug'], 100, 1)
            repo['stat'] = res
        
        org['repos'] = repos

    with open('repostat.json', 'w') as f:
        json.dump(orgs, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
    
