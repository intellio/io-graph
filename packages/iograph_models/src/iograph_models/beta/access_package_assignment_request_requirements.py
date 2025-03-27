from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentRequestRequirements(BaseModel):
	existingAnswers: Optional[list[Annotated[Union[AccessPackageAnswerString]],Field(discriminator="odata_type")]]] = Field(alias="existingAnswers", default=None,)
	isApprovalRequired: Optional[bool] = Field(alias="isApprovalRequired", default=None,)
	isApprovalRequiredForExtension: Optional[bool] = Field(alias="isApprovalRequiredForExtension", default=None,)
	isCustomAssignmentScheduleAllowed: Optional[bool] = Field(alias="isCustomAssignmentScheduleAllowed", default=None,)
	isRequestorJustificationRequired: Optional[bool] = Field(alias="isRequestorJustificationRequired", default=None,)
	policyDescription: Optional[str] = Field(alias="policyDescription", default=None,)
	policyDisplayName: Optional[str] = Field(alias="policyDisplayName", default=None,)
	policyId: Optional[str] = Field(alias="policyId", default=None,)
	questions: Optional[list[Annotated[Union[AccessPackageMultipleChoiceQuestion, AccessPackageTextInputQuestion]],Field(discriminator="odata_type")]]] = Field(alias="questions", default=None,)
	schedule: Optional[RequestSchedule] = Field(alias="schedule", default=None,)
	verifiableCredentialRequirementStatus: Optional[Union[VerifiableCredentialRequired, VerifiableCredentialRetrieved, VerifiableCredentialVerified]] = Field(alias="verifiableCredentialRequirementStatus", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_package_answer_string import AccessPackageAnswerString
from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
from .access_package_text_input_question import AccessPackageTextInputQuestion
from .request_schedule import RequestSchedule
from .verifiable_credential_required import VerifiableCredentialRequired
from .verifiable_credential_retrieved import VerifiableCredentialRetrieved
from .verifiable_credential_verified import VerifiableCredentialVerified

