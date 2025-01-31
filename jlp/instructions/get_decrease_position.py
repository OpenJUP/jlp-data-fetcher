from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class GetDecreasePositionArgs(typing.TypedDict):
    params: types.get_decrease_position_params.GetDecreasePositionParams


layout = borsh.CStruct(
    "params" / types.get_decrease_position_params.GetDecreasePositionParams.layout
)


class GetDecreasePositionAccounts(typing.TypedDict):
    perpetuals: Pubkey
    pool: Pubkey
    position: Pubkey
    custody: Pubkey
    custody_oracle_account: Pubkey
    collateral_custody: Pubkey
    collateral_custody_oracle_account: Pubkey
    custody_price_update: Pubkey
    collateral_custody_price_update: Pubkey


def get_decrease_position(
    args: GetDecreasePositionArgs,
    accounts: GetDecreasePositionAccounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["perpetuals"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["pool"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["position"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["custody"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["custody_oracle_account"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["collateral_custody"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["collateral_custody_oracle_account"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["custody_price_update"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["collateral_custody_price_update"],
            is_signer=False,
            is_writable=False,
        ),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"j\x1f\x92\xc3gl0\xfa"
    encoded_args = layout.build(
        {
            "params": args["params"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
