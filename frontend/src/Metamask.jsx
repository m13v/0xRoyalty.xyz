import React, { Component } from 'react';
import Tracker from "./Tracker.json";
import { ethers } from "ethers";

class Metamask extends Component {
    constructor(props) {
        super(props);
        this.state = {
        };
    }

    async connectToMetamask() {
        console.log('connecting to contract')
        const provider = new ethers.providers.JsonRpcProvider('https://wallaby.node.glif.io/rpc/v0')
        
        const contract_address = '0xcED7B64Dc3F4ef7a2FdcF9A1937FA389E37dc639'

        const trackerContract = new ethers.Contract(contract_address, Tracker, provider)
        console.log('Connected contract:')
        console.log(trackerContract)
        let contract_data = await trackerContract.allProjects()
        console.log("Projects are: ", contract_data)

        this.setState({ selectedAddress: contract_address, contract_data: contract_data.toString() })
        this.renderMetamask()

        // const provider = new ethers.providers.Web3Provider(window.ethereum)
        //const accounts = await provider.send("eth_requestAccounts", []);
        //this.setState({ selectedAddress: accounts[0] })       
        //const Tracker = await ethers.getContractFactory("SimpleCoin")
        //console.log('factory')
        //accounts = await ethers.getSigners()
        //const signer = accounts[0]
        //const daiContract = new ethers.Contract(contract_address, Tracker, provider);
        //const tokenName = await daiContract.name();
        //const tokenBalance = await daiContract.balanceOf(accounts[0]);
        //const tokenUnits = await daiContract.decimals();
        //const tokenBalanceInEther = ethers.utils.formatUnits(tokenBalance, tokenUnits);
    }

    renderMetamask() {
        if (!this.state.selectedAddress) {
            return (
                <button onClick={() => this.connectToMetamask()}>Update the list from IPFS</button>
            )
        } else {
            return (
                <div>
                    <p>Welcome {this.state.selectedAddress}</p>
                    <p>Balance is {this.state.contract_data} coins</p>
                </div>
            );
        }
    }

    render() {
        return (
            <div>
                {this.renderMetamask()}
            </div>
        )
    }
}

export default Metamask;