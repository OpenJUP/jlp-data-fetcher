from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class LiquidateFullPosition2ParamsJSON(typing.TypedDict):
    use_price_update: bool


@dataclass
class LiquidateFullPosition2Params:
    layout: typing.ClassVar = borsh.CStruct("use_price_update" / borsh.Bool)
    use_price_update: bool

    @classmethod
    def from_decoded(cls, obj: Container) -> "LiquidateFullPosition2Params":
        return cls(use_price_update=obj.use_price_update)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"use_price_update": self.use_price_update}

    def to_json(self) -> LiquidateFullPosition2ParamsJSON:
        return {"use_price_update": self.use_price_update}

    @classmethod
    def from_json(
        cls, obj: LiquidateFullPosition2ParamsJSON
    ) -> "LiquidateFullPosition2Params":
        return cls(use_price_update=obj["use_price_update"])
