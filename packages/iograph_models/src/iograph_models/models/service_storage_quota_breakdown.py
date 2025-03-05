from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceStorageQuotaBreakdown(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	manageWebUrl: Optional[str] = Field(default=None,alias="manageWebUrl",)
	used: Optional[int] = Field(default=None,alias="used",)


