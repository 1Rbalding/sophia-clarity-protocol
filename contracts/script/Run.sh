# add to .env: ORIGINATOR_EOA, CLAIMS_EOA, ... PUBLIC_COMPUTER_EOA, TERM_SECONDS
forge script script/GrantRoles.s.sol:GrantRolesScript \
  --rpc-url $RPC_URL --broadcast -vvvv