from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class LiquidateFullPosition2Args(typing.TypedDict):
    params: types.liquidate_full_position2_params.LiquidateFullPosition2Params


layout = borsh.CStruct(
    "params" / types.liquidate_full_position2_params.LiquidateFullPosition2Params.layout
)


class LiquidateFullPosition2Accounts(typing.TypedDict):
    signer: Pubkey
    perpetuals: Pubkey
    pool: Pubkey
    position: Pubkey
    custody: Pubkey
    custody_oracle_account: Pubkey
    collateral_custody: Pubkey
    collateral_custody_oracle_account: Pubkey
    collateral_custody_token_account: Pubkey
    custody_price_update: Pubkey
    collateral_custody_price_update: Pubkey
    event_authority: Pubkey
    program: Pubkey


def liquidate_full_position2(
    args: LiquidateFullPosition2Args,
    accounts: LiquidateFullPosition2Accounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["signer"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["perpetuals"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["pool"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["position"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["custody"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["custody_oracle_account"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["collateral_custody"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["collateral_custody_oracle_account"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["collateral_custody_token_account"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["custody_price_update"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["collateral_custody_price_update"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["event_authority"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["program"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xe9\xa0\xbbb\x02\xea0\xf9"
    encoded_args = layout.build(
        {
            "params": args["params"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
