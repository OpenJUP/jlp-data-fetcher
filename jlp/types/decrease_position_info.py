from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class DecreasePositionInfoJSON(typing.TypedDict):
    price: int
    liquidation_price: int
    fee_usd: int
    collateral_usd: int
    has_profit: bool
    pnl_delta: int
    transfer_amount_usd: int
    transfer_token: int


@dataclass
class DecreasePositionInfo:
    layout: typing.ClassVar = borsh.CStruct(
        "price" / borsh.U64,
        "liquidation_price" / borsh.U64,
        "fee_usd" / borsh.U64,
        "collateral_usd" / borsh.U64,
        "has_profit" / borsh.Bool,
        "pnl_delta" / borsh.U64,
        "transfer_amount_usd" / borsh.U64,
        "transfer_token" / borsh.U64,
    )
    price: int
    liquidation_price: int
    fee_usd: int
    collateral_usd: int
    has_profit: bool
    pnl_delta: int
    transfer_amount_usd: int
    transfer_token: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "DecreasePositionInfo":
        return cls(
            price=obj.price,
            liquidation_price=obj.liquidation_price,
            fee_usd=obj.fee_usd,
            collateral_usd=obj.collateral_usd,
            has_profit=obj.has_profit,
            pnl_delta=obj.pnl_delta,
            transfer_amount_usd=obj.transfer_amount_usd,
            transfer_token=obj.transfer_token,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "price": self.price,
            "liquidation_price": self.liquidation_price,
            "fee_usd": self.fee_usd,
            "collateral_usd": self.collateral_usd,
            "has_profit": self.has_profit,
            "pnl_delta": self.pnl_delta,
            "transfer_amount_usd": self.transfer_amount_usd,
            "transfer_token": self.transfer_token,
        }

    def to_json(self) -> DecreasePositionInfoJSON:
        return {
            "price": self.price,
            "liquidation_price": self.liquidation_price,
            "fee_usd": self.fee_usd,
            "collateral_usd": self.collateral_usd,
            "has_profit": self.has_profit,
            "pnl_delta": self.pnl_delta,
            "transfer_amount_usd": self.transfer_amount_usd,
            "transfer_token": self.transfer_token,
        }

    @classmethod
    def from_json(cls, obj: DecreasePositionInfoJSON) -> "DecreasePositionInfo":
        return cls(
            price=obj["price"],
            liquidation_price=obj["liquidation_price"],
            fee_usd=obj["fee_usd"],
            collateral_usd=obj["collateral_usd"],
            has_profit=obj["has_profit"],
            pnl_delta=obj["pnl_delta"],
            transfer_amount_usd=obj["transfer_amount_usd"],
            transfer_token=obj["transfer_token"],
        )
