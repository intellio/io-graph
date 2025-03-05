from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityWhoisNameserver(BaseModel):
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	host: SerializeAsAny[Optional[SecurityHost]] = Field(default=None,alias="host",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_host import SecurityHost

