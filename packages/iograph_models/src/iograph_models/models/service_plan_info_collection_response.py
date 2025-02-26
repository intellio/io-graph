from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ServicePlanInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ServicePlanInfo] = Field(alias="value",)

from .service_plan_info import ServicePlanInfo

