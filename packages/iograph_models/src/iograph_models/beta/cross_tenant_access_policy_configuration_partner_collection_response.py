from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CrossTenantAccessPolicyConfigurationPartnerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CrossTenantAccessPolicyConfigurationPartner]] = Field(alias="value", default=None,)

from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner

