from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityWhoisNameserver(BaseModel):
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime",default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime",default=None,)
	host: SerializeAsAny[Optional[SecurityHost]] = Field(alias="host",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_host import SecurityHost

