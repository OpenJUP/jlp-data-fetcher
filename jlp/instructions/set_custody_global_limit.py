from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class SetCustodyGlobalLimitArgs(typing.TypedDict):
    params: types.set_custody_global_limit_params.SetCustodyGlobalLimitParams


layout = borsh.CStruct(
    "params" / types.set_custody_global_limit_params.SetCustodyGlobalLimitParams.layout
)


class SetCustodyGlobalLimitAccounts(typing.TypedDict):
    keeper: Pubkey
    custody: Pubkey


def set_custody_global_limit(
    args: SetCustodyGlobalLimitArgs,
    accounts: SetCustodyGlobalLimitAccounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["keeper"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["custody"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"^R\x9a\xb1\xc1\xcd\x8dL"
    encoded_args = layout.build(
        {
            "params": args["params"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
