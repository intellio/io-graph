from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostPair(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	linkKind: Optional[str] = Field(default=None,alias="linkKind",)
	childHost: Optional[SecurityHost] = Field(default=None,alias="childHost",)
	parentHost: Optional[SecurityHost] = Field(default=None,alias="parentHost",)

from .security_host import SecurityHost
from .security_host import SecurityHost

