from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class LicenseAssignmentState(BaseModel):
	assignedByGroup: Optional[str] = Field(default=None,alias="assignedByGroup",)
	disabledPlans: Optional[list[UUID]] = Field(default=None,alias="disabledPlans",)
	error: Optional[str] = Field(default=None,alias="error",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	skuId: Optional[UUID] = Field(default=None,alias="skuId",)
	state: Optional[str] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


