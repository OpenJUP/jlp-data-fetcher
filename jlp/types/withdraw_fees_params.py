from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class WithdrawFeesParamsJSON(typing.TypedDict):
    pass


@dataclass
class WithdrawFeesParams:
    layout: typing.ClassVar = borsh.CStruct()

    @classmethod
    def from_decoded(cls, obj: Container) -> "WithdrawFeesParams":
        return cls()

    def to_encodable(self) -> dict[str, typing.Any]:
        return {}

    def to_json(self) -> WithdrawFeesParamsJSON:
        return {}

    @classmethod
    def from_json(cls, obj: WithdrawFeesParamsJSON) -> "WithdrawFeesParams":
        return cls()
