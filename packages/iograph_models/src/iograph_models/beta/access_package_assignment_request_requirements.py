from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentRequestRequirements(BaseModel):
	existingAnswers: SerializeAsAny[Optional[list[AccessPackageAnswer]]] = Field(alias="existingAnswers",default=None,)
	isApprovalRequired: Optional[bool] = Field(alias="isApprovalRequired",default=None,)
	isApprovalRequiredForExtension: Optional[bool] = Field(alias="isApprovalRequiredForExtension",default=None,)
	isCustomAssignmentScheduleAllowed: Optional[bool] = Field(alias="isCustomAssignmentScheduleAllowed",default=None,)
	isRequestorJustificationRequired: Optional[bool] = Field(alias="isRequestorJustificationRequired",default=None,)
	policyDescription: Optional[str] = Field(alias="policyDescription",default=None,)
	policyDisplayName: Optional[str] = Field(alias="policyDisplayName",default=None,)
	policyId: Optional[str] = Field(alias="policyId",default=None,)
	questions: SerializeAsAny[Optional[list[AccessPackageQuestion]]] = Field(alias="questions",default=None,)
	schedule: Optional[RequestSchedule] = Field(alias="schedule",default=None,)
	verifiableCredentialRequirementStatus: SerializeAsAny[Optional[VerifiableCredentialRequirementStatus]] = Field(alias="verifiableCredentialRequirementStatus",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .access_package_answer import AccessPackageAnswer
from .access_package_question import AccessPackageQuestion
from .request_schedule import RequestSchedule
from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

