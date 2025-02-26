from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityHostTrackerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityHostTracker] = Field(alias="value",)

from .security_host_tracker import SecurityHostTracker

