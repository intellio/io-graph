from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityHostTrackerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityHostTracker]] = Field(alias="value", default=None,)

from .security_host_tracker import SecurityHostTracker
