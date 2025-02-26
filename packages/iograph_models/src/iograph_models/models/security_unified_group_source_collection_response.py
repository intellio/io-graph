from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityUnifiedGroupSourceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityUnifiedGroupSource] = Field(alias="value",)

from .security_unified_group_source import SecurityUnifiedGroupSource

