from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AssignedPlan(BaseModel):
	assignedDateTime: Optional[datetime] = Field(alias="assignedDateTime", default=None,)
	capabilityStatus: Optional[str] = Field(alias="capabilityStatus", default=None,)
	service: Optional[str] = Field(alias="service", default=None,)
	servicePlanId: Optional[UUID] = Field(alias="servicePlanId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


