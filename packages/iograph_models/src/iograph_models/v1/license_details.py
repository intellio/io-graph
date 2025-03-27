from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LicenseDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	servicePlans: Optional[list[ServicePlanInfo]] = Field(alias="servicePlans", default=None,)
	skuId: Optional[UUID] = Field(alias="skuId", default=None,)
	skuPartNumber: Optional[str] = Field(alias="skuPartNumber", default=None,)

from .service_plan_info import ServicePlanInfo

