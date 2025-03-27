from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Office365GroupsActivityGroupCounts(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	active: Optional[int] = Field(alias="active", default=None,)
	reportDate: Optional[str] = Field(alias="reportDate", default=None,)
	reportPeriod: Optional[str] = Field(alias="reportPeriod", default=None,)
	reportRefreshDate: Optional[str] = Field(alias="reportRefreshDate", default=None,)
	total: Optional[int] = Field(alias="total", default=None,)


