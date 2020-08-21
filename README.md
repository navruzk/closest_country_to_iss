# Find the closest country to the International Space Station

It is fun game built on ethereum blockchain.

## Getting Started

This is blockchain based fun game. 

Game starts with users sending the name of location on earth that is the closest to ISS.
Users can view latitude and longitude of ISS by calling viewLongitude() and viewLatitude() functions of the contract.
They are view functions so no trasactions happen and users will not spend test ether.

Users can submit answer by calling sendAnswer(area_code). Area code should be ISO 3166 2 letter code. 
If the ISS is close to some area of some country but that area is not close to cities user should submit 'nc'.

Contract checks and rewards users by sending 1000 "GeographyGeniusToken". It is ERC20 token and could be send to other users as well.
I will upload the ERC721 token based modification soon.

Contracts are in .sol files. And contract updaters and markerers are in .py files.

User needs the brownie framework to build more interesting apps on top of this. 

After installing the brownie, create a new folder and run from that folder 

```bash
brownie init
```

The code above creates a new project. Move .sol files from this repo to contract folder in that new project folder. 
Move .py files from this repo to scripts folder in that new project folder.

Now user needs to compile .sol files.

```bash
brownie compile
```

Now brownie console could be open for development.

```bash
brownie console
```

### Installing

Solidity scripts (.sol) can be used to deploy smart contracts in ethereum testnets.
Or user can build more interesting applications on top of this.

## Built With

* [Brownie](https://eth-brownie.readthedocs.io/en/stable/) - The smart contract development framework used
* [Python](https://python.org/) - Python

## Authors

[navruz](https://github.com/navruzbek1992)

