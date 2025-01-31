from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class GetAssetsUnderManagementArgs(typing.TypedDict):
    params: types.get_assets_under_management_params.GetAssetsUnderManagementParams


layout = borsh.CStruct(
    "params"
    / types.get_assets_under_management_params.GetAssetsUnderManagementParams.layout
)


class GetAssetsUnderManagementAccounts(typing.TypedDict):
    perpetuals: Pubkey
    pool: Pubkey


def get_assets_under_management(
    args: GetAssetsUnderManagementArgs,
    accounts: GetAssetsUnderManagementAccounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["perpetuals"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["pool"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b",\x03\xa1E\xaeK\x89\xa2"
    encoded_args = layout.build(
        {
            "params": args["params"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
