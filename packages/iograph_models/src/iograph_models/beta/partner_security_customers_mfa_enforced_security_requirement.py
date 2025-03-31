from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PartnerSecurityCustomersMfaEnforcedSecurityRequirement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.partner.security.customersMfaEnforcedSecurityRequirement"] = Field(alias="@odata.type",)
	actionUrl: Optional[str] = Field(alias="actionUrl", default=None,)
	complianceStatus: Optional[PartnerSecurityComplianceStatus | str] = Field(alias="complianceStatus", default=None,)
	helpUrl: Optional[str] = Field(alias="helpUrl", default=None,)
	maxScore: Optional[int] = Field(alias="maxScore", default=None,)
	requirementType: Optional[PartnerSecuritySecurityRequirementType | str] = Field(alias="requirementType", default=None,)
	score: Optional[int] = Field(alias="score", default=None,)
	state: Optional[PartnerSecuritySecurityRequirementState | str] = Field(alias="state", default=None,)
	updatedDateTime: Optional[datetime] = Field(alias="updatedDateTime", default=None,)
	compliantTenantCount: Optional[int] = Field(alias="compliantTenantCount", default=None,)
	totalTenantCount: Optional[int] = Field(alias="totalTenantCount", default=None,)

from .partner_security_compliance_status import PartnerSecurityComplianceStatus
from .partner_security_security_requirement_type import PartnerSecuritySecurityRequirementType
from .partner_security_security_requirement_state import PartnerSecuritySecurityRequirementState
