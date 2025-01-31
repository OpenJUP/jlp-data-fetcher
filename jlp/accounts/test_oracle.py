import typing
from dataclasses import dataclass
from solders.pubkey import Pubkey
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
import borsh_construct as borsh
from anchorpy.coder.accounts import ACCOUNT_DISCRIMINATOR_SIZE
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from ..program_id import PROGRAM_ID


class TestOracleJSON(typing.TypedDict):
    price: int
    expo: int
    conf: int
    publish_time: int


@dataclass
class TestOracle:
    discriminator: typing.ClassVar = b"\xc61?\x86\xe8\xfb\xa8\x1c"
    layout: typing.ClassVar = borsh.CStruct(
        "price" / borsh.U64,
        "expo" / borsh.I32,
        "conf" / borsh.U64,
        "publish_time" / borsh.I64,
    )
    price: int
    expo: int
    conf: int
    publish_time: int

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: Pubkey,
        commitment: typing.Optional[Commitment] = None,
        program_id: Pubkey = PROGRAM_ID,
    ) -> typing.Optional["TestOracle"]:
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
    ) -> typing.List[typing.Optional["TestOracle"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["TestOracle"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "TestOracle":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = TestOracle.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            price=dec.price,
            expo=dec.expo,
            conf=dec.conf,
            publish_time=dec.publish_time,
        )

    def to_json(self) -> TestOracleJSON:
        return {
            "price": self.price,
            "expo": self.expo,
            "conf": self.conf,
            "publish_time": self.publish_time,
        }

    @classmethod
    def from_json(cls, obj: TestOracleJSON) -> "TestOracle":
        return cls(
            price=obj["price"],
            expo=obj["expo"],
            conf=obj["conf"],
            publish_time=obj["publish_time"],
        )
