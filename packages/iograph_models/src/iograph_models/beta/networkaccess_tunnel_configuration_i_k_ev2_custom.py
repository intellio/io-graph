from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessTunnelConfigurationIKEv2Custom(BaseModel):
	preSharedKey: Optional[str] = Field(alias="preSharedKey", default=None,)
	zoneRedundancyPreSharedKey: Optional[str] = Field(alias="zoneRedundancyPreSharedKey", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Custom"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.tunnelConfigurationIKEv2Custom")
	dhGroup: Optional[NetworkaccessDhGroup | str] = Field(alias="dhGroup", default=None,)
	ikeEncryption: Optional[NetworkaccessIkeEncryption | str] = Field(alias="ikeEncryption", default=None,)
	ikeIntegrity: Optional[NetworkaccessIkeIntegrity | str] = Field(alias="ikeIntegrity", default=None,)
	ipSecEncryption: Optional[NetworkaccessIpSecEncryption | str] = Field(alias="ipSecEncryption", default=None,)
	ipSecIntegrity: Optional[NetworkaccessIpSecIntegrity | str] = Field(alias="ipSecIntegrity", default=None,)
	pfsGroup: Optional[NetworkaccessPfsGroup | str] = Field(alias="pfsGroup", default=None,)
	saLifeTimeSeconds: Optional[int] = Field(alias="saLifeTimeSeconds", default=None,)

from .networkaccess_dh_group import NetworkaccessDhGroup
from .networkaccess_ike_encryption import NetworkaccessIkeEncryption
from .networkaccess_ike_integrity import NetworkaccessIkeIntegrity
from .networkaccess_ip_sec_encryption import NetworkaccessIpSecEncryption
from .networkaccess_ip_sec_integrity import NetworkaccessIpSecIntegrity
from .networkaccess_pfs_group import NetworkaccessPfsGroup
