from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostComponent(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	category: Optional[str] = Field(default=None,alias="category",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	name: Optional[str] = Field(default=None,alias="name",)
	version: Optional[str] = Field(default=None,alias="version",)
	host: SerializeAsAny[Optional[SecurityHost]] = Field(default=None,alias="host",)

from .security_host import SecurityHost

