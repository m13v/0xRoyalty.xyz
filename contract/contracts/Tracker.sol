pragma solidity ^0.8.0;

contract Tracker {

    struct Project {
        uint16 id;
        string name;
        string repoLink;
        bytes cid; //CID with revenue/fees/list of contributors and contributions
    }

    mapping(uint16 => Project) public projects;

    address payable public owner;

    constructor() {
        owner = payable(msg.sender);
    }

    function update(uint16 id, string name, string repoLink, bytes cid) public {
        //require(msg.sender == owner, "only owner could update"); TODO should be validated, but disabled for test and demonstration
        Project memory project;
        project.id = id;
        project.name = name;
        project.repoLink = repoLink;
        project.cid = cid;
        projects[id].push(project);
    }

    function allProjects() public view returns (mapping(uint16 => Project)) {
        return projects;
    }
}
