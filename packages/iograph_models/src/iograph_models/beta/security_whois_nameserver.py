from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityWhoisNameserver(BaseModel):
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	host: Optional[Union[SecurityHostname, SecurityIpAddress]] = Field(alias="host", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_hostname import SecurityHostname
from .security_ip_address import SecurityIpAddress
