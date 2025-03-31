from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class PartnerSecuritySecurityRequirement(BaseModel):
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

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.partner.security.adminsMfaEnforcedSecurityRequirement":
				from .partner_security_admins_mfa_enforced_security_requirement import PartnerSecurityAdminsMfaEnforcedSecurityRequirement
				return PartnerSecurityAdminsMfaEnforcedSecurityRequirement.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.customersMfaEnforcedSecurityRequirement":
				from .partner_security_customers_mfa_enforced_security_requirement import PartnerSecurityCustomersMfaEnforcedSecurityRequirement
				return PartnerSecurityCustomersMfaEnforcedSecurityRequirement.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.customersSpendingBudgetSecurityRequirement":
				from .partner_security_customers_spending_budget_security_requirement import PartnerSecurityCustomersSpendingBudgetSecurityRequirement
				return PartnerSecurityCustomersSpendingBudgetSecurityRequirement.model_validate(data)
			if mapping_key == "#microsoft.graph.partner.security.responseTimeSecurityRequirement":
				from .partner_security_response_time_security_requirement import PartnerSecurityResponseTimeSecurityRequirement
				return PartnerSecurityResponseTimeSecurityRequirement.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .partner_security_compliance_status import PartnerSecurityComplianceStatus
from .partner_security_security_requirement_type import PartnerSecuritySecurityRequirementType
from .partner_security_security_requirement_state import PartnerSecuritySecurityRequirementState
