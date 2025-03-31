from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostCookie(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.hostCookie"] = Field(alias="@odata.type", default="#microsoft.graph.security.hostCookie")
	domain: Optional[str] = Field(alias="domain", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	host: Optional[Union[SecurityHostname, SecurityIpAddress]] = Field(alias="host", default=None,discriminator="odata_type", )

from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress
