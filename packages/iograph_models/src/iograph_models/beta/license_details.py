from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class LicenseDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.licenseDetails"] = Field(alias="@odata.type",)
	servicePlans: Optional[list[ServicePlanInfo]] = Field(alias="servicePlans", default=None,)
	skuId: Optional[UUID] = Field(alias="skuId", default=None,)
	skuPartNumber: Optional[str] = Field(alias="skuPartNumber", default=None,)

from .service_plan_info import ServicePlanInfo
