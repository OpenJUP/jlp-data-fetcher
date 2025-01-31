from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class OraclePriceInfoJSON(typing.TypedDict):
    increase_long: int
    increase_short: int
    decrease_long: int
    decrease_short: int
    buy_lp: int
    sell_lp: int


@dataclass
class OraclePriceInfo:
    layout: typing.ClassVar = borsh.CStruct(
        "increase_long" / borsh.U64,
        "increase_short" / borsh.U64,
        "decrease_long" / borsh.U64,
        "decrease_short" / borsh.U64,
        "buy_lp" / borsh.U64,
        "sell_lp" / borsh.U64,
    )
    increase_long: int
    increase_short: int
    decrease_long: int
    decrease_short: int
    buy_lp: int
    sell_lp: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "OraclePriceInfo":
        return cls(
            increase_long=obj.increase_long,
            increase_short=obj.increase_short,
            decrease_long=obj.decrease_long,
            decrease_short=obj.decrease_short,
            buy_lp=obj.buy_lp,
            sell_lp=obj.sell_lp,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "increase_long": self.increase_long,
            "increase_short": self.increase_short,
            "decrease_long": self.decrease_long,
            "decrease_short": self.decrease_short,
            "buy_lp": self.buy_lp,
            "sell_lp": self.sell_lp,
        }

    def to_json(self) -> OraclePriceInfoJSON:
        return {
            "increase_long": self.increase_long,
            "increase_short": self.increase_short,
            "decrease_long": self.decrease_long,
            "decrease_short": self.decrease_short,
            "buy_lp": self.buy_lp,
            "sell_lp": self.sell_lp,
        }

    @classmethod
    def from_json(cls, obj: OraclePriceInfoJSON) -> "OraclePriceInfo":
        return cls(
            increase_long=obj["increase_long"],
            increase_short=obj["increase_short"],
            decrease_long=obj["decrease_long"],
            decrease_short=obj["decrease_short"],
            buy_lp=obj["buy_lp"],
            sell_lp=obj["sell_lp"],
        )
