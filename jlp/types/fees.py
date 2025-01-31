from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class FeesJSON(typing.TypedDict):
    increase_position_bps: int
    decrease_position_bps: int
    add_remove_liquidity_bps: int
    swap_bps: int
    tax_bps: int
    stable_swap_bps: int
    stable_swap_tax_bps: int
    liquidation_reward_bps: int
    protocol_share_bps: int


@dataclass
class Fees:
    layout: typing.ClassVar = borsh.CStruct(
        "increase_position_bps" / borsh.U64,
        "decrease_position_bps" / borsh.U64,
        "add_remove_liquidity_bps" / borsh.U64,
        "swap_bps" / borsh.U64,
        "tax_bps" / borsh.U64,
        "stable_swap_bps" / borsh.U64,
        "stable_swap_tax_bps" / borsh.U64,
        "liquidation_reward_bps" / borsh.U64,
        "protocol_share_bps" / borsh.U64,
    )
    increase_position_bps: int
    decrease_position_bps: int
    add_remove_liquidity_bps: int
    swap_bps: int
    tax_bps: int
    stable_swap_bps: int
    stable_swap_tax_bps: int
    liquidation_reward_bps: int
    protocol_share_bps: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "Fees":
        return cls(
            increase_position_bps=obj.increase_position_bps,
            decrease_position_bps=obj.decrease_position_bps,
            add_remove_liquidity_bps=obj.add_remove_liquidity_bps,
            swap_bps=obj.swap_bps,
            tax_bps=obj.tax_bps,
            stable_swap_bps=obj.stable_swap_bps,
            stable_swap_tax_bps=obj.stable_swap_tax_bps,
            liquidation_reward_bps=obj.liquidation_reward_bps,
            protocol_share_bps=obj.protocol_share_bps,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "increase_position_bps": self.increase_position_bps,
            "decrease_position_bps": self.decrease_position_bps,
            "add_remove_liquidity_bps": self.add_remove_liquidity_bps,
            "swap_bps": self.swap_bps,
            "tax_bps": self.tax_bps,
            "stable_swap_bps": self.stable_swap_bps,
            "stable_swap_tax_bps": self.stable_swap_tax_bps,
            "liquidation_reward_bps": self.liquidation_reward_bps,
            "protocol_share_bps": self.protocol_share_bps,
        }

    def to_json(self) -> FeesJSON:
        return {
            "increase_position_bps": self.increase_position_bps,
            "decrease_position_bps": self.decrease_position_bps,
            "add_remove_liquidity_bps": self.add_remove_liquidity_bps,
            "swap_bps": self.swap_bps,
            "tax_bps": self.tax_bps,
            "stable_swap_bps": self.stable_swap_bps,
            "stable_swap_tax_bps": self.stable_swap_tax_bps,
            "liquidation_reward_bps": self.liquidation_reward_bps,
            "protocol_share_bps": self.protocol_share_bps,
        }

    @classmethod
    def from_json(cls, obj: FeesJSON) -> "Fees":
        return cls(
            increase_position_bps=obj["increase_position_bps"],
            decrease_position_bps=obj["decrease_position_bps"],
            add_remove_liquidity_bps=obj["add_remove_liquidity_bps"],
            swap_bps=obj["swap_bps"],
            tax_bps=obj["tax_bps"],
            stable_swap_bps=obj["stable_swap_bps"],
            stable_swap_tax_bps=obj["stable_swap_tax_bps"],
            liquidation_reward_bps=obj["liquidation_reward_bps"],
            protocol_share_bps=obj["protocol_share_bps"],
        )
