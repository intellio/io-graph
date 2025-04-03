from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Office365GroupsActivityGroupCounts(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.office365GroupsActivityGroupCounts"] = Field(alias="@odata.type", default="#microsoft.graph.office365GroupsActivityGroupCounts")
	active: Optional[int] = Field(alias="active", default=None,)
	reportDate: Optional[str] = Field(alias="reportDate", default=None,)
	reportPeriod: Optional[str] = Field(alias="reportPeriod", default=None,)
	reportRefreshDate: Optional[str] = Field(alias="reportRefreshDate", default=None,)
	total: Optional[int] = Field(alias="total", default=None,)

