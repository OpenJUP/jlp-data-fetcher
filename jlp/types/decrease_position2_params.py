from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class DecreasePosition2ParamsJSON(typing.TypedDict):
    use_price_update: bool


@dataclass
class DecreasePosition2Params:
    layout: typing.ClassVar = borsh.CStruct("use_price_update" / borsh.Bool)
    use_price_update: bool

    @classmethod
    def from_decoded(cls, obj: Container) -> "DecreasePosition2Params":
        return cls(use_price_update=obj.use_price_update)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"use_price_update": self.use_price_update}

    def to_json(self) -> DecreasePosition2ParamsJSON:
        return {"use_price_update": self.use_price_update}

    @classmethod
    def from_json(cls, obj: DecreasePosition2ParamsJSON) -> "DecreasePosition2Params":
        return cls(use_price_update=obj["use_price_update"])
