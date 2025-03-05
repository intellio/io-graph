from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LicenseDetails(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	servicePlans: Optional[list[ServicePlanInfo]] = Field(default=None,alias="servicePlans",)
	skuId: Optional[UUID] = Field(default=None,alias="skuId",)
	skuPartNumber: Optional[str] = Field(default=None,alias="skuPartNumber",)

from .service_plan_info import ServicePlanInfo

