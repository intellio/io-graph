from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class NetworkConnection(BaseModel):
	applicationName: Optional[str] = Field(default=None,alias="applicationName",)
	destinationAddress: Optional[str] = Field(default=None,alias="destinationAddress",)
	destinationDomain: Optional[str] = Field(default=None,alias="destinationDomain",)
	destinationLocation: Optional[str] = Field(default=None,alias="destinationLocation",)
	destinationPort: Optional[str] = Field(default=None,alias="destinationPort",)
	destinationUrl: Optional[str] = Field(default=None,alias="destinationUrl",)
	direction: Optional[ConnectionDirection] = Field(default=None,alias="direction",)
	domainRegisteredDateTime: Optional[datetime] = Field(default=None,alias="domainRegisteredDateTime",)
	localDnsName: Optional[str] = Field(default=None,alias="localDnsName",)
	natDestinationAddress: Optional[str] = Field(default=None,alias="natDestinationAddress",)
	natDestinationPort: Optional[str] = Field(default=None,alias="natDestinationPort",)
	natSourceAddress: Optional[str] = Field(default=None,alias="natSourceAddress",)
	natSourcePort: Optional[str] = Field(default=None,alias="natSourcePort",)
	protocol: Optional[SecurityNetworkProtocol] = Field(default=None,alias="protocol",)
	riskScore: Optional[str] = Field(default=None,alias="riskScore",)
	sourceAddress: Optional[str] = Field(default=None,alias="sourceAddress",)
	sourceLocation: Optional[str] = Field(default=None,alias="sourceLocation",)
	sourcePort: Optional[str] = Field(default=None,alias="sourcePort",)
	status: Optional[ConnectionStatus] = Field(default=None,alias="status",)
	urlParameters: Optional[str] = Field(default=None,alias="urlParameters",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .connection_direction import ConnectionDirection
from .security_network_protocol import SecurityNetworkProtocol
from .connection_status import ConnectionStatus

