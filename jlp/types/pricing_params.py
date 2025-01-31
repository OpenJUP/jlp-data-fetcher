from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class PricingParamsJSON(typing.TypedDict):
    trade_spread_long: int
    trade_spread_short: int
    swap_spread: int
    max_leverage: int
    max_global_long_sizes: int
    max_global_short_sizes: int


@dataclass
class PricingParams:
    layout: typing.ClassVar = borsh.CStruct(
        "trade_spread_long" / borsh.U64,
        "trade_spread_short" / borsh.U64,
        "swap_spread" / borsh.U64,
        "max_leverage" / borsh.U64,
        "max_global_long_sizes" / borsh.U64,
        "max_global_short_sizes" / borsh.U64,
    )
    trade_spread_long: int
    trade_spread_short: int
    swap_spread: int
    max_leverage: int
    max_global_long_sizes: int
    max_global_short_sizes: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "PricingParams":
        return cls(
            trade_spread_long=obj.trade_spread_long,
            trade_spread_short=obj.trade_spread_short,
            swap_spread=obj.swap_spread,
            max_leverage=obj.max_leverage,
            max_global_long_sizes=obj.max_global_long_sizes,
            max_global_short_sizes=obj.max_global_short_sizes,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "trade_spread_long": self.trade_spread_long,
            "trade_spread_short": self.trade_spread_short,
            "swap_spread": self.swap_spread,
            "max_leverage": self.max_leverage,
            "max_global_long_sizes": self.max_global_long_sizes,
            "max_global_short_sizes": self.max_global_short_sizes,
        }

    def to_json(self) -> PricingParamsJSON:
        return {
            "trade_spread_long": self.trade_spread_long,
            "trade_spread_short": self.trade_spread_short,
            "swap_spread": self.swap_spread,
            "max_leverage": self.max_leverage,
            "max_global_long_sizes": self.max_global_long_sizes,
            "max_global_short_sizes": self.max_global_short_sizes,
        }

    @classmethod
    def from_json(cls, obj: PricingParamsJSON) -> "PricingParams":
        return cls(
            trade_spread_long=obj["trade_spread_long"],
            trade_spread_short=obj["trade_spread_short"],
            swap_spread=obj["swap_spread"],
            max_leverage=obj["max_leverage"],
            max_global_long_sizes=obj["max_global_long_sizes"],
            max_global_short_sizes=obj["max_global_short_sizes"],
        )
