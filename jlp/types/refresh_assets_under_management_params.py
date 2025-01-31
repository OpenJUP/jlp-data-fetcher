from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class RefreshAssetsUnderManagementParamsJSON(typing.TypedDict):
    pass


@dataclass
class RefreshAssetsUnderManagementParams:
    layout: typing.ClassVar = borsh.CStruct()

    @classmethod
    def from_decoded(cls, obj: Container) -> "RefreshAssetsUnderManagementParams":
        return cls()

    def to_encodable(self) -> dict[str, typing.Any]:
        return {}

    def to_json(self) -> RefreshAssetsUnderManagementParamsJSON:
        return {}

    @classmethod
    def from_json(
        cls, obj: RefreshAssetsUnderManagementParamsJSON
    ) -> "RefreshAssetsUnderManagementParams":
        return cls()
