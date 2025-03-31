from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PermissionsAnalyticsAggregatedResourceSummary(BaseModel):
	findingsCount: Optional[int] = Field(alias="findingsCount", default=None,)
	totalCount: Optional[int] = Field(alias="totalCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

