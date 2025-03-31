from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CompanySubscription(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.companySubscription"] = Field(alias="@odata.type",)
	commerceSubscriptionId: Optional[str] = Field(alias="commerceSubscriptionId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isTrial: Optional[bool] = Field(alias="isTrial", default=None,)
	nextLifecycleDateTime: Optional[datetime] = Field(alias="nextLifecycleDateTime", default=None,)
	ownerId: Optional[str] = Field(alias="ownerId", default=None,)
	ownerTenantId: Optional[str] = Field(alias="ownerTenantId", default=None,)
	ownerType: Optional[str] = Field(alias="ownerType", default=None,)
	serviceStatus: Optional[list[ServicePlanInfo]] = Field(alias="serviceStatus", default=None,)
	skuId: Optional[str] = Field(alias="skuId", default=None,)
	skuPartNumber: Optional[str] = Field(alias="skuPartNumber", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	totalLicenses: Optional[int] = Field(alias="totalLicenses", default=None,)

from .service_plan_info import ServicePlanInfo
