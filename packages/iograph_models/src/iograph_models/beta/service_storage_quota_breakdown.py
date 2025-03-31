from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ServiceStorageQuotaBreakdown(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.serviceStorageQuotaBreakdown"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	manageWebUrl: Optional[str] = Field(alias="manageWebUrl", default=None,)
	used: Optional[int] = Field(alias="used", default=None,)

