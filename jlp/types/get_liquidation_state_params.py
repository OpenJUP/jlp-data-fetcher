from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class GetLiquidationStateParamsJSON(typing.TypedDict):
    pass


@dataclass
class GetLiquidationStateParams:
    layout: typing.ClassVar = borsh.CStruct()

    @classmethod
    def from_decoded(cls, obj: Container) -> "GetLiquidationStateParams":
        return cls()

    def to_encodable(self) -> dict[str, typing.Any]:
        return {}

    def to_json(self) -> GetLiquidationStateParamsJSON:
        return {}

    @classmethod
    def from_json(
        cls, obj: GetLiquidationStateParamsJSON
    ) -> "GetLiquidationStateParams":
        return cls()
