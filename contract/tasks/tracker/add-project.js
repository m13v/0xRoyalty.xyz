task("add-project", "Calls the tracker Contract to read all projects data.")
  .addParam("contract", "The address the tracker contract")
  .addParam("name", "The name of the project")
  .addParam("repolink", "The link to the repo of the related project")
  .addParam("cid", "cid with metadata")
  .setAction(async (taskArgs) => {
    const contractAddr = taskArgs.contract
    const name = taskArgs.name
    const repoLink = taskArgs.repolink
    const cid = taskArgs.cid
    const networkId = network.name
    console.log("Adding new project on network ", networkId)
    const Tracker = await ethers.getContractFactory("Tracker")

    //Get signer information
    const accounts = await ethers.getSigners()
    const signer = accounts[0]

    const trackerContract = new ethers.Contract(contractAddr, Tracker.interface, signer)
    let result = BigInt(await trackerContract.add(name, repoLink, ethers.utils.toUtf8Bytes(cid))).toString()
    console.log("Project id is: ", result)
  })

module.exports = {}