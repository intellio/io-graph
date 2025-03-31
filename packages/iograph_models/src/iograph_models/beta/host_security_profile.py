from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class HostSecurityProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.hostSecurityProfile"] = Field(alias="@odata.type",)
	azureSubscriptionId: Optional[str] = Field(alias="azureSubscriptionId", default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	fqdn: Optional[str] = Field(alias="fqdn", default=None,)
	isAzureAdJoined: Optional[bool] = Field(alias="isAzureAdJoined", default=None,)
	isAzureAdRegistered: Optional[bool] = Field(alias="isAzureAdRegistered", default=None,)
	isHybridAzureDomainJoined: Optional[bool] = Field(alias="isHybridAzureDomainJoined", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	logonUsers: Optional[list[LogonUser]] = Field(alias="logonUsers", default=None,)
	netBiosName: Optional[str] = Field(alias="netBiosName", default=None,)
	networkInterfaces: Optional[list[NetworkInterface]] = Field(alias="networkInterfaces", default=None,)
	os: Optional[str] = Field(alias="os", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	parentHost: Optional[str] = Field(alias="parentHost", default=None,)
	relatedHostIds: Optional[list[str]] = Field(alias="relatedHostIds", default=None,)
	riskScore: Optional[str] = Field(alias="riskScore", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	vendorInformation: Optional[SecurityVendorInformation] = Field(alias="vendorInformation", default=None,)

from .logon_user import LogonUser
from .network_interface import NetworkInterface
from .security_vendor_information import SecurityVendorInformation
