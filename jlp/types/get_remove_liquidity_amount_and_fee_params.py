from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class GetRemoveLiquidityAmountAndFeeParamsJSON(typing.TypedDict):
    lp_amount_in: int


@dataclass
class GetRemoveLiquidityAmountAndFeeParams:
    layout: typing.ClassVar = borsh.CStruct("lp_amount_in" / borsh.U64)
    lp_amount_in: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "GetRemoveLiquidityAmountAndFeeParams":
        return cls(lp_amount_in=obj.lp_amount_in)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"lp_amount_in": self.lp_amount_in}

    def to_json(self) -> GetRemoveLiquidityAmountAndFeeParamsJSON:
        return {"lp_amount_in": self.lp_amount_in}

    @classmethod
    def from_json(
        cls, obj: GetRemoveLiquidityAmountAndFeeParamsJSON
    ) -> "GetRemoveLiquidityAmountAndFeeParams":
        return cls(lp_amount_in=obj["lp_amount_in"])
