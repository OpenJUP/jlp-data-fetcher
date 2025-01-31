from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class GetPnlAndFeeParamsJSON(typing.TypedDict):
    pass


@dataclass
class GetPnlAndFeeParams:
    layout: typing.ClassVar = borsh.CStruct()

    @classmethod
    def from_decoded(cls, obj: Container) -> "GetPnlAndFeeParams":
        return cls()

    def to_encodable(self) -> dict[str, typing.Any]:
        return {}

    def to_json(self) -> GetPnlAndFeeParamsJSON:
        return {}

    @classmethod
    def from_json(cls, obj: GetPnlAndFeeParamsJSON) -> "GetPnlAndFeeParams":
        return cls()
