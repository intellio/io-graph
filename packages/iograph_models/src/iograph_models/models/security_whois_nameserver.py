from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityWhoisNameserver(BaseModel):
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	host: Optional[SecurityHost] = Field(default=None,alias="host",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_host import SecurityHost

