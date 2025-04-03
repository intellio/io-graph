from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Office365ServicesUserCounts(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.office365ServicesUserCounts"] = Field(alias="@odata.type", default="#microsoft.graph.office365ServicesUserCounts")
	exchangeActive: Optional[int] = Field(alias="exchangeActive", default=None,)
	exchangeInactive: Optional[int] = Field(alias="exchangeInactive", default=None,)
	office365Active: Optional[int] = Field(alias="office365Active", default=None,)
	office365Inactive: Optional[int] = Field(alias="office365Inactive", default=None,)
	oneDriveActive: Optional[int] = Field(alias="oneDriveActive", default=None,)
	oneDriveInactive: Optional[int] = Field(alias="oneDriveInactive", default=None,)
	reportPeriod: Optional[str] = Field(alias="reportPeriod", default=None,)
	reportRefreshDate: Optional[str] = Field(alias="reportRefreshDate", default=None,)
	sharePointActive: Optional[int] = Field(alias="sharePointActive", default=None,)
	sharePointInactive: Optional[int] = Field(alias="sharePointInactive", default=None,)
	skypeForBusinessActive: Optional[int] = Field(alias="skypeForBusinessActive", default=None,)
	skypeForBusinessInactive: Optional[int] = Field(alias="skypeForBusinessInactive", default=None,)
	teamsActive: Optional[int] = Field(alias="teamsActive", default=None,)
	teamsInactive: Optional[int] = Field(alias="teamsInactive", default=None,)
	yammerActive: Optional[int] = Field(alias="yammerActive", default=None,)
	yammerInactive: Optional[int] = Field(alias="yammerInactive", default=None,)

