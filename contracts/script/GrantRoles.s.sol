// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "forge-std/Script.sol";
import "forge-std/console.sol";

interface IAccessControlTerm {
    function grantRoleWithTerm(bytes32 role, address account, uint64 termEnd) external;
    function grantRole(bytes32 role, address account) external;
    function hasRole(bytes32 role, address account) external view returns (bool);
}

interface IUpgradeUnlock {
    function setPublicComputer(address computer) external;
}

/**
 * @title GrantRolesScript
 * @notice Grants term-limited operational roles after DeployAll + WireTimelock.
 *
 * Env:
 *   DEPLOYER_PRIVATE_KEY
 *   TERM_SECONDS          (e.g. 31536000 = 1 year)
 *
 *   ORIGINATOR_EOA
 *   CLAIMS_EOA
 *   PRICE_UPDATER_EOA
 *   CREDIT_UPDATER_EOA
 *   VERIFIER_EOA
 *   GUARDIAN_EOA
 *   FUND_MANAGER_EOA
 *   PUBLIC_COMPUTER_EOA
 *
 *   MORTGAGE_CONTROLLER
 *   ORIGINATOR
 *   INSURANCE_POOL
 *   COLLECTIVE_FUND
 *   PRICE_ORACLE
 *   CREDIT_ORACLE
 *   GOVERNANCE_CONTROLLER
 *   UPGRADE_UNLOCK
 *   ARENA (optional)
 */
contract GrantRolesScript is Script {
    bytes32 constant ORIGINATOR_ROLE       = keccak256("ORIGINATOR_ROLE");
    bytes32 constant CLAIMS_ROLE           = keccak256("CLAIMS_ROLE");
    bytes32 constant UPDATER_ROLE          = keccak256("UPDATER_ROLE");
    bytes32 constant PRICE_UPDATER_ROLE    = keccak256("PRICE_UPDATER_ROLE");
    bytes32 constant VERIFIER_ROLE         = keccak256("VERIFIER_ROLE");
    bytes32 constant GUARDIAN_ROLE         = keccak256("GUARDIAN_ROLE");
    bytes32 constant FUND_MANAGER_ROLE     = keccak256("FUND_MANAGER_ROLE");
    bytes32 constant PUBLIC_COMPUTER_ROLE  = keccak256("PUBLIC_COMPUTER_ROLE");
    bytes32 constant FEE_RECEIVER_ROLE     = keccak256("FEE_RECEIVER_ROLE");
    bytes32 constant INSURANCE_ROLE        = keccak256("INSURANCE_ROLE");

    function run() external {
        uint256 pk = vm.envUint("DEPLOYER_PRIVATE_KEY");
        uint256 termSeconds = vm.envOr("TERM_SECONDS", uint256(365 days));
        uint64 termEnd = uint64(block.timestamp + termSeconds);

        address originatorEoa      = vm.envAddress("ORIGINATOR_EOA");
        address claimsEoa          = vm.envAddress("CLAIMS_EOA");
        address priceUpdaterEoa    = vm.envAddress("PRICE_UPDATER_EOA");
        address creditUpdaterEoa   = vm.envAddress("CREDIT_UPDATER_EOA");
        address verifierEoa        = vm.envAddress("VERIFIER_EOA");
        address guardianEoa        = vm.envAddress("GUARDIAN_EOA");
        address fundManagerEoa     = vm.envAddress("FUND_MANAGER_EOA");
        address publicComputerEoa  = vm.envAddress("PUBLIC_COMPUTER_EOA");

        address mortgageController   = vm.envAddress("MORTGAGE_CONTROLLER");
        address originator           = vm.envAddress("ORIGINATOR");
        address insurancePool        = vm.envAddress("INSURANCE_POOL");
        address collectiveFund       = vm.envAddress("COLLECTIVE_FUND");
        address priceOracle          = vm.envAddress("PRICE_ORACLE");
        address creditOracle         = vm.envAddress("CREDIT_ORACLE");
        address governanceController = vm.envAddress("GOVERNANCE_CONTROLLER");
        address upgradeUnlock        = vm.envAddress("UPGRADE_UNLOCK");

        vm.startBroadcast(pk);

        // --- Originator contract may call MortgageController ---
        _grantTerm(mortgageController, ORIGINATOR_ROLE, originator, termEnd);
        _grantTerm(originator, ORIGINATOR_ROLE, originatorEoa, termEnd);

        // --- Claims / hardship ---
        _grantTerm(insurancePool, CLAIMS_ROLE, claimsEoa, termEnd);
        // InsurancePool must be allowed to call applyHardshipSupport
        _grantTerm(mortgageController, INSURANCE_ROLE, insurancePool, termEnd);

        // --- Oracles ---
        _grantTerm(priceOracle, PRICE_UPDATER_ROLE, priceUpdaterEoa, termEnd);
        // fallback if contract uses UPDATER_ROLE only:
        _grantTerm(priceOracle, UPDATER_ROLE, priceUpdaterEoa, termEnd);
        _grantTerm(creditOracle, UPDATER_ROLE, creditUpdaterEoa, termEnd);

        // --- Governance ---
        _grantTerm(governanceController, VERIFIER_ROLE, verifierEoa, termEnd);
        _grantTerm(governanceController, GUARDIAN_ROLE, guardianEoa, termEnd);

        // --- Fund ---
        _grantTerm(collectiveFund, FUND_MANAGER_ROLE, fundManagerEoa, termEnd);

        // --- Public computer (2/3 unlock) ---
        _grantTerm(upgradeUnlock, PUBLIC_COMPUTER_ROLE, publicComputerEoa, termEnd);
        IUpgradeUnlock(upgradeUnlock).setPublicComputer(publicComputerEoa);

        // --- Optional: Arena fee receiver already set in DeployAll; re-assert if needed ---
        // InsurancePool.grantRole(FEE_RECEIVER_ROLE, arena) — done at deploy

        vm.stopBroadcast();

        console.log("========== ROLES GRANTED ==========");
        console.log("Term end (unix):", termEnd);
        console.log("ORIGINATOR_EOA:", originatorEoa);
        console.log("CLAIMS_EOA:", claimsEoa);
        console.log("PRICE_UPDATER_EOA:", priceUpdaterEoa);
        console.log("CREDIT_UPDATER_EOA:", creditUpdaterEoa);
        console.log("VERIFIER_EOA:", verifierEoa);
        console.log("GUARDIAN_EOA:", guardianEoa);
        console.log("FUND_MANAGER_EOA:", fundManagerEoa);
        console.log("PUBLIC_COMPUTER_EOA:", publicComputerEoa);
        console.log("===================================");
        console.log("NEXT: Seed prices, then Testnet Operator Checklist Phase 3");
    }

    function _grantTerm(
        address target,
        bytes32 role,
        address account,
        uint64 termEnd
    ) internal {
        if (account == address(0) || target == address(0)) return;

        // Prefer term-limited API; fall back to plain grantRole if needed
        try IAccessControlTerm(target).grantRoleWithTerm(role, account, termEnd) {
            console.log("grantRoleWithTerm ok");
        } catch {
            IAccessControlTerm(target).grantRole(role, account);
            console.log("grantRole (no term) fallback");
        }
        console.log(account);
    }
}