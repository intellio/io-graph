from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class HostSecurityState(BaseModel):
	fqdn: Optional[str] = Field(alias="fqdn", default=None,)
	isAzureAdJoined: Optional[bool] = Field(alias="isAzureAdJoined", default=None,)
	isAzureAdRegistered: Optional[bool] = Field(alias="isAzureAdRegistered", default=None,)
	isHybridAzureDomainJoined: Optional[bool] = Field(alias="isHybridAzureDomainJoined", default=None,)
	netBiosName: Optional[str] = Field(alias="netBiosName", default=None,)
	os: Optional[str] = Field(alias="os", default=None,)
	privateIpAddress: Optional[str] = Field(alias="privateIpAddress", default=None,)
	publicIpAddress: Optional[str] = Field(alias="publicIpAddress", default=None,)
	riskScore: Optional[str] = Field(alias="riskScore", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

