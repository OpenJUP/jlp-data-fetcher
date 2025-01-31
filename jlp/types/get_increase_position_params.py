from __future__ import annotations
from . import (
    side,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class GetIncreasePositionParamsJSON(typing.TypedDict):
    collateral_token_delta: int
    size_usd_delta: int
    side: side.SideJSON


@dataclass
class GetIncreasePositionParams:
    layout: typing.ClassVar = borsh.CStruct(
        "collateral_token_delta" / borsh.U64,
        "size_usd_delta" / borsh.U64,
        "side" / side.layout,
    )
    collateral_token_delta: int
    size_usd_delta: int
    side: side.SideKind

    @classmethod
    def from_decoded(cls, obj: Container) -> "GetIncreasePositionParams":
        return cls(
            collateral_token_delta=obj.collateral_token_delta,
            size_usd_delta=obj.size_usd_delta,
            side=side.from_decoded(obj.side),
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "collateral_token_delta": self.collateral_token_delta,
            "size_usd_delta": self.size_usd_delta,
            "side": self.side.to_encodable(),
        }

    def to_json(self) -> GetIncreasePositionParamsJSON:
        return {
            "collateral_token_delta": self.collateral_token_delta,
            "size_usd_delta": self.size_usd_delta,
            "side": self.side.to_json(),
        }

    @classmethod
    def from_json(
        cls, obj: GetIncreasePositionParamsJSON
    ) -> "GetIncreasePositionParams":
        return cls(
            collateral_token_delta=obj["collateral_token_delta"],
            size_usd_delta=obj["size_usd_delta"],
            side=side.from_json(obj["side"]),
        )
