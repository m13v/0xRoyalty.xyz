To deploy:
```shell
yarn install
yarn hardhat deploy
```
Add project:
```
yarn hardhat add-project --contract <contract> --name 'Test1' --repolink 'http://something.com' --cid 'bafk2bzaceajz56zudni2hli7id6jvvpo5n4wj5eoxm5xwj2ipthwc2pkgowwu'
```
Update project:
```
yarn hardhat update-project --contract <contract> --id 1 --cid 'bafk2bzaceajz56zudni2hli7id6jvvpo5n4wj5eoxm5xwj2ipthwc2pkgowwu'

```
List of all projects:
```
yarn hardhat get-all --contract <contract>
```