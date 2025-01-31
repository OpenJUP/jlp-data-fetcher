from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class IncreasePositionInfoJSON(typing.TypedDict):
    price: int
    liquidation_price: int
    fee_usd: int
    collateral_usd: int


@dataclass
class IncreasePositionInfo:
    layout: typing.ClassVar = borsh.CStruct(
        "price" / borsh.U64,
        "liquidation_price" / borsh.U64,
        "fee_usd" / borsh.U64,
        "collateral_usd" / borsh.U64,
    )
    price: int
    liquidation_price: int
    fee_usd: int
    collateral_usd: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "IncreasePositionInfo":
        return cls(
            price=obj.price,
            liquidation_price=obj.liquidation_price,
            fee_usd=obj.fee_usd,
            collateral_usd=obj.collateral_usd,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "price": self.price,
            "liquidation_price": self.liquidation_price,
            "fee_usd": self.fee_usd,
            "collateral_usd": self.collateral_usd,
        }

    def to_json(self) -> IncreasePositionInfoJSON:
        return {
            "price": self.price,
            "liquidation_price": self.liquidation_price,
            "fee_usd": self.fee_usd,
            "collateral_usd": self.collateral_usd,
        }

    @classmethod
    def from_json(cls, obj: IncreasePositionInfoJSON) -> "IncreasePositionInfo":
        return cls(
            price=obj["price"],
            liquidation_price=obj["liquidation_price"],
            fee_usd=obj["fee_usd"],
            collateral_usd=obj["collateral_usd"],
        )
