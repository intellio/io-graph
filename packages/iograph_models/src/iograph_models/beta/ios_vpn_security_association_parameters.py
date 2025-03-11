from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosVpnSecurityAssociationParameters(BaseModel):
	lifetimeInMinutes: Optional[int] = Field(alias="lifetimeInMinutes",default=None,)
	securityDiffieHellmanGroup: Optional[int] = Field(alias="securityDiffieHellmanGroup",default=None,)
	securityEncryptionAlgorithm: Optional[VpnEncryptionAlgorithmType | str] = Field(alias="securityEncryptionAlgorithm",default=None,)
	securityIntegrityAlgorithm: Optional[VpnIntegrityAlgorithmType | str] = Field(alias="securityIntegrityAlgorithm",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .vpn_encryption_algorithm_type import VpnEncryptionAlgorithmType
from .vpn_integrity_algorithm_type import VpnIntegrityAlgorithmType

