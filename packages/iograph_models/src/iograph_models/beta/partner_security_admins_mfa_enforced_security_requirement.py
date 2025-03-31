from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PartnerSecurityAdminsMfaEnforcedSecurityRequirement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.partner.security.adminsMfaEnforcedSecurityRequirement"] = Field(alias="@odata.type",)
	actionUrl: Optional[str] = Field(alias="actionUrl", default=None,)
	complianceStatus: Optional[PartnerSecurityComplianceStatus | str] = Field(alias="complianceStatus", default=None,)
	helpUrl: Optional[str] = Field(alias="helpUrl", default=None,)
	maxScore: Optional[int] = Field(alias="maxScore", default=None,)
	requirementType: Optional[PartnerSecuritySecurityRequirementType | str] = Field(alias="requirementType", default=None,)
	score: Optional[int] = Field(alias="score", default=None,)
	state: Optional[PartnerSecuritySecurityRequirementState | str] = Field(alias="state", default=None,)
	updatedDateTime: Optional[datetime] = Field(alias="updatedDateTime", default=None,)
	adminsRequiredNotUsingMfaCount: Optional[int] = Field(alias="adminsRequiredNotUsingMfaCount", default=None,)
	legacyPerUserMfaStatus: Optional[PartnerSecurityPolicyStatus | str] = Field(alias="legacyPerUserMfaStatus", default=None,)
	mfaConditionalAccessPolicyStatus: Optional[PartnerSecurityPolicyStatus | str] = Field(alias="mfaConditionalAccessPolicyStatus", default=None,)
	mfaEnabledAdminsCount: Optional[int] = Field(alias="mfaEnabledAdminsCount", default=None,)
	mfaEnabledUsersCount: Optional[int] = Field(alias="mfaEnabledUsersCount", default=None,)
	securityDefaultsStatus: Optional[PartnerSecurityPolicyStatus | str] = Field(alias="securityDefaultsStatus", default=None,)
	totalAdminsCount: Optional[int] = Field(alias="totalAdminsCount", default=None,)
	totalUsersCount: Optional[int] = Field(alias="totalUsersCount", default=None,)
	usersRequiredNotUsingMfaCount: Optional[int] = Field(alias="usersRequiredNotUsingMfaCount", default=None,)

from .partner_security_compliance_status import PartnerSecurityComplianceStatus
from .partner_security_security_requirement_type import PartnerSecuritySecurityRequirementType
from .partner_security_security_requirement_state import PartnerSecuritySecurityRequirementState
from .partner_security_policy_status import PartnerSecurityPolicyStatus
