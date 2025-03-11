from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CryptographySuite(BaseModel):
	authenticationTransformConstants: Optional[AuthenticationTransformConstant | str] = Field(alias="authenticationTransformConstants",default=None,)
	cipherTransformConstants: Optional[VpnEncryptionAlgorithmType | str] = Field(alias="cipherTransformConstants",default=None,)
	dhGroup: Optional[DiffieHellmanGroup | str] = Field(alias="dhGroup",default=None,)
	encryptionMethod: Optional[VpnEncryptionAlgorithmType | str] = Field(alias="encryptionMethod",default=None,)
	integrityCheckMethod: Optional[VpnIntegrityAlgorithmType | str] = Field(alias="integrityCheckMethod",default=None,)
	pfsGroup: Optional[PerfectForwardSecrecyGroup | str] = Field(alias="pfsGroup",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authentication_transform_constant import AuthenticationTransformConstant
from .vpn_encryption_algorithm_type import VpnEncryptionAlgorithmType
from .diffie_hellman_group import DiffieHellmanGroup
from .vpn_encryption_algorithm_type import VpnEncryptionAlgorithmType
from .vpn_integrity_algorithm_type import VpnIntegrityAlgorithmType
from .perfect_forward_secrecy_group import PerfectForwardSecrecyGroup

