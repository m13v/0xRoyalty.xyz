task("update-project", "Calls the tracker Contract to read all projects data.")
  .addParam("contract", "The address the tracker contract")
  .addParam("id", "id of the project")
  .addParam("cid", "cid with metadata")
  .setAction(async (taskArgs) => {
    const contractAddr = taskArgs.contract
    const id = taskArgs.id
    const cid = taskArgs.cid
    const networkId = network.name
    console.log("Updating project on network ", networkId)
    const Tracker = await ethers.getContractFactory("Tracker")

    //Get signer information
    const accounts = await ethers.getSigners()
    const signer = accounts[0]

    const trackerContract = new ethers.Contract(contractAddr, Tracker.interface, signer)
    let result = BigInt(await trackerContract.updateCid(id, ethers.utils.toUtf8Bytes(cid))).toString()
    console.log("Project id is: ", result)
  })

module.exports = {}