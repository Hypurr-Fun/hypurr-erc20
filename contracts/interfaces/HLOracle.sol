// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface SystemOracle {
    function getMarkPxs() external view returns (uint[] memory);

    function getOraclePxs() external view returns (uint[] memory);

    function getSpotPxs() external view returns (uint[] memory);
}