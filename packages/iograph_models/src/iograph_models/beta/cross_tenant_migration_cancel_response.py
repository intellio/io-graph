from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantMigrationCancelResponse(BaseModel):
	message: Optional[str] = Field(alias="message", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

