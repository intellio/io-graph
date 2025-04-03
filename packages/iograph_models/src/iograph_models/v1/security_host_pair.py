from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostPair(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.hostPair"] = Field(alias="@odata.type", default="#microsoft.graph.security.hostPair")
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	linkKind: Optional[str] = Field(alias="linkKind", default=None,)
	childHost: Optional[Union[SecurityHostname, SecurityIpAddress]] = Field(alias="childHost", default=None,discriminator="odata_type", )
	parentHost: Optional[Union[SecurityHostname, SecurityIpAddress]] = Field(alias="parentHost", default=None,discriminator="odata_type", )

from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress
