from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IpApplicationSegment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.ipApplicationSegment"] = Field(alias="@odata.type", default="#microsoft.graph.ipApplicationSegment")
	destinationHost: Optional[str] = Field(alias="destinationHost", default=None,)
	destinationType: Optional[PrivateNetworkDestinationType | str] = Field(alias="destinationType", default=None,)
	port: Optional[int] = Field(alias="port", default=None,)
	ports: Optional[list[str]] = Field(alias="ports", default=None,)
	protocol: Optional[PrivateNetworkProtocol | str] = Field(alias="protocol", default=None,)
	application: Optional[Application] = Field(alias="application", default=None,)

from .private_network_destination_type import PrivateNetworkDestinationType
from .private_network_protocol import PrivateNetworkProtocol
from .application import Application

