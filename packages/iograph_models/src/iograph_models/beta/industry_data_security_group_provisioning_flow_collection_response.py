from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IndustryDataSecurityGroupProvisioningFlowCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IndustryDataSecurityGroupProvisioningFlow]] = Field(alias="value", default=None,)

from .industry_data_security_group_provisioning_flow import IndustryDataSecurityGroupProvisioningFlow
