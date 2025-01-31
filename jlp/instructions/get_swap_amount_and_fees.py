from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class GetSwapAmountAndFeesArgs(typing.TypedDict):
    params: types.get_swap_amount_and_fees_params.GetSwapAmountAndFeesParams


layout = borsh.CStruct(
    "params" / types.get_swap_amount_and_fees_params.GetSwapAmountAndFeesParams.layout
)


class GetSwapAmountAndFeesAccounts(typing.TypedDict):
    perpetuals: Pubkey
    pool: Pubkey
    receiving_custody: Pubkey
    receiving_custody_oracle_account: Pubkey
    dispensing_custody: Pubkey
    dispensing_custody_oracle_account: Pubkey


def get_swap_amount_and_fees(
    args: GetSwapAmountAndFeesArgs,
    accounts: GetSwapAmountAndFeesAccounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["perpetuals"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["pool"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["receiving_custody"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["receiving_custody_oracle_account"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(
            pubkey=accounts["dispensing_custody"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["dispensing_custody_oracle_account"],
            is_signer=False,
            is_writable=False,
        ),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xf7y(c#Rd "
    encoded_args = layout.build(
        {
            "params": args["params"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
