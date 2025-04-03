from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Office365GroupsActivityStorage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.office365GroupsActivityStorage"] = Field(alias="@odata.type", default="#microsoft.graph.office365GroupsActivityStorage")
	mailboxStorageUsedInBytes: Optional[int] = Field(alias="mailboxStorageUsedInBytes", default=None,)
	reportDate: Optional[str] = Field(alias="reportDate", default=None,)
	reportPeriod: Optional[str] = Field(alias="reportPeriod", default=None,)
	reportRefreshDate: Optional[str] = Field(alias="reportRefreshDate", default=None,)
	siteStorageUsedInBytes: Optional[int] = Field(alias="siteStorageUsedInBytes", default=None,)

