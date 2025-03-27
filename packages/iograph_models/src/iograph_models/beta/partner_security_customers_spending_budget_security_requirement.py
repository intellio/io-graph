from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PartnerSecurityCustomersSpendingBudgetSecurityRequirement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	actionUrl: Optional[str] = Field(alias="actionUrl", default=None,)
	complianceStatus: Optional[PartnerSecurityComplianceStatus | str] = Field(alias="complianceStatus", default=None,)
	helpUrl: Optional[str] = Field(alias="helpUrl", default=None,)
	maxScore: Optional[int] = Field(alias="maxScore", default=None,)
	requirementType: Optional[PartnerSecuritySecurityRequirementType | str] = Field(alias="requirementType", default=None,)
	score: Optional[int] = Field(alias="score", default=None,)
	state: Optional[PartnerSecuritySecurityRequirementState | str] = Field(alias="state", default=None,)
	updatedDateTime: Optional[datetime] = Field(alias="updatedDateTime", default=None,)
	customersWithSpendBudgetCount: Optional[int] = Field(alias="customersWithSpendBudgetCount", default=None,)
	totalCustomersCount: Optional[int] = Field(alias="totalCustomersCount", default=None,)

from .partner_security_compliance_status import PartnerSecurityComplianceStatus
from .partner_security_security_requirement_type import PartnerSecuritySecurityRequirementType
from .partner_security_security_requirement_state import PartnerSecuritySecurityRequirementState

