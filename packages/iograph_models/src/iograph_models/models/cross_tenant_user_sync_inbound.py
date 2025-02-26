from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantUserSyncInbound(BaseModel):
	isSyncAllowed: Optional[bool] = Field(default=None,alias="isSyncAllowed",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


