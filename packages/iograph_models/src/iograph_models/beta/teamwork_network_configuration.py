from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamworkNetworkConfiguration(BaseModel):
	defaultGateway: Optional[str] = Field(alias="defaultGateway", default=None,)
	domainName: Optional[str] = Field(alias="domainName", default=None,)
	hostName: Optional[str] = Field(alias="hostName", default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress", default=None,)
	isDhcpEnabled: Optional[bool] = Field(alias="isDhcpEnabled", default=None,)
	isPCPortEnabled: Optional[bool] = Field(alias="isPCPortEnabled", default=None,)
	primaryDns: Optional[str] = Field(alias="primaryDns", default=None,)
	secondaryDns: Optional[str] = Field(alias="secondaryDns", default=None,)
	subnetMask: Optional[str] = Field(alias="subnetMask", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

