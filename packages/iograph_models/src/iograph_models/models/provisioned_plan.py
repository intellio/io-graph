from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProvisionedPlan(BaseModel):
	capabilityStatus: Optional[str] = Field(default=None,alias="capabilityStatus",)
	provisioningStatus: Optional[str] = Field(default=None,alias="provisioningStatus",)
	service: Optional[str] = Field(default=None,alias="service",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


