from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CommunicationsApplicationInstanceIdentity(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	hidden: Optional[bool] = Field(default=None,alias="hidden",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)


