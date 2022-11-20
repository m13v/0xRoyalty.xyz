import json

with open(r'0xRoyalty.xyz\parser\repostat.json', 'r', encoding='utf-8') as f:
    orgs = json.load(f)

global_users = {}

for org in orgs:
    print(org['name'])
    volume = org['volume']
    repos = org['repos']
    org_total = 0
    for repo in repos:
        print(repo['slug'])
        repo_total = 0
        users = repo['stat']
        for user in users:
            contrib = user['contributions']
            repo_total += contrib
        repo['repo_total'] = repo_total
        org_total += repo_total
        print(repo_total)
    org['org_total'] = org_total
    print(org_total)
    
    


for org in orgs:
    volume = org['volume']
    repos = org['repos']
    org_total = org['org_total']
    for repo in repos:
        repo_total = repo['repo_total']
        users = repo['stat']
        for user in users:
            contrib = user['contributions']
            if user['type'] != 'User':
                break
            if user['login'] not in global_users.keys():
                global_users[user['login']] = volume/repo_total*contrib*repo_total/org_total
            else:
                global_users[user['login']] += volume/repo_total*contrib*repo_total/org_total
    
dict(sorted(global_users.items(), key=lambda item: item[1], reverse=True))
print(global_users)

for (login, value) in global_users.items():
    global_users['login'] = round(value)

with open('leaderboard.json', 'w') as f:
    json.dump(global_users, f, ensure_ascii=False, indent=4)
