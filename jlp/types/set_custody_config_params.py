from __future__ import annotations
from . import (
    pricing_params,
    oracle_params,
    permissions,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class SetCustodyConfigParamsJSON(typing.TypedDict):
    oracle: oracle_params.OracleParamsJSON
    pricing: pricing_params.PricingParamsJSON
    permissions: permissions.PermissionsJSON
    hourly_funding_bps: int
    target_ratio_bps: int


@dataclass
class SetCustodyConfigParams:
    layout: typing.ClassVar = borsh.CStruct(
        "oracle" / oracle_params.OracleParams.layout,
        "pricing" / pricing_params.PricingParams.layout,
        "permissions" / permissions.Permissions.layout,
        "hourly_funding_bps" / borsh.U64,
        "target_ratio_bps" / borsh.U64,
    )
    oracle: oracle_params.OracleParams
    pricing: pricing_params.PricingParams
    permissions: permissions.Permissions
    hourly_funding_bps: int
    target_ratio_bps: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "SetCustodyConfigParams":
        return cls(
            oracle=oracle_params.OracleParams.from_decoded(obj.oracle),
            pricing=pricing_params.PricingParams.from_decoded(obj.pricing),
            permissions=permissions.Permissions.from_decoded(obj.permissions),
            hourly_funding_bps=obj.hourly_funding_bps,
            target_ratio_bps=obj.target_ratio_bps,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "oracle": self.oracle.to_encodable(),
            "pricing": self.pricing.to_encodable(),
            "permissions": self.permissions.to_encodable(),
            "hourly_funding_bps": self.hourly_funding_bps,
            "target_ratio_bps": self.target_ratio_bps,
        }

    def to_json(self) -> SetCustodyConfigParamsJSON:
        return {
            "oracle": self.oracle.to_json(),
            "pricing": self.pricing.to_json(),
            "permissions": self.permissions.to_json(),
            "hourly_funding_bps": self.hourly_funding_bps,
            "target_ratio_bps": self.target_ratio_bps,
        }

    @classmethod
    def from_json(cls, obj: SetCustodyConfigParamsJSON) -> "SetCustodyConfigParams":
        return cls(
            oracle=oracle_params.OracleParams.from_json(obj["oracle"]),
            pricing=pricing_params.PricingParams.from_json(obj["pricing"]),
            permissions=permissions.Permissions.from_json(obj["permissions"]),
            hourly_funding_bps=obj["hourly_funding_bps"],
            target_ratio_bps=obj["target_ratio_bps"],
        )
