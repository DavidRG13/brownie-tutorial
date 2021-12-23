// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    struct Person {
        uint256 favouriteNumber;
        string name;
    }
    Person[] public people;

    mapping(string => uint256) public nameToFav;

    uint256 public favouriteNumber;

    function store(uint256 _favouriteNumber) public {
        favouriteNumber = _favouriteNumber;
    }

    function get() public view returns (uint256) {
        return favouriteNumber;
    }

    function compute(uint256 number) public pure {
        number + number;
    }

    function addPerson(string memory _name, uint256 _favouriteNumber) public {
        people.push(Person({favouriteNumber: _favouriteNumber, name: _name}));
        nameToFav[_name] = _favouriteNumber;
    }
}
