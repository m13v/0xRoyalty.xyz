pragma solidity ^0.8.0;

contract Tracker {

    struct Project {
        uint id;
        string name;
        string repoLink;
        bytes cid; //CID with revenue/fees/list of contributors, contributions etc.
    }

    mapping(uint => Project) public projects;
    uint projectsCount;

    address payable public owner;

    constructor() {
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
}
