from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CompanySubscription(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	commerceSubscriptionId: Optional[str] = Field(default=None,alias="commerceSubscriptionId",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	isTrial: Optional[bool] = Field(default=None,alias="isTrial",)
	nextLifecycleDateTime: Optional[datetime] = Field(default=None,alias="nextLifecycleDateTime",)
	ownerId: Optional[str] = Field(default=None,alias="ownerId",)
	ownerTenantId: Optional[str] = Field(default=None,alias="ownerTenantId",)
	ownerType: Optional[str] = Field(default=None,alias="ownerType",)
	serviceStatus: Optional[list[ServicePlanInfo]] = Field(default=None,alias="serviceStatus",)
	skuId: Optional[str] = Field(default=None,alias="skuId",)
	skuPartNumber: Optional[str] = Field(default=None,alias="skuPartNumber",)
	status: Optional[str] = Field(default=None,alias="status",)
	totalLicenses: Optional[int] = Field(default=None,alias="totalLicenses",)

from .service_plan_info import ServicePlanInfo

