
pragma solidity >=0.5.0 <=0.6.2;

import "OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/access/Ownable.sol";
import "./GeographyGeniusToken.sol";

abstract contract GeographyGeniusTokenInterface {
  function balanceOf(address tokenOwner) virtual public returns (uint);
  function transferFrom(address owner, address buyer, uint numTokens) virtual public returns (bool);
}

contract GeographyGenius is Ownable {

  string latitude;
  string longitude;
  string country_name;

  uint private randNonce = 0;
  uint private modulus = 1000;

  struct SubmissionInfo {
    address _address;
    uint _submitted_time;
    string _answer;
  }
  
  uint [] submissionList;

  mapping(uint256 => SubmissionInfo) submissionInfo;

  event UpdateDataEvent(string _longitude_data, string _latitude_data, string _country_name);

  function submitAnswer(string memory _answer) public {

      randNonce++;
      uint id = uint(keccak256(abi.encodePacked(now, msg.sender, randNonce))) % modulus;

      submissionList.push(id);

      SubmissionInfo[id]._address = msg.sender;
      SubmissionInfo[id]._submitted_time = now;
      SubmissionInfo[id]._answer = _answer;
  }

  function viewLatitudeData() public view returns (string memory) {
    return latitude;
  }

  function viewLongitudeData() public view returns (string memory) {
    return longitude;
  }

  function getSubmissionList() public view onlyOwner returns (uint [] memory) {
      return submissionList;
  }

  function getCountryName() public view onlyOwner returns (string memory){
    return country_name;
  }

  function getSubmissionInfo_address(uint256 _id) public view onlyOwner returns (address _address){
    return submissionInfo[_id]._address;
  }

  function getSubmissionInfo_answer(uint256 _id) public view onlyOwner returns (string _id){
    return submissionInfo[_id]._answer;
  }

  function updateData(string memory _longitude_data, string memory _latitude_data, string memory _country_name) public onlyOwner {

    latitude = _latitude_data;
    longitude = _longitude_data;
    country_name = _country_name;

    emit UpdateDataEvent(_longitude_data, _latitude_data, _country_name);
  }

  function destroy() public onlyOwner {
      selfdestruct(msg.sender);
  }
}
