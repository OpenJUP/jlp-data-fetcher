from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class GetDecreasePositionParamsJSON(typing.TypedDict):
    collateral_usd_delta: int
    size_usd_delta: int


@dataclass
class GetDecreasePositionParams:
    layout: typing.ClassVar = borsh.CStruct(
        "collateral_usd_delta" / borsh.U64, "size_usd_delta" / borsh.U64
    )
    collateral_usd_delta: int
    size_usd_delta: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "GetDecreasePositionParams":
        return cls(
            collateral_usd_delta=obj.collateral_usd_delta,
            size_usd_delta=obj.size_usd_delta,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "collateral_usd_delta": self.collateral_usd_delta,
            "size_usd_delta": self.size_usd_delta,
        }

    def to_json(self) -> GetDecreasePositionParamsJSON:
        return {
            "collateral_usd_delta": self.collateral_usd_delta,
            "size_usd_delta": self.size_usd_delta,
        }

    @classmethod
    def from_json(
        cls, obj: GetDecreasePositionParamsJSON
    ) -> "GetDecreasePositionParams":
        return cls(
            collateral_usd_delta=obj["collateral_usd_delta"],
            size_usd_delta=obj["size_usd_delta"],
        )
