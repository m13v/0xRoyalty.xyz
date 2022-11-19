task("get-all", "Calls the tracker Contract to read all projects data.")
  .addParam("contract", "The address the tracker contract")
  .setAction(async (taskArgs) => {
    const contractAddr = taskArgs.contract
    const networkId = network.name
    console.log("Reading all projects data on network ", networkId)
    const Tracker = await ethers.getContractFactory("Tracker")

    //Get signer information
    const accounts = await ethers.getSigners()
    const signer = accounts[0]

    const trackerContract = new ethers.Contract(contractAddr, Tracker.interface, signer)
    let result = BigInt(await trackerContract.allProjects()).toString()
    console.log("Data is: ", result)
  })

module.exports = {}