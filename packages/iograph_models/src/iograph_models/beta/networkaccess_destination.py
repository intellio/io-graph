from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessDestination(BaseModel):
	deviceCount: Optional[int] = Field(alias="deviceCount",default=None,)
	firstAccessDateTime: Optional[datetime] = Field(alias="firstAccessDateTime",default=None,)
	fqdn: Optional[str] = Field(alias="fqdn",default=None,)
	ip: Optional[str] = Field(alias="ip",default=None,)
	lastAccessDateTime: Optional[datetime] = Field(alias="lastAccessDateTime",default=None,)
	networkingProtocol: Optional[NetworkaccessNetworkingProtocol | str] = Field(alias="networkingProtocol",default=None,)
	port: Optional[int] = Field(alias="port",default=None,)
	threatCount: Optional[int] = Field(alias="threatCount",default=None,)
	totalBytesReceived: Optional[int] = Field(alias="totalBytesReceived",default=None,)
	totalBytesSent: Optional[int] = Field(alias="totalBytesSent",default=None,)
	trafficType: Optional[NetworkaccessTrafficType | str] = Field(alias="trafficType",default=None,)
	transactionCount: Optional[int] = Field(alias="transactionCount",default=None,)
	userCount: Optional[int] = Field(alias="userCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .networkaccess_networking_protocol import NetworkaccessNetworkingProtocol
from .networkaccess_traffic_type import NetworkaccessTrafficType

