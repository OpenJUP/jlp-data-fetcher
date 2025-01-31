from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.system_program import ID as SYS_PROGRAM_ID
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class SetTestOraclePriceArgs(typing.TypedDict):
    params: types.set_test_oracle_price_params.SetTestOraclePriceParams


layout = borsh.CStruct(
    "params" / types.set_test_oracle_price_params.SetTestOraclePriceParams.layout
)


class SetTestOraclePriceAccounts(typing.TypedDict):
    admin: Pubkey
    perpetuals: Pubkey
    pool: Pubkey
    custody: Pubkey
    oracle_account: Pubkey


def set_test_oracle_price(
    args: SetTestOraclePriceArgs,
    accounts: SetTestOraclePriceAccounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["admin"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["perpetuals"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["pool"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["custody"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["oracle_account"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=SYS_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b",o\xa5\xb9:\x0e\xf9\xf9"
    encoded_args = layout.build(
        {
            "params": args["params"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
