from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AssignedPlan(BaseModel):
	assignedDateTime: Optional[datetime] = Field(default=None,alias="assignedDateTime",)
	capabilityStatus: Optional[str] = Field(default=None,alias="capabilityStatus",)
	service: Optional[str] = Field(default=None,alias="service",)
	servicePlanId: Optional[UUID] = Field(default=None,alias="servicePlanId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


