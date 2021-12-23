// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract FundMe {

    mapping(address => uint256) public addressToAmountFunded;
    address owner;

    constructor() public {
        owner = msg.sender;
    }

    function fund() public payable {
        uint256 minimumUsd = 50 * 10 ** 18;
        require(getGWeiConversionRate(msg.value) >= minimumUsd, "You need to spend more ETH!!");

        addressToAmountFunded[msg.sender] += msg.value;
    }

    function getPriceInWei() public view returns(uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x22); //depends on the network we are
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }

    function getGWeiConversionRate(uint256 ethAmount) public view returns(uint256) {
        uint256 ethPrice = getPriceInWei();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }

    modifier onlyOwner {
        require(msg.sender == owner);
        _; //here is where the modified function is executed
    }

    function withdraw() public payable onlyOwner {
        msg.sender.transfer(address(this).balance);
    }
}
