from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantUserSyncInbound(BaseModel):
	isSyncAllowed: Optional[bool] = Field(alias="isSyncAllowed", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

