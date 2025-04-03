from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MacOSSoftwareUpdateAccountSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.macOSSoftwareUpdateAccountSummary"] = Field(alias="@odata.type", default="#microsoft.graph.macOSSoftwareUpdateAccountSummary")
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	failedUpdateCount: Optional[int] = Field(alias="failedUpdateCount", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	successfulUpdateCount: Optional[int] = Field(alias="successfulUpdateCount", default=None,)
	totalUpdateCount: Optional[int] = Field(alias="totalUpdateCount", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	categorySummaries: Optional[list[MacOSSoftwareUpdateCategorySummary]] = Field(alias="categorySummaries", default=None,)

from .mac_o_s_software_update_category_summary import MacOSSoftwareUpdateCategorySummary
