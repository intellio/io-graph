from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyConfigurationPartnerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CrossTenantAccessPolicyConfigurationPartner]] = Field(default=None,alias="value",)

from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner

