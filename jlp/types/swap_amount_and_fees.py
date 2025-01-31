from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class SwapAmountAndFeesJSON(typing.TypedDict):
    amount_in: int
    amount_out: int
    fee_bps: int
    fee_token: int


@dataclass
class SwapAmountAndFees:
    layout: typing.ClassVar = borsh.CStruct(
        "amount_in" / borsh.U64,
        "amount_out" / borsh.U64,
        "fee_bps" / borsh.U64,
        "fee_token" / borsh.U64,
    )
    amount_in: int
    amount_out: int
    fee_bps: int
    fee_token: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "SwapAmountAndFees":
        return cls(
            amount_in=obj.amount_in,
            amount_out=obj.amount_out,
            fee_bps=obj.fee_bps,
            fee_token=obj.fee_token,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "amount_in": self.amount_in,
            "amount_out": self.amount_out,
            "fee_bps": self.fee_bps,
            "fee_token": self.fee_token,
        }

    def to_json(self) -> SwapAmountAndFeesJSON:
        return {
            "amount_in": self.amount_in,
            "amount_out": self.amount_out,
            "fee_bps": self.fee_bps,
            "fee_token": self.fee_token,
        }

    @classmethod
    def from_json(cls, obj: SwapAmountAndFeesJSON) -> "SwapAmountAndFees":
        return cls(
            amount_in=obj["amount_in"],
            amount_out=obj["amount_out"],
            fee_bps=obj["fee_bps"],
            fee_token=obj["fee_token"],
        )
