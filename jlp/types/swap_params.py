from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class SwapParamsJSON(typing.TypedDict):
    amount_in: int
    min_amount_out: int


@dataclass
class SwapParams:
    layout: typing.ClassVar = borsh.CStruct(
        "amount_in" / borsh.U64, "min_amount_out" / borsh.U64
    )
    amount_in: int
    min_amount_out: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "SwapParams":
        return cls(amount_in=obj.amount_in, min_amount_out=obj.min_amount_out)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"amount_in": self.amount_in, "min_amount_out": self.min_amount_out}

    def to_json(self) -> SwapParamsJSON:
        return {"amount_in": self.amount_in, "min_amount_out": self.min_amount_out}

    @classmethod
    def from_json(cls, obj: SwapParamsJSON) -> "SwapParams":
        return cls(amount_in=obj["amount_in"], min_amount_out=obj["min_amount_out"])
