from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessTenantStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.tenantStatus"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.tenantStatus")
	onboardingErrorMessage: Optional[str] = Field(alias="onboardingErrorMessage", default=None,)
	onboardingStatus: Optional[NetworkaccessOnboardingStatus | str] = Field(alias="onboardingStatus", default=None,)

from .networkaccess_onboarding_status import NetworkaccessOnboardingStatus
