from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class SetTestOraclePriceParamsJSON(typing.TypedDict):
    price: int
    expo: int
    conf: int
    publish_time: int


@dataclass
class SetTestOraclePriceParams:
    layout: typing.ClassVar = borsh.CStruct(
        "price" / borsh.U64,
        "expo" / borsh.I32,
        "conf" / borsh.U64,
        "publish_time" / borsh.I64,
    )
    price: int
    expo: int
    conf: int
    publish_time: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "SetTestOraclePriceParams":
        return cls(
            price=obj.price, expo=obj.expo, conf=obj.conf, publish_time=obj.publish_time
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "price": self.price,
            "expo": self.expo,
            "conf": self.conf,
            "publish_time": self.publish_time,
        }

    def to_json(self) -> SetTestOraclePriceParamsJSON:
        return {
            "price": self.price,
            "expo": self.expo,
            "conf": self.conf,
            "publish_time": self.publish_time,
        }

    @classmethod
    def from_json(cls, obj: SetTestOraclePriceParamsJSON) -> "SetTestOraclePriceParams":
        return cls(
            price=obj["price"],
            expo=obj["expo"],
            conf=obj["conf"],
            publish_time=obj["publish_time"],
        )
