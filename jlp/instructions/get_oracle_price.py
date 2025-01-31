from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
from ..program_id import PROGRAM_ID


class GetOraclePriceAccounts(typing.TypedDict):
    perpetuals: Pubkey
    pool: Pubkey
    custody: Pubkey
    custody_oracle_account: Pubkey
    custody_price_update: Pubkey


def get_oracle_price(
    accounts: GetOraclePriceAccounts,
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
            pubkey=accounts["custody_price_update"], is_signer=False, is_writable=False
        ),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xc8\x14\x00j8\xd2\xe6\x8c"
    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
