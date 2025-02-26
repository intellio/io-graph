from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UsageDetails(BaseModel):
	lastAccessedDateTime: Optional[datetime] = Field(default=None,alias="lastAccessedDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


