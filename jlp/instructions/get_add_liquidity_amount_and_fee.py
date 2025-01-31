from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class GetAddLiquidityAmountAndFeeArgs(typing.TypedDict):
    params: types.get_add_liquidity_amount_and_fee_params.GetAddLiquidityAmountAndFeeParams


layout = borsh.CStruct(
    "params"
    / types.get_add_liquidity_amount_and_fee_params.GetAddLiquidityAmountAndFeeParams.layout
)


class GetAddLiquidityAmountAndFeeAccounts(typing.TypedDict):
    perpetuals: Pubkey
    pool: Pubkey
    custody: Pubkey
    custody_oracle_account: Pubkey
    lp_token_mint: Pubkey


def get_add_liquidity_amount_and_fee(
    args: GetAddLiquidityAmountAndFeeArgs,
    accounts: GetAddLiquidityAmountAndFeeAccounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["perpetuals"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["pool"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["custody"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["custody_oracle_account"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["lp_token_mint"], is_signer=False, is_writable=False
        ),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xac\x96\xf9\xb5\xe9\xf1N\x8b"
    encoded_args = layout.build(
        {
            "params": args["params"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
