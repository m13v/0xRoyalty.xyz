import './App.css'
//importing table ux/ui
import MyCompanent from "./myCompanent.jsx";
//import { ConnectWallet, useAddress } from "@thirdweb-dev/react";
import Metamask from './Metamask'

export default function App() {
 // const address = useAddress();
  return (
    <main>
      <h1>
        {"Trustless reputation and royalty algorithm for developers in web3"}
      </h1>
      <h2>{"[STEP 1] We believe top web3 developers deserve more credit."}</h2>
      <p>{"Let’s name the ones who contributed the most to web3!"}</p>
      <p>
        {
          "as a first step we have linked DEX protocols volume and their Github repos contributors"
        }
      </p>
      <h2>{"[STEP 2] We want to bring royalties to developers."}</h2>
      <p>
        {
          "If developers contribute to open source projects which are forked and generate profit, they must pay back original contibutors"
        }
      </p>
      <h2>{"Leaderboard"}</h2> 
      <Metamask />   
      <MyCompanent />
      React ⚛️ + Vite ⚡ + Replit 🌀
    </main>
  )
}