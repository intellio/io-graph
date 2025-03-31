from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SubscribedSku(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.subscribedSku"] = Field(alias="@odata.type",)
	accountId: Optional[str] = Field(alias="accountId", default=None,)
	accountName: Optional[str] = Field(alias="accountName", default=None,)
	appliesTo: Optional[str] = Field(alias="appliesTo", default=None,)
	capabilityStatus: Optional[str] = Field(alias="capabilityStatus", default=None,)
	consumedUnits: Optional[int] = Field(alias="consumedUnits", default=None,)
	prepaidUnits: Optional[LicenseUnitsDetail] = Field(alias="prepaidUnits", default=None,)
	servicePlans: Optional[list[ServicePlanInfo]] = Field(alias="servicePlans", default=None,)
	skuId: Optional[UUID] = Field(alias="skuId", default=None,)
	skuPartNumber: Optional[str] = Field(alias="skuPartNumber", default=None,)
	subscriptionIds: Optional[list[str]] = Field(alias="subscriptionIds", default=None,)

from .license_units_detail import LicenseUnitsDetail
from .service_plan_info import ServicePlanInfo
