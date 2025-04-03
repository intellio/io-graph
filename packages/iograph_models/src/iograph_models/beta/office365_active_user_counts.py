from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Office365ActiveUserCounts(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.office365ActiveUserCounts"] = Field(alias="@odata.type", default="#microsoft.graph.office365ActiveUserCounts")
	exchange: Optional[int] = Field(alias="exchange", default=None,)
	office365: Optional[int] = Field(alias="office365", default=None,)
	oneDrive: Optional[int] = Field(alias="oneDrive", default=None,)
	reportDate: Optional[str] = Field(alias="reportDate", default=None,)
	reportPeriod: Optional[str] = Field(alias="reportPeriod", default=None,)
	reportRefreshDate: Optional[str] = Field(alias="reportRefreshDate", default=None,)
	sharePoint: Optional[int] = Field(alias="sharePoint", default=None,)
	skypeForBusiness: Optional[int] = Field(alias="skypeForBusiness", default=None,)
	teams: Optional[int] = Field(alias="teams", default=None,)
	yammer: Optional[int] = Field(alias="yammer", default=None,)

