from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HostSecurityState(BaseModel):
	fqdn: Optional[str] = Field(default=None,alias="fqdn",)
	isAzureAdJoined: Optional[bool] = Field(default=None,alias="isAzureAdJoined",)
	isAzureAdRegistered: Optional[bool] = Field(default=None,alias="isAzureAdRegistered",)
	isHybridAzureDomainJoined: Optional[bool] = Field(default=None,alias="isHybridAzureDomainJoined",)
	netBiosName: Optional[str] = Field(default=None,alias="netBiosName",)
	os: Optional[str] = Field(default=None,alias="os",)
	privateIpAddress: Optional[str] = Field(default=None,alias="privateIpAddress",)
	publicIpAddress: Optional[str] = Field(default=None,alias="publicIpAddress",)
	riskScore: Optional[str] = Field(default=None,alias="riskScore",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


