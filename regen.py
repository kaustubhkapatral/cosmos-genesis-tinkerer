#!/usr/bin/env python
"""
Genesis modification script on a stateful genesis file.
This example will turn a genesis file exported from mainnet
into the genesis used for theta-testnet-001.
Usage:
$ ./genesis_theta.py
"""
from cosmos_genesis_tinker import Delegator, Validator, GenesisTinker

GENESIS_ARCHIVE = "test.json"

NEW_CHAIN_ID = "regen-1"

# Tokens configuration
UATOM_STAKE_INCREASE = 550000000 * 1000000
UATOM_LIQUID_TOKEN_INCREASE = 175000000 * 1000000

THETA_LIQUID_TOKEN_INCREASE = 1000
RHO_LIQUID_TOKEN_INCREASE = 1000
LAMBDA_LIQUID_TOKEN_INCREASE = 1000
EPSILON_LIQUID_TOKEN_INCREASE = 1000

# The Coinbase validator is being replaced with the earth node
cb_val = Validator()
cb_val.self_delegation_address = "regen1ceunjpth8nds7sfmfd9yjmh97vxmwqfy4e70qz"
cb_val.self_delegation_public_key = "AvB8BkC+U9Q8QI/sEZSasjJuPCmoV8Ixq+pMjr6GBHZ/"
cb_val.operator_address = "regenvaloper1ceunjpth8nds7sfmfd9yjmh97vxmwqfyf7r2cn"
cb_val.public_key = "dmRWr9awPjLmuwFoCr9bWmRhYLmva2EuVWxnngL8B8M="
cb_val.address = "E026181D3E76C4846BCCE9443707D2EFB4604B05"
cb_val.consensus_address = "regenvalcons1uqnps8f7wmzgg67va9zrwp7ja76xqjc93ql20m"


do_val = Validator()
do_val.self_delegation_address = "regen1v5hrqlv8dqgzvy0pwzqzg0gxy899rm4k547w43"
do_val.self_delegation_public_key = "AsICOBNYDs+Jyw2UfKbmWmTfXozcpKHHlpG/Lv7cyEkw"
do_val.operator_address = "regenvaloper1v5hrqlv8dqgzvy0pwzqzg0gxy899rm4kgjrtdq"
do_val.public_key = "DC2csM0Nb+dbZfdPMKZXqQOKpifkr4NaDF7B7fcgaRg="
do_val.address = "F4C55E61B92190CB7CD688CCA12E78D21CD940FD"
do_val.consensus_address = "regenvalcons17nz4ucdeyxgvklxk3rx2ztnc6gwdjs8atwjjnz"


ch_val = Validator()
ch_val.self_delegation_address = "regen15urq2dtp9qce4fyc85m6upwm9xul3049re4h4f"
ch_val.self_delegation_public_key = "AoUAnGnBsT7xGv2PTnIQbfK4t4oNyimGk2AhPwfgxq3T"
ch_val.operator_address = "regenvaloper15urq2dtp9qce4fyc85m6upwm9xul3049l7gjdc"
ch_val.public_key = "oceaCqELoCYevpgttA9XXbAHx7D86Traubeg93sBa4o="
ch_val.address = "FC7E26051B1773BA3E39B75019D28C36F66DED5E"
ch_val.consensus_address = "regenvalcons1l3lzvpgmzaem503ekagpn55vxmmxmm27ck7rsl"

ta_val = Validator()
ta_val.self_delegation_address = "regen1zppjyal5emta5cquje8ndkpz0rs046m778mxes"
ta_val.self_delegation_public_key = "AuAyjzS7Rz8kUC7jOhx3rYkTo41s1GKbG9IT7bPsTGs0"
ta_val.operator_address = "regenvaloper1zppjyal5emta5cquje8ndkpz0rs046m7zqxrpp"
ta_val.public_key = "dNO95TeRS9oyZgluL+wETqZE6IVZY/vypyTF7RDbYMg="
ta_val.address = "557F4F7167BF732D698B15E17AA5161AF1CEBD18"
ta_val.consensus_address = "regenvalcons124l57ut8haej66vtzhsh4fgkrtcua0gc4wzn5k"


earth_val = Validator()
earth_val.self_delegation_address = "regen1qwa9xy0997j5mrc4dxn7jrcvvkpm3uwuldkrmg"
earth_val.self_delegation_public_key = "AvnM2dfST0M94PSkoNo2NaI9Jx0CIu4VYIcYd+nTqW83"
earth_val.operator_address = "regenvaloper1qwa9xy0997j5mrc4dxn7jrcvvkpm3uwur2txre"
earth_val.public_key = "6p/aBaVHQwXdNq5uWnbzuD6VwT7xEac+Cuqtj4NNRUg="
earth_val.address = "FA93C9682445DA618F81465AAE6D8B1729A8F939"
earth_val.consensus_address = "regenvalcons1l2fuj6pyghdxrrupged2umvtzu5637feds79lh"

two_val = Validator()
two_val.self_delegation_address = "regen132hlyt0uwnl6sy9esrerdf0gtmhex6ephc2mwq"
two_val.self_delegation_public_key = "AxVOZW2fPjMNrGlrhaAMp+z/b0ynivpaLvYZVrWtxN3t"
two_val.operator_address = "regenvaloper132hlyt0uwnl6sy9esrerdf0gtmhex6eptlh7k3"
two_val.public_key = "wjzZC6eu0gZAmCilv02elkKHPBfjiJFqzEuaP7VI+TI="
two_val.address = "8D9FA05784C4D715EC1992053F7A24C4AB90EED4"
two_val.consensus_address = "regenvalcons13k06q4uycnt3tmqejgzn773ycj4epmk5ydme3g"

thr_val = Validator()
thr_val.self_delegation_address = "regen108fuazrugwhvf9sxknn2r5nyv24vaetaensyhc"
thr_val.self_delegation_public_key = "AyqNQ+/abYo+K+ojOn/OtuO/ZmfjKGAyEsJF1ICv2ntD"
thr_val.operator_address = "regenvaloper108fuazrugwhvf9sxknn2r5nyv24vaeta95dp0f"
thr_val.public_key = "YcXqTgVTFF4REYQvqNqtWEIYdQu41WO2qYrUOysKheo="
thr_val.address = "B5A2BC28ECBB45F73FA27305A07BDBE36DD497E3"
thr_val.consensus_address = "regenvalcons1kk3tc28vhdzlw0azwvz6q77mudkaf9lrzthwgd"

fo_val = Validator()
fo_val.self_delegation_address = "regen1j0wl83ulvwancndjg5jp3r5l2m8jq0fap88ew0"
fo_val.self_delegation_public_key = "AlRNrZa3ere1NviRxtDWJvsKmp0pZ7bm/QD2xmpq+ZVq"
fo_val.operator_address = "regenvaloper1j0wl83ulvwancndjg5jp3r5l2m8jq0faaq6uk7"
fo_val.public_key = "zq4uIOsatCoVCl4RjKE1XtDKqZXeR2CP9zWILLh4L0Y="
fo_val.address = "7C61A4FE055AE13E61BE936CCA58CFFDA031D33B"
fo_val.consensus_address = "regenvalcons103s6fls9ttsnucd7jdkv5kx0lksrr5emrl648q"

earth_del = Delegator()
earth_del.address = "regen1qwa9xy0997j5mrc4dxn7jrcvvkpm3uwuldkrmg"
earth_del.public_key = "AvnM2dfST0M94PSkoNo2NaI9Jx0CIu4VYIcYd+nTqW83"

two_del = Delegator()
two_del.address = "regen132hlyt0uwnl6sy9esrerdf0gtmhex6ephc2mwq"
two_del.public_key = "AxVOZW2fPjMNrGlrhaAMp+z/b0ynivpaLvYZVrWtxN3t"

thr_del = Delegator()
thr_del.address = "regen108fuazrugwhvf9sxknn2r5nyv24vaetaensyhc"
thr_del.public_key = "AyqNQ+/abYo+K+ojOn/OtuO/ZmfjKGAyEsJF1ICv2ntD"

fo_del = Delegator()
fo_del.address = "regen1j0wl83ulvwancndjg5jp3r5l2m8jq0fap88ew0"
fo_del.public_key = "AlRNrZa3ere1NviRxtDWJvsKmp0pZ7bm/QD2xmpq+ZVq"


print("Tinkering...")
gentink = GenesisTinker(input_file=GENESIS_ARCHIVE)

gentink.add_task(gentink.replace_validator,
                 old_validator=cb_val,
                 new_validator=earth_val)

gentink.add_task(gentink.replace_validator,
                 old_validator=do_val,
                 new_validator=two_val)

gentink.add_task(gentink.replace_validator,
                 old_validator=ch_val,
                 new_validator=thr_val)

gentink.add_task(gentink.replace_validator,
                 old_validator=ta_val,
                 new_validator=fo_val)

gentink.add_task(gentink.set_chain_id,
                 chain_id=NEW_CHAIN_ID)


gentink.add_task(gentink.increase_delegator_stake_to_validator,
                 delegator=earth_del,
                 validator=earth_val,
                 increase={'amount': UATOM_STAKE_INCREASE,
                           'denom': 'uregen'})

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
                 voting_period='3600s')

# Make redelegations faster
gentink.add_task(gentink.set_unbonding_time,
                 unbonding_time='1s')


gentink.run_tasks()
