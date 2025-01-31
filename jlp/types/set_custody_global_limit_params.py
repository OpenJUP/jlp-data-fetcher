from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class SetCustodyGlobalLimitParamsJSON(typing.TypedDict):
    max_global_long_sizes: int
    max_global_short_sizes: int


@dataclass
class SetCustodyGlobalLimitParams:
    layout: typing.ClassVar = borsh.CStruct(
        "max_global_long_sizes" / borsh.U64, "max_global_short_sizes" / borsh.U64
    )
    max_global_long_sizes: int
    max_global_short_sizes: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "SetCustodyGlobalLimitParams":
        return cls(
            max_global_long_sizes=obj.max_global_long_sizes,
            max_global_short_sizes=obj.max_global_short_sizes,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "max_global_long_sizes": self.max_global_long_sizes,
            "max_global_short_sizes": self.max_global_short_sizes,
        }

    def to_json(self) -> SetCustodyGlobalLimitParamsJSON:
        return {
            "max_global_long_sizes": self.max_global_long_sizes,
            "max_global_short_sizes": self.max_global_short_sizes,
        }

    @classmethod
    def from_json(
        cls, obj: SetCustodyGlobalLimitParamsJSON
    ) -> "SetCustodyGlobalLimitParams":
        return cls(
            max_global_long_sizes=obj["max_global_long_sizes"],
            max_global_short_sizes=obj["max_global_short_sizes"],
        )
