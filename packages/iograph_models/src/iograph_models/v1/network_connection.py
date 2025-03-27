from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkConnection(BaseModel):
	applicationName: Optional[str] = Field(alias="applicationName", default=None,)
	destinationAddress: Optional[str] = Field(alias="destinationAddress", default=None,)
	destinationDomain: Optional[str] = Field(alias="destinationDomain", default=None,)
	destinationLocation: Optional[str] = Field(alias="destinationLocation", default=None,)
	destinationPort: Optional[str] = Field(alias="destinationPort", default=None,)
	destinationUrl: Optional[str] = Field(alias="destinationUrl", default=None,)
	direction: Optional[ConnectionDirection | str] = Field(alias="direction", default=None,)
	domainRegisteredDateTime: Optional[datetime] = Field(alias="domainRegisteredDateTime", default=None,)
	localDnsName: Optional[str] = Field(alias="localDnsName", default=None,)
	natDestinationAddress: Optional[str] = Field(alias="natDestinationAddress", default=None,)
	natDestinationPort: Optional[str] = Field(alias="natDestinationPort", default=None,)
	natSourceAddress: Optional[str] = Field(alias="natSourceAddress", default=None,)
	natSourcePort: Optional[str] = Field(alias="natSourcePort", default=None,)
	protocol: Optional[SecurityNetworkProtocol | str] = Field(alias="protocol", default=None,)
	riskScore: Optional[str] = Field(alias="riskScore", default=None,)
	sourceAddress: Optional[str] = Field(alias="sourceAddress", default=None,)
	sourceLocation: Optional[str] = Field(alias="sourceLocation", default=None,)
	sourcePort: Optional[str] = Field(alias="sourcePort", default=None,)
	status: Optional[ConnectionStatus | str] = Field(alias="status", default=None,)
	urlParameters: Optional[str] = Field(alias="urlParameters", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .connection_direction import ConnectionDirection
from .security_network_protocol import SecurityNetworkProtocol
from .connection_status import ConnectionStatus

