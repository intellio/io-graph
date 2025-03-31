from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostPortBanner(BaseModel):
	banner: Optional[str] = Field(alias="banner", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	scanProtocol: Optional[str] = Field(alias="scanProtocol", default=None,)
	timesObserved: Optional[int] = Field(alias="timesObserved", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

