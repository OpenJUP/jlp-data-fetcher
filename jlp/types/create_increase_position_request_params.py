from __future__ import annotations
from . import (
    request_type,
    side,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class CreateIncreasePositionRequestParamsJSON(typing.TypedDict):
    size_usd_delta: int
    collateral_token_delta: int
    side: side.SideJSON
    request_type: request_type.RequestTypeJSON
    price_slippage: typing.Optional[int]
    jupiter_minimum_out: typing.Optional[int]
    trigger_price: typing.Optional[int]
    trigger_above_threshold: typing.Optional[bool]
    counter: int


@dataclass
class CreateIncreasePositionRequestParams:
    layout: typing.ClassVar = borsh.CStruct(
        "size_usd_delta" / borsh.U64,
        "collateral_token_delta" / borsh.U64,
        "side" / side.layout,
        "request_type" / request_type.layout,
        "price_slippage" / borsh.Option(borsh.U64),
        "jupiter_minimum_out" / borsh.Option(borsh.U64),
        "trigger_price" / borsh.Option(borsh.U64),
        "trigger_above_threshold" / borsh.Option(borsh.Bool),
        "counter" / borsh.U64,
    )
    size_usd_delta: int
    collateral_token_delta: int
    side: side.SideKind
    request_type: request_type.RequestTypeKind
    price_slippage: typing.Optional[int]
    jupiter_minimum_out: typing.Optional[int]
    trigger_price: typing.Optional[int]
    trigger_above_threshold: typing.Optional[bool]
    counter: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "CreateIncreasePositionRequestParams":
        return cls(
            size_usd_delta=obj.size_usd_delta,
            collateral_token_delta=obj.collateral_token_delta,
            side=side.from_decoded(obj.side),
            request_type=request_type.from_decoded(obj.request_type),
            price_slippage=obj.price_slippage,
            jupiter_minimum_out=obj.jupiter_minimum_out,
            trigger_price=obj.trigger_price,
            trigger_above_threshold=obj.trigger_above_threshold,
            counter=obj.counter,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "size_usd_delta": self.size_usd_delta,
            "collateral_token_delta": self.collateral_token_delta,
            "side": self.side.to_encodable(),
            "request_type": self.request_type.to_encodable(),
            "price_slippage": self.price_slippage,
            "jupiter_minimum_out": self.jupiter_minimum_out,
            "trigger_price": self.trigger_price,
            "trigger_above_threshold": self.trigger_above_threshold,
            "counter": self.counter,
        }

    def to_json(self) -> CreateIncreasePositionRequestParamsJSON:
        return {
            "size_usd_delta": self.size_usd_delta,
            "collateral_token_delta": self.collateral_token_delta,
            "side": self.side.to_json(),
            "request_type": self.request_type.to_json(),
            "price_slippage": self.price_slippage,
            "jupiter_minimum_out": self.jupiter_minimum_out,
            "trigger_price": self.trigger_price,
            "trigger_above_threshold": self.trigger_above_threshold,
            "counter": self.counter,
        }

    @classmethod
    def from_json(
        cls, obj: CreateIncreasePositionRequestParamsJSON
    ) -> "CreateIncreasePositionRequestParams":
        return cls(
            size_usd_delta=obj["size_usd_delta"],
            collateral_token_delta=obj["collateral_token_delta"],
            side=side.from_json(obj["side"]),
            request_type=request_type.from_json(obj["request_type"]),
            price_slippage=obj["price_slippage"],
            jupiter_minimum_out=obj["jupiter_minimum_out"],
            trigger_price=obj["trigger_price"],
            trigger_above_threshold=obj["trigger_above_threshold"],
            counter=obj["counter"],
        )
