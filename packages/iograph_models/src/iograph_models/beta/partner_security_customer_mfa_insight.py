from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PartnerSecurityCustomerMfaInsight(BaseModel):
	compliantAdminsCount: Optional[int] = Field(alias="compliantAdminsCount", default=None,)
	compliantNonAdminsCount: Optional[int] = Field(alias="compliantNonAdminsCount", default=None,)
	legacyPerUserMfaStatus: Optional[PartnerSecurityPolicyStatus | str] = Field(alias="legacyPerUserMfaStatus", default=None,)
	mfaConditionalAccessPolicyStatus: Optional[PartnerSecurityPolicyStatus | str] = Field(alias="mfaConditionalAccessPolicyStatus", default=None,)
	securityDefaultsStatus: Optional[PartnerSecurityPolicyStatus | str] = Field(alias="securityDefaultsStatus", default=None,)
	totalUsersCount: Optional[int] = Field(alias="totalUsersCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .partner_security_policy_status import PartnerSecurityPolicyStatus
