from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class LimitJSON(typing.TypedDict):
    max_aum_usd: int
    token_weightage_buffer_bps: int
    max_position_usd: int


@dataclass
class Limit:
    layout: typing.ClassVar = borsh.CStruct(
        "max_aum_usd" / borsh.U128,
        "token_weightage_buffer_bps" / borsh.U128,
        "max_position_usd" / borsh.U64,
    )
    max_aum_usd: int
    token_weightage_buffer_bps: int
    max_position_usd: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "Limit":
        return cls(
            max_aum_usd=obj.max_aum_usd,
            token_weightage_buffer_bps=obj.token_weightage_buffer_bps,
            max_position_usd=obj.max_position_usd,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "max_aum_usd": self.max_aum_usd,
            "token_weightage_buffer_bps": self.token_weightage_buffer_bps,
            "max_position_usd": self.max_position_usd,
        }

    def to_json(self) -> LimitJSON:
        return {
            "max_aum_usd": self.max_aum_usd,
            "token_weightage_buffer_bps": self.token_weightage_buffer_bps,
            "max_position_usd": self.max_position_usd,
        }

    @classmethod
    def from_json(cls, obj: LimitJSON) -> "Limit":
        return cls(
            max_aum_usd=obj["max_aum_usd"],
            token_weightage_buffer_bps=obj["token_weightage_buffer_bps"],
            max_position_usd=obj["max_position_usd"],
        )
