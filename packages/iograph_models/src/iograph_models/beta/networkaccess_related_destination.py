from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedDestination(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedDestination"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedDestination")
	fqdn: Optional[str] = Field(alias="fqdn", default=None,)
	ip: Optional[str] = Field(alias="ip", default=None,)
	networkingProtocol: Optional[NetworkaccessNetworkingProtocol | str] = Field(alias="networkingProtocol", default=None,)
	port: Optional[int] = Field(alias="port", default=None,)

from .networkaccess_networking_protocol import NetworkaccessNetworkingProtocol

