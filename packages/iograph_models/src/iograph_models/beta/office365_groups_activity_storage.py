from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Office365GroupsActivityStorage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	mailboxStorageUsedInBytes: Optional[int] = Field(alias="mailboxStorageUsedInBytes", default=None,)
	reportDate: Optional[str] = Field(alias="reportDate", default=None,)
	reportPeriod: Optional[str] = Field(alias="reportPeriod", default=None,)
	reportRefreshDate: Optional[str] = Field(alias="reportRefreshDate", default=None,)
	siteStorageUsedInBytes: Optional[int] = Field(alias="siteStorageUsedInBytes", default=None,)


