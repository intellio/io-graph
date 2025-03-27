from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessTenantStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	onboardingErrorMessage: Optional[str] = Field(alias="onboardingErrorMessage", default=None,)
	onboardingStatus: Optional[NetworkaccessOnboardingStatus | str] = Field(alias="onboardingStatus", default=None,)

from .networkaccess_onboarding_status import NetworkaccessOnboardingStatus

