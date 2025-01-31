from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class GetSwapAmountAndFeesParamsJSON(typing.TypedDict):
    amount_in: int


@dataclass
class GetSwapAmountAndFeesParams:
    layout: typing.ClassVar = borsh.CStruct("amount_in" / borsh.U64)
    amount_in: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "GetSwapAmountAndFeesParams":
        return cls(amount_in=obj.amount_in)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"amount_in": self.amount_in}

    def to_json(self) -> GetSwapAmountAndFeesParamsJSON:
        return {"amount_in": self.amount_in}

    @classmethod
    def from_json(
        cls, obj: GetSwapAmountAndFeesParamsJSON
    ) -> "GetSwapAmountAndFeesParams":
        return cls(amount_in=obj["amount_in"])
