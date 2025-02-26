from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class OsVersionCount(BaseModel):
	deviceCount: Optional[int] = Field(default=None,alias="deviceCount",)
	lastUpdateDateTime: Optional[datetime] = Field(default=None,alias="lastUpdateDateTime",)
	osVersion: Optional[str] = Field(default=None,alias="osVersion",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


