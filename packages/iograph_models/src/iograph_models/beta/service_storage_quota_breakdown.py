from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceStorageQuotaBreakdown(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	manageWebUrl: Optional[str] = Field(alias="manageWebUrl",default=None,)
	used: Optional[int] = Field(alias="used",default=None,)


