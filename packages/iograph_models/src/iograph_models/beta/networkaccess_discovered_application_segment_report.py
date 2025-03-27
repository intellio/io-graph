from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessDiscoveredApplicationSegmentReport(BaseModel):
	accessType: Optional[NetworkaccessAccessType | str] = Field(alias="accessType", default=None,)
	deviceCount: Optional[int] = Field(alias="deviceCount", default=None,)
	discoveredApplicationSegmentId: Optional[str] = Field(alias="discoveredApplicationSegmentId", default=None,)
	firstAccessDateTime: Optional[datetime] = Field(alias="firstAccessDateTime", default=None,)
	fqdn: Optional[str] = Field(alias="fqdn", default=None,)
	ip: Optional[str] = Field(alias="ip", default=None,)
	lastAccessDateTime: Optional[datetime] = Field(alias="lastAccessDateTime", default=None,)
	port: Optional[int] = Field(alias="port", default=None,)
	totalBytesReceived: Optional[int] = Field(alias="totalBytesReceived", default=None,)
	totalBytesSent: Optional[int] = Field(alias="totalBytesSent", default=None,)
	transactionCount: Optional[int] = Field(alias="transactionCount", default=None,)
	transportProtocol: Optional[NetworkaccessNetworkingProtocol | str] = Field(alias="transportProtocol", default=None,)
	userCount: Optional[int] = Field(alias="userCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .networkaccess_access_type import NetworkaccessAccessType
from .networkaccess_networking_protocol import NetworkaccessNetworkingProtocol

