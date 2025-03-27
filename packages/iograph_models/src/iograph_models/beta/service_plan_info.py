from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePlanInfo(BaseModel):
	appliesTo: Optional[str] = Field(alias="appliesTo", default=None,)
	provisioningStatus: Optional[str] = Field(alias="provisioningStatus", default=None,)
	servicePlanId: Optional[UUID] = Field(alias="servicePlanId", default=None,)
	servicePlanName: Optional[str] = Field(alias="servicePlanName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


