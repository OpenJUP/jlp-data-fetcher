from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class DecreasePositionPostSwapArgs(typing.TypedDict):
    params: types.decrease_position_post_swap_params.DecreasePositionPostSwapParams


layout = borsh.CStruct(
    "params"
    / types.decrease_position_post_swap_params.DecreasePositionPostSwapParams.layout
)


class DecreasePositionPostSwapAccounts(typing.TypedDict):
    keeper: Pubkey
    position_request: Pubkey
    position_request_ata: Pubkey
    event_authority: Pubkey
    program: Pubkey


def decrease_position_post_swap(
    args: DecreasePositionPostSwapArgs,
    accounts: DecreasePositionPostSwapAccounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["keeper"], is_signer=True, is_writable=False),
        AccountMeta(
            pubkey=accounts["position_request"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["position_request_ata"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["event_authority"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["program"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"K\xf6\xd0\x07\xcbBj["
    encoded_args = layout.build(
        {
            "params": args["params"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)
