from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class GetExactOutSwapAmountAndFeesParamsJSON(typing.TypedDict):
    amount_out: int


@dataclass
class GetExactOutSwapAmountAndFeesParams:
    layout: typing.ClassVar = borsh.CStruct("amount_out" / borsh.U64)
    amount_out: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "GetExactOutSwapAmountAndFeesParams":
        return cls(amount_out=obj.amount_out)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"amount_out": self.amount_out}

    def to_json(self) -> GetExactOutSwapAmountAndFeesParamsJSON:
        return {"amount_out": self.amount_out}

    @classmethod
    def from_json(
        cls, obj: GetExactOutSwapAmountAndFeesParamsJSON
    ) -> "GetExactOutSwapAmountAndFeesParams":
        return cls(amount_out=obj["amount_out"])
