/*
 * SPDX-License-Identifier: MIT
 * Midpoint Sample Contract v3.0.0
 *
 * This is a contract generated at 2022-11-19 16:58:52 for testing requests to midpoint 486. 
 * This contract is intended to serve as a guide for interfacing with a midpoint and should not be used
 * as is in a production environment.
 * For more information on setting up a midpoint and using this contract see docs.midpointapi.com
 */

pragma solidity>=0.8.0;

interface IMidpoint {
    function callMidpoint(uint64 midpointId, bytes calldata _data) external returns(uint256 requestId);
}

contract TestMidpoint486Contract {
    // These events can be removed without impacting the functionality of your midpoint
    event RequestMade(uint256 requestId, string repository, string bearer);
    event ResponseReceived(uint256 requestId, string[] login, string[] contributions, string[] id, string[] url, string[] user_type);
    
    // A verified startpoint for an unspecified blockchain (select a blockchain above)
    address constant startpointAddress = 0x9BEa2A4C2d84334287D60D6c36Ab45CB453821eB;
    
    // A verified midpoint callback address for an unspecified blockchain (select a blockchain above)
    address constant whitelistedCallbackAddress = 0xC0FFEE4a3A2D488B138d090b8112875B90b5e6D9;
    
    // The globally unique identifier for your midpoint
    uint64 constant midpointID = 486;
    
    // Mapping of Request ID to a flag that is checked when the request is satisfied
    // This can be removed without impacting the functionality of your midpoint
    mapping(uint256 => bool) public request_id_satisfied;
    
    // Mappings from Request ID to each of your results
    // This can be removed without impacting the functionality of your midpoint
    mapping(uint256 => string[]) public request_id_to_login;
    mapping(uint256 => string[]) public request_id_to_contributions;
    mapping(uint256 => string[]) public request_id_to_id;
    mapping(uint256 => string[]) public request_id_to_url;
    mapping(uint256 => string[]) public request_id_to_user_type;
    
    /*
     * This function makes a call to your midpoint with On-Chain Variables specified as function inputs. 
     * 
     * Note that this is a public function and will allow any address or contract to call midpoint 486.
     * Configure your midpoint to permit calls from this contract when testing. Before using your midpoint
     * in a production environment, ensure that calls to 'callMidpoint' are protected.
     * Any call to 'callMidpoint' from a whitelisted contract will make a call to your midpoint;
     * there may be multiple places in this contract that call the midpoint or multiple midpoints called by the same contract.
     */ 

    function testMidpointRequest(string memory repository, string memory bearer) public {
        // This packs together all of the On-Chain Variables for your midpoint into a single bytestring
        bytes memory args = abi.encodePacked(repository, bytes1(0x00), bearer, bytes1(0x00));
        
        // This makes the call to your midpoint
        uint256 requestId = IMidpoint(startpointAddress).callMidpoint(midpointID, args);

        // This logs that the call has been made, and can be removed without impacting your midpoint
        emit RequestMade(requestId, repository, bearer);
        request_id_satisfied[requestId] = false;
    }
    
   /*
    * This function is the callback target specified in your midpoint callback definition. 
    * Note that the callback is placed in the same contract as the call to callMidpoint for simplicity when testing.
    * The callback does not need to be defined in the same contract as the request or live on the same chain.
    */

   function callback(uint256 _requestId, uint64 _midpointId, string[] memory login, string[] memory contributions, string[] memory id, string[] memory url, string[] memory user_type) public {
       // Only allow a verified callback address to submit information for your midpoint.
       require(tx.origin == whitelistedCallbackAddress, "Invalid callback address");
       // Only allow requests that came from your midpoint ID
       require(midpointID == _midpointId, "Invalid Midpoint ID");
       
       // This stores each of your response variables. This is where you would place any logic associated with your callback.
       // Your midpoint can transact to a callback with arbitrary execution and gas cost.
       request_id_to_login[_requestId] = login;
       request_id_to_contributions[_requestId] = contributions;
       request_id_to_id[_requestId] = id;
       request_id_to_url[_requestId] = url;
       request_id_to_user_type[_requestId] = user_type;
       
       // This logs that a response has been received, and can be removed without impacting your midpoint
       emit ResponseReceived(_requestId, login, contributions, id, url, user_type);
       request_id_satisfied[_requestId] = true;
   }
}
