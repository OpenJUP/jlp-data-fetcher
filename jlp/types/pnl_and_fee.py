from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class PnlAndFeeJSON(typing.TypedDict):
    has_profit: bool
    pnl_delta: int
    open_position_fee_usd: int
    close_position_fee_usd: int
    funding_fee_usd: int
    liquidation_price: int


@dataclass
class PnlAndFee:
    layout: typing.ClassVar = borsh.CStruct(
        "has_profit" / borsh.Bool,
        "pnl_delta" / borsh.U64,
        "open_position_fee_usd" / borsh.U64,
        "close_position_fee_usd" / borsh.U64,
        "funding_fee_usd" / borsh.U64,
        "liquidation_price" / borsh.U64,
    )
    has_profit: bool
    pnl_delta: int
    open_position_fee_usd: int
    close_position_fee_usd: int
    funding_fee_usd: int
    liquidation_price: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "PnlAndFee":
        return cls(
            has_profit=obj.has_profit,
            pnl_delta=obj.pnl_delta,
            open_position_fee_usd=obj.open_position_fee_usd,
            close_position_fee_usd=obj.close_position_fee_usd,
            funding_fee_usd=obj.funding_fee_usd,
            liquidation_price=obj.liquidation_price,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "has_profit": self.has_profit,
            "pnl_delta": self.pnl_delta,
            "open_position_fee_usd": self.open_position_fee_usd,
            "close_position_fee_usd": self.close_position_fee_usd,
            "funding_fee_usd": self.funding_fee_usd,
            "liquidation_price": self.liquidation_price,
        }

    def to_json(self) -> PnlAndFeeJSON:
        return {
            "has_profit": self.has_profit,
            "pnl_delta": self.pnl_delta,
            "open_position_fee_usd": self.open_position_fee_usd,
            "close_position_fee_usd": self.close_position_fee_usd,
            "funding_fee_usd": self.funding_fee_usd,
            "liquidation_price": self.liquidation_price,
        }

    @classmethod
    def from_json(cls, obj: PnlAndFeeJSON) -> "PnlAndFee":
        return cls(
            has_profit=obj["has_profit"],
            pnl_delta=obj["pnl_delta"],
            open_position_fee_usd=obj["open_position_fee_usd"],
            close_position_fee_usd=obj["close_position_fee_usd"],
            funding_fee_usd=obj["funding_fee_usd"],
            liquidation_price=obj["liquidation_price"],
        )
