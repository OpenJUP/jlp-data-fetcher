from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class UpdateIncreasePositionRequestParamsJSON(typing.TypedDict):
    size_usd_delta: int
    trigger_price: int


@dataclass
class UpdateIncreasePositionRequestParams:
    layout: typing.ClassVar = borsh.CStruct(
        "size_usd_delta" / borsh.U64, "trigger_price" / borsh.U64
    )
    size_usd_delta: int
    trigger_price: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "UpdateIncreasePositionRequestParams":
        return cls(size_usd_delta=obj.size_usd_delta, trigger_price=obj.trigger_price)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "size_usd_delta": self.size_usd_delta,
            "trigger_price": self.trigger_price,
        }

    def to_json(self) -> UpdateIncreasePositionRequestParamsJSON:
        return {
            "size_usd_delta": self.size_usd_delta,
            "trigger_price": self.trigger_price,
        }

    @classmethod
    def from_json(
        cls, obj: UpdateIncreasePositionRequestParamsJSON
    ) -> "UpdateIncreasePositionRequestParams":
        return cls(
            size_usd_delta=obj["size_usd_delta"], trigger_price=obj["trigger_price"]
        )
