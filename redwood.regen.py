#!/usr/bin/env python
"""
Genesis modification script on a stateful genesis file.
This example will turn a genesis file exported from mainnet
into the genesis used for theta-testnet-001.
Usage:
$ ./genesis_theta.py
"""
from cosmos_genesis_tinker import Delegator, Validator, GenesisTinker

GENESIS_ARCHIVE = "export.json"

NEW_CHAIN_ID = "redwood-test"

# Tokens configuration
UATOM_STAKE_INCREASE = 550000000 * 1000000
UATOM_LIQUID_TOKEN_INCREASE = 175000000 * 1000000

THETA_LIQUID_TOKEN_INCREASE = 1000
RHO_LIQUID_TOKEN_INCREASE = 1000
LAMBDA_LIQUID_TOKEN_INCREASE = 1000
EPSILON_LIQUID_TOKEN_INCREASE = 1000

# The Coinbase validator is being replaced with the earth node
cb_val = Validator()
cb_val.self_delegation_address = "regen15cea7lrp06c86hc3azzm0ffuvuya4e62aj2vyn"
cb_val.self_delegation_public_key = "AkQhy8wCnpKurglghnNCe0Oremu8mqqRyCNh+8T52sss"
cb_val.operator_address = "regenvaloper15cea7lrp06c86hc3azzm0ffuvuya4e62p4hfuz"
cb_val.public_key = "nUzWRiQMZEGTXgQF3jRfHqJMrboyFvGBsZE+uNtY21o="
cb_val.address = "02AE0B322F74633CE9E07DF248F116E826B4036A"
cb_val.consensus_address = "regenvalcons1q2hqkv30w33ne60q0hey3ugkaqntgqm2mxx8qq"


do_val = Validator()
do_val.self_delegation_address = "regen1hjr5ukxfxqlcef363an2snd0wgsnkte0xh8wmr"
do_val.self_delegation_public_key = "AxbWeFgCNOGpaLSKHNc7zQaVDWn+vcpRGMzoowpqTZyh"
do_val.operator_address = "regenvaloper1hjr5ukxfxqlcef363an2snd0wgsnkte06s6trj"
do_val.public_key = "vG+k+Nqk+tQoQgIsxelgJ5lwB289TUXOwVa/B8HMpcI="
do_val.address = "3550F8C14AA9C8B639EBC028CDD9C6125CBFECCF"
do_val.consensus_address = "regenvalcons1x4g03s2248ytvw0tcq5vmkwxzfwtlmx0es9vrg"



earth_val = Validator()
earth_val.self_delegation_address = "regen1j6vhmzwtsu72wrm53vfhrhtj5dnng2dlml7k0d"
earth_val.self_delegation_public_key = "AlzrXgtStV3NYlZ6A0rLySyocl0w9lrmIAQyyDemiXRY"
earth_val.operator_address = "regenvaloper1j6vhmzwtsu72wrm53vfhrhtj5dnng2dl8crnhu"
earth_val.public_key = "+7ANNUY/ovnnj6FcY1j0qnPn1khd+5Xaeln427emR/w="
earth_val.address = "BA082CBBBA1795740764CD29DA763588891A71BF"
earth_val.consensus_address = "regenvalcons1hgyzewa6z72hgpmye55a5a343zy35udl6ttucl"

two_val = Validator()
two_val.self_delegation_address = "regen16atcve2pn9x46xmrdktjlvgzqj0efxgccj0clz"
two_val.self_delegation_public_key = "A5uZT9T06ADwQud3QxpRxXIcdaW3stmCnwXkLxJvX8uM"
two_val.operator_address = "regenvaloper16atcve2pn9x46xmrdktjlvgzqj0efxgcy4ja8n"
two_val.public_key = "lmzZtzHngZxNrj8oFc0AMhdqH3n3X5DUCfAFNmtTYI4="
two_val.address = "2CBC8BDA44F04E367B8A89FEF0A874B32FEC6342"
two_val.consensus_address = "regenvalcons19j7ghkjy7p8rv7u238l0p2r5kvh7cc6zf6cypp"



print("Tinkering...")
gentink = GenesisTinker(input_file=GENESIS_ARCHIVE)

gentink.add_task(gentink.replace_validator,
                 old_validator=cb_val,
                 new_validator=earth_val)

gentink.add_task(gentink.replace_validator,
                 old_validator=do_val,
                 new_validator=two_val)


gentink.add_task(gentink.set_chain_id,
                 chain_id=NEW_CHAIN_ID)


# Set new governance parameters for convenience
gentink.add_task(gentink.set_min_deposit,
                 min_amount='1',
                 denom='uregen')
gentink.add_task(gentink.set_tally_param,
                 parameter_name='quorum',
                 value='0.000000000000000001')
gentink.add_task(gentink.set_tally_param,
                 parameter_name='threshold',
                 value='0.000000000000000001')
gentink.add_task(gentink.set_voting_period,
                 voting_period='300s')

# Make redelegations faster
gentink.add_task(gentink.set_unbonding_time,
                 unbonding_time='1s')


gentink.run_tasks()
