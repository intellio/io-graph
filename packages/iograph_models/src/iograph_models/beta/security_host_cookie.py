from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostCookie(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	domain: Optional[str] = Field(alias="domain",default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime",default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	host: SerializeAsAny[Optional[SecurityHost]] = Field(alias="host",default=None,)

from .security_host import SecurityHost

