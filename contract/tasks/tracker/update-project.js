const util = require("util");
const request = util.promisify(require("request"));

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
    const priorityFee = await callRpc("eth_maxPriorityFeePerGas")

    async function callRpc(method, params) {
      var options = {
          method: "POST",
          url: "https://wallaby.node.glif.io/rpc/v0",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify({
              jsonrpc: "2.0",
              method: method,
              params: params,
              id: 1,
          }),
      };
      const res = await request(options);
      return JSON.parse(res.body).result;
    }

    //Get signer information
    const accounts = await ethers.getSigners()
    const signer = accounts[0]

    const trackerContract = new ethers.Contract(contractAddr, Tracker.interface, signer)
    let result = (await trackerContract.updateCid(id, ethers.utils.toUtf8Bytes(cid), {
        gasLimit: 1000000000,
        maxPriorityFeePerGas: priorityFee
    })).toString()
    console.log("Project id is: ", result)
  })

module.exports = {}