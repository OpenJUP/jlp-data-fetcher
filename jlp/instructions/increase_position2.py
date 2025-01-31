from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from spl.token.constants import TOKEN_PROGRAM_ID
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class IncreasePosition2Args(typing.TypedDict):
    params: types.increase_position2_params.IncreasePosition2Params


layout = borsh.CStruct(
    "params" / types.increase_position2_params.IncreasePosition2Params.layout
)


class IncreasePosition2Accounts(typing.TypedDict):
    keeper: Pubkey
    perpetuals: Pubkey
    pool: Pubkey
    position_request: Pubkey
    position_request_ata: Pubkey
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


def increase_position2(
    args: IncreasePosition2Args,
    accounts: IncreasePosition2Accounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["keeper"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["perpetuals"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["pool"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["position_request"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["position_request_ata"], is_signer=False, is_writable=True
        ),
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
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
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
    identifier = b"\xd7e>d\x98\x0b\x9a="
    encoded_args = layout.build(
        {
            "params": args["params"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
