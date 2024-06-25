// SPDX-License-Identifier: MIT
pragma solidity ^0.8.1;

import "OpenZeppelin/openzeppelin-contracts@5.0.2/contracts/token/ERC20/ERC20.sol";


contract HLERC20 is ERC20 {
    uint256 _totalSupply;
    uint8 _decimals;

    constructor(string memory name_, string memory symbol_, uint256 totalSupply_, uint8 decimals_) ERC20(name_, symbol_) {
        _mint(0x2222222222222222222222222222222222222222, totalSupply_);
        _decimals = decimals_;
    }

    function decimals() public view virtual override returns (uint8) {
        return _decimals;
    }
}
