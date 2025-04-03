from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MacOSSoftwareUpdateCategorySummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.macOSSoftwareUpdateCategorySummary"] = Field(alias="@odata.type", default="#microsoft.graph.macOSSoftwareUpdateCategorySummary")
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	failedUpdateCount: Optional[int] = Field(alias="failedUpdateCount", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	successfulUpdateCount: Optional[int] = Field(alias="successfulUpdateCount", default=None,)
	totalUpdateCount: Optional[int] = Field(alias="totalUpdateCount", default=None,)
	updateCategory: Optional[MacOSSoftwareUpdateCategory | str] = Field(alias="updateCategory", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	updateStateSummaries: Optional[list[MacOSSoftwareUpdateStateSummary]] = Field(alias="updateStateSummaries", default=None,)

from .mac_o_s_software_update_category import MacOSSoftwareUpdateCategory
from .mac_o_s_software_update_state_summary import MacOSSoftwareUpdateStateSummary
