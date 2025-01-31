import typing
from dataclasses import dataclass
from solders.pubkey import Pubkey
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
import borsh_construct as borsh
from anchorpy.coder.accounts import ACCOUNT_DISCRIMINATOR_SIZE
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from anchorpy.borsh_extension import BorshPubkey
from ..program_id import PROGRAM_ID
from .. import types


class CustodyJSON(typing.TypedDict):
    pool: str
    mint: str
    token_account: str
    decimals: int
    is_stable: bool
    oracle: types.oracle_params.OracleParamsJSON
    pricing: types.pricing_params.PricingParamsJSON
    permissions: types.permissions.PermissionsJSON
    target_ratio_bps: int
    assets: types.assets.AssetsJSON
    funding_rate_state: types.funding_rate_state.FundingRateStateJSON
    bump: int
    token_account_bump: int


@dataclass
class Custody:
    discriminator: typing.ClassVar = b"\x01\xb80Q]\x83?\x91"
    layout: typing.ClassVar = borsh.CStruct(
        "pool" / BorshPubkey,
        "mint" / BorshPubkey,
        "token_account" / BorshPubkey,
        "decimals" / borsh.U8,
        "is_stable" / borsh.Bool,
        "oracle" / types.oracle_params.OracleParams.layout,
        "pricing" / types.pricing_params.PricingParams.layout,
        "permissions" / types.permissions.Permissions.layout,
        "target_ratio_bps" / borsh.U64,
        "assets" / types.assets.Assets.layout,
        "funding_rate_state" / types.funding_rate_state.FundingRateState.layout,
        "bump" / borsh.U8,
        "token_account_bump" / borsh.U8,
    )
    pool: Pubkey
    mint: Pubkey
    token_account: Pubkey
    decimals: int
    is_stable: bool
    oracle: types.oracle_params.OracleParams
    pricing: types.pricing_params.PricingParams
    permissions: types.permissions.Permissions
    target_ratio_bps: int
    assets: types.assets.Assets
    funding_rate_state: types.funding_rate_state.FundingRateState
    bump: int
    token_account_bump: int

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: Pubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: Pubkey = PROGRAM_ID,
    ) -> typing.Optional["Custody"]:
        resp = await conn.get_account_info(address, commitment=commitment)
        info = resp.value
        if info is None:
            return None
        if info.owner != program_id:
            raise ValueError("Account does not belong to this program")
        bytes_data = info.data
        return cls.decode(bytes_data)

    @classmethod
    async def fetch_multiple(
        cls,
        conn: AsyncClient,
        addresses: list[Pubkey],
        commitment: typing.Optional[Commitment] = None,
        program_id: Pubkey = PROGRAM_ID,
    ) -> typing.List[typing.Optional["Custody"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["Custody"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "Custody":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = Custody.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            pool=dec.pool,
            mint=dec.mint,
            token_account=dec.token_account,
            decimals=dec.decimals,
            is_stable=dec.is_stable,
            oracle=types.oracle_params.OracleParams.from_decoded(dec.oracle),
            pricing=types.pricing_params.PricingParams.from_decoded(dec.pricing),
            permissions=types.permissions.Permissions.from_decoded(dec.permissions),
            target_ratio_bps=dec.target_ratio_bps,
            assets=types.assets.Assets.from_decoded(dec.assets),
            funding_rate_state=types.funding_rate_state.FundingRateState.from_decoded(
                dec.funding_rate_state
            ),
            bump=dec.bump,
            token_account_bump=dec.token_account_bump,
        )

    def to_json(self) -> CustodyJSON:
        return {
            "pool": str(self.pool),
            "mint": str(self.mint),
            "token_account": str(self.token_account),
            "decimals": self.decimals,
            "is_stable": self.is_stable,
            "oracle": self.oracle.to_json(),
            "pricing": self.pricing.to_json(),
            "permissions": self.permissions.to_json(),
            "target_ratio_bps": self.target_ratio_bps,
            "assets": self.assets.to_json(),
            "funding_rate_state": self.funding_rate_state.to_json(),
            "bump": self.bump,
            "token_account_bump": self.token_account_bump,
        }

    @classmethod
    def from_json(cls, obj: CustodyJSON) -> "Custody":
        return cls(
            pool=Pubkey.from_string(obj["pool"]),
            mint=Pubkey.from_string(obj["mint"]),
            token_account=Pubkey.from_string(obj["token_account"]),
            decimals=obj["decimals"],
            is_stable=obj["is_stable"],
            oracle=types.oracle_params.OracleParams.from_json(obj["oracle"]),
            pricing=types.pricing_params.PricingParams.from_json(obj["pricing"]),
            permissions=types.permissions.Permissions.from_json(obj["permissions"]),
            target_ratio_bps=obj["target_ratio_bps"],
            assets=types.assets.Assets.from_json(obj["assets"]),
            funding_rate_state=types.funding_rate_state.FundingRateState.from_json(
                obj["funding_rate_state"]
            ),
            bump=obj["bump"],
            token_account_bump=obj["token_account_bump"],
        )
