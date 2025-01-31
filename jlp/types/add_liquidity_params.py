from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class AddLiquidityParamsJSON(typing.TypedDict):
    token_amount_in: int
    min_lp_amount_out: int
    token_amount_pre_swap: typing.Optional[int]


@dataclass
class AddLiquidityParams:
    layout: typing.ClassVar = borsh.CStruct(
        "token_amount_in" / borsh.U64,
        "min_lp_amount_out" / borsh.U64,
        "token_amount_pre_swap" / borsh.Option(borsh.U64),
    )
    token_amount_in: int
    min_lp_amount_out: int
    token_amount_pre_swap: typing.Optional[int]

    @classmethod
    def from_decoded(cls, obj: Container) -> "AddLiquidityParams":
        return cls(
            token_amount_in=obj.token_amount_in,
            min_lp_amount_out=obj.min_lp_amount_out,
            token_amount_pre_swap=obj.token_amount_pre_swap,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "token_amount_in": self.token_amount_in,
            "min_lp_amount_out": self.min_lp_amount_out,
            "token_amount_pre_swap": self.token_amount_pre_swap,
        }

    def to_json(self) -> AddLiquidityParamsJSON:
        return {
            "token_amount_in": self.token_amount_in,
            "min_lp_amount_out": self.min_lp_amount_out,
            "token_amount_pre_swap": self.token_amount_pre_swap,
        }

    @classmethod
    def from_json(cls, obj: AddLiquidityParamsJSON) -> "AddLiquidityParams":
        return cls(
            token_amount_in=obj["token_amount_in"],
            min_lp_amount_out=obj["min_lp_amount_out"],
            token_amount_pre_swap=obj["token_amount_pre_swap"],
        )
