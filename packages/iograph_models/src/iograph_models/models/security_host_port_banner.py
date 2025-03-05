from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostPortBanner(BaseModel):
	banner: Optional[str] = Field(default=None,alias="banner",)
	firstSeenDateTime: Optional[datetime] = Field(default=None,alias="firstSeenDateTime",)
	lastSeenDateTime: Optional[datetime] = Field(default=None,alias="lastSeenDateTime",)
	scanProtocol: Optional[str] = Field(default=None,alias="scanProtocol",)
	timesObserved: Optional[int] = Field(default=None,alias="timesObserved",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


