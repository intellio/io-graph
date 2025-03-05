from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SubscribedSku(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	accountId: Optional[str] = Field(default=None,alias="accountId",)
	accountName: Optional[str] = Field(default=None,alias="accountName",)
	appliesTo: Optional[str] = Field(default=None,alias="appliesTo",)
	capabilityStatus: Optional[str] = Field(default=None,alias="capabilityStatus",)
	consumedUnits: Optional[int] = Field(default=None,alias="consumedUnits",)
	prepaidUnits: Optional[LicenseUnitsDetail] = Field(default=None,alias="prepaidUnits",)
	servicePlans: Optional[list[ServicePlanInfo]] = Field(default=None,alias="servicePlans",)
	skuId: Optional[UUID] = Field(default=None,alias="skuId",)
	skuPartNumber: Optional[str] = Field(default=None,alias="skuPartNumber",)
	subscriptionIds: Optional[list[str]] = Field(default=None,alias="subscriptionIds",)

from .license_units_detail import LicenseUnitsDetail
from .service_plan_info import ServicePlanInfo

