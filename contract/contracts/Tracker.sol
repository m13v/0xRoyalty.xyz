pragma solidity ^0.8.0;

import "./filecoinMockAPIs/types/MarketTypes.sol";
import "./filecoinMockAPIs/MarketAPI.sol";

contract Tracker {

    address marketApiAddress;

    struct Project {
        uint id;
        string name;
        string repoLink;
        bytes cid; //CID with revenue/fees/list of contributors, contributions etc.
    }

    mapping(uint => Project) public projects;
    uint projectsCount;

    address payable public owner;

    constructor(address _marketApiAddress) {
        marketApiAddress = _marketApiAddress;
        owner = payable(msg.sender);
    }

    function add(string calldata name, string calldata repoLink, bytes calldata cid) public returns (uint) {
        //require(msg.sender == owner, "only owner could update"); TODO should be validated, but disabled for test and demonstration
        projectsCount++;
        Project memory project;
        project.id = projectsCount;
        project.name = name;
        project.repoLink = repoLink;
        project.cid = cid;
        projects[projectsCount] = project;
        return projectsCount;
    }

    function updateCid(uint16 id, bytes calldata cid) public {
        //require(msg.sender == owner, "only owner could update"); TODO should be validated, but disabled for test and demonstration
        Project storage project = projects[id];
        project.cid = cid;
    }

    function allProjects() public view returns (Project[] memory) {
        Project[] memory result = new Project[](projectsCount);
        for (uint i = 0; i < projectsCount; i++) {
            result[i] = projects[i];
        }
        return result;
    }

    function market_add_balance(string memory addr) public {
        //require(msg.sender == owner, "only owner could update"); TODO should be validated, but disabled for test and demonstration
        MarketAPI marketApiInstance = MarketAPI(marketApiAddress);

        MarketTypes.AddBalanceParams memory params = MarketTypes.AddBalanceParams(addr);

        marketApiInstance.add_balance(params);
    }

    function get_balance(string memory addr) public view returns (MarketTypes.GetBalanceReturn memory) {
        MarketAPI marketApiInstance = MarketAPI(marketApiAddress);

        MarketTypes.GetBalanceReturn memory response = marketApiInstance.get_balance(addr);
        return response;
    }

    function market_withdraw_balance(string memory addr, uint256 tokenAmount) public returns (MarketTypes.WithdrawBalanceReturn memory) {
        //require(msg.sender == owner, "only owner could update"); TODO should be validated, but disabled for test and demonstration
        MarketAPI marketApiInstance = MarketAPI(marketApiAddress);

        MarketTypes.WithdrawBalanceParams memory params = MarketTypes.WithdrawBalanceParams(addr, tokenAmount);

        MarketTypes.WithdrawBalanceReturn memory response = marketApiInstance
        .withdraw_balance(params);
        return response;
    }
}
