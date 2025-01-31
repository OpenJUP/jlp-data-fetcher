from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class SwapExactOutParamsJSON(typing.TypedDict):
    amount_out: int
    max_amount_in: int


@dataclass
class SwapExactOutParams:
    layout: typing.ClassVar = borsh.CStruct(
        "amount_out" / borsh.U64, "max_amount_in" / borsh.U64
    )
    amount_out: int
    max_amount_in: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "SwapExactOutParams":
        return cls(amount_out=obj.amount_out, max_amount_in=obj.max_amount_in)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"amount_out": self.amount_out, "max_amount_in": self.max_amount_in}

    def to_json(self) -> SwapExactOutParamsJSON:
        return {"amount_out": self.amount_out, "max_amount_in": self.max_amount_in}

    @classmethod
    def from_json(cls, obj: SwapExactOutParamsJSON) -> "SwapExactOutParams":
        return cls(amount_out=obj["amount_out"], max_amount_in=obj["max_amount_in"])
