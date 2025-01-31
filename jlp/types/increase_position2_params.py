from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class IncreasePosition2ParamsJSON(typing.TypedDict):
    use_price_update: bool


@dataclass
class IncreasePosition2Params:
    layout: typing.ClassVar = borsh.CStruct("use_price_update" / borsh.Bool)
    use_price_update: bool

    @classmethod
    def from_decoded(cls, obj: Container) -> "IncreasePosition2Params":
        return cls(use_price_update=obj.use_price_update)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"use_price_update": self.use_price_update}

    def to_json(self) -> IncreasePosition2ParamsJSON:
        return {"use_price_update": self.use_price_update}

    @classmethod
    def from_json(cls, obj: IncreasePosition2ParamsJSON) -> "IncreasePosition2Params":
        return cls(use_price_update=obj["use_price_update"])
