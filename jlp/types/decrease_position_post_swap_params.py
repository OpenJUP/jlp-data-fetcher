from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class DecreasePositionPostSwapParamsJSON(typing.TypedDict):
    pass


@dataclass
class DecreasePositionPostSwapParams:
    layout: typing.ClassVar = borsh.CStruct()

    @classmethod
    def from_decoded(cls, obj: Container) -> "DecreasePositionPostSwapParams":
        return cls()

    def to_encodable(self) -> dict[str, typing.Any]:
        return {}

    def to_json(self) -> DecreasePositionPostSwapParamsJSON:
        return {}

    @classmethod
    def from_json(
        cls, obj: DecreasePositionPostSwapParamsJSON
    ) -> "DecreasePositionPostSwapParams":
        return cls()
