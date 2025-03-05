from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePlanInfo(BaseModel):
	appliesTo: Optional[str] = Field(default=None,alias="appliesTo",)
	provisioningStatus: Optional[str] = Field(default=None,alias="provisioningStatus",)
	servicePlanId: Optional[UUID] = Field(default=None,alias="servicePlanId",)
	servicePlanName: Optional[str] = Field(default=None,alias="servicePlanName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


