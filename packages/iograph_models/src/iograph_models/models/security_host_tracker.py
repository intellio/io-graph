from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostTracker(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	kind: Optional[str] = Field(default=None,alias="kind",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	value: Optional[str] = Field(default=None,alias="value",)
	host: Optional[SecurityHost] = Field(default=None,alias="host",)

from .security_host import SecurityHost

