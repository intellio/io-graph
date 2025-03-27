from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsCredentialUserRegistrationsSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime", default=None,)
	mfaAndSsprCapableUserCount: Optional[int] = Field(alias="mfaAndSsprCapableUserCount", default=None,)
	mfaConditionalAccessPolicyState: Optional[str] = Field(alias="mfaConditionalAccessPolicyState", default=None,)
	mfaExcludedUserCount: Optional[int] = Field(alias="mfaExcludedUserCount", default=None,)
	mfaRegisteredUserCount: Optional[int] = Field(alias="mfaRegisteredUserCount", default=None,)
	securityDefaultsEnabled: Optional[bool] = Field(alias="securityDefaultsEnabled", default=None,)
	ssprEnabledUserCount: Optional[int] = Field(alias="ssprEnabledUserCount", default=None,)
	ssprRegisteredUserCount: Optional[int] = Field(alias="ssprRegisteredUserCount", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	tenantLicenseType: Optional[str] = Field(alias="tenantLicenseType", default=None,)
	totalUserCount: Optional[int] = Field(alias="totalUserCount", default=None,)


