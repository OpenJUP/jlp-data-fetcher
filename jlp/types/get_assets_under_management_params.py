from __future__ import annotations
from . import (
    price_calc_mode,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class GetAssetsUnderManagementParamsJSON(typing.TypedDict):
    mode: typing.Optional[price_calc_mode.PriceCalcModeJSON]


@dataclass
class GetAssetsUnderManagementParams:
    layout: typing.ClassVar = borsh.CStruct(
        "mode" / borsh.Option(price_calc_mode.layout)
    )
    mode: typing.Optional[price_calc_mode.PriceCalcModeKind]

    @classmethod
    def from_decoded(cls, obj: Container) -> "GetAssetsUnderManagementParams":
        return cls(
            mode=(None if obj.mode is None else price_calc_mode.from_decoded(obj.mode))
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"mode": (None if self.mode is None else self.mode.to_encodable())}

    def to_json(self) -> GetAssetsUnderManagementParamsJSON:
        return {"mode": (None if self.mode is None else self.mode.to_json())}

    @classmethod
    def from_json(
        cls, obj: GetAssetsUnderManagementParamsJSON
    ) -> "GetAssetsUnderManagementParams":
        return cls(
            mode=(
                None if obj["mode"] is None else price_calc_mode.from_json(obj["mode"])
            )
        )
