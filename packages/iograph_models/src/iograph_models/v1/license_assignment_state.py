from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class LicenseAssignmentState(BaseModel):
	assignedByGroup: Optional[str] = Field(alias="assignedByGroup", default=None,)
	disabledPlans: Optional[list[UUID]] = Field(alias="disabledPlans", default=None,)
	error: Optional[str] = Field(alias="error", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	skuId: Optional[UUID] = Field(alias="skuId", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


