from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProvisionedPlan(BaseModel):
	capabilityStatus: Optional[str] = Field(alias="capabilityStatus", default=None,)
	provisioningStatus: Optional[str] = Field(alias="provisioningStatus", default=None,)
	service: Optional[str] = Field(alias="service", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


