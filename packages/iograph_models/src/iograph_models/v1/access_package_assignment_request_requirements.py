from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AccessPackageAssignmentRequestRequirements(BaseModel):
	allowCustomAssignmentSchedule: Optional[bool] = Field(alias="allowCustomAssignmentSchedule", default=None,)
	isApprovalRequiredForAdd: Optional[bool] = Field(alias="isApprovalRequiredForAdd", default=None,)
	isApprovalRequiredForUpdate: Optional[bool] = Field(alias="isApprovalRequiredForUpdate", default=None,)
	policyDescription: Optional[str] = Field(alias="policyDescription", default=None,)
	policyDisplayName: Optional[str] = Field(alias="policyDisplayName", default=None,)
	policyId: Optional[str] = Field(alias="policyId", default=None,)
	schedule: Optional[EntitlementManagementSchedule] = Field(alias="schedule", default=None,)
	questions: Optional[list[Annotated[Union[AccessPackageMultipleChoiceQuestion, AccessPackageTextInputQuestion],Field(discriminator="odata_type")]]] = Field(alias="questions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .entitlement_management_schedule import EntitlementManagementSchedule
from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
from .access_package_text_input_question import AccessPackageTextInputQuestion
