from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsWorkloadStatus(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	offboardedDateTime: Optional[datetime] = Field(alias="offboardedDateTime", default=None,)
	onboardedDateTime: Optional[datetime] = Field(alias="onboardedDateTime", default=None,)
	onboardingStatus: Optional[ManagedTenantsWorkloadOnboardingStatus | str] = Field(alias="onboardingStatus", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .managed_tenants_workload_onboarding_status import ManagedTenantsWorkloadOnboardingStatus

