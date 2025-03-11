from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsTenantStatusInformation(BaseModel):
	delegatedPrivilegeStatus: Optional[ManagedTenantsDelegatedPrivilegeStatus | str] = Field(alias="delegatedPrivilegeStatus",default=None,)
	lastDelegatedPrivilegeRefreshDateTime: Optional[datetime] = Field(alias="lastDelegatedPrivilegeRefreshDateTime",default=None,)
	offboardedByUserId: Optional[str] = Field(alias="offboardedByUserId",default=None,)
	offboardedDateTime: Optional[datetime] = Field(alias="offboardedDateTime",default=None,)
	onboardedByUserId: Optional[str] = Field(alias="onboardedByUserId",default=None,)
	onboardedDateTime: Optional[datetime] = Field(alias="onboardedDateTime",default=None,)
	onboardingStatus: Optional[ManagedTenantsTenantOnboardingStatus | str] = Field(alias="onboardingStatus",default=None,)
	tenantOnboardingEligibilityReason: Optional[ManagedTenantsTenantOnboardingEligibilityReason | str] = Field(alias="tenantOnboardingEligibilityReason",default=None,)
	workloadStatuses: Optional[list[ManagedTenantsWorkloadStatus]] = Field(alias="workloadStatuses",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .managed_tenants_delegated_privilege_status import ManagedTenantsDelegatedPrivilegeStatus
from .managed_tenants_tenant_onboarding_status import ManagedTenantsTenantOnboardingStatus
from .managed_tenants_tenant_onboarding_eligibility_reason import ManagedTenantsTenantOnboardingEligibilityReason
from .managed_tenants_workload_status import ManagedTenantsWorkloadStatus

