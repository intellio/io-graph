from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEmailThreatSubmission(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.emailThreatSubmission"] = Field(alias="@odata.type", default="#microsoft.graph.security.emailThreatSubmission")
	adminReview: Optional[SecuritySubmissionAdminReview] = Field(alias="adminReview", default=None,)
	category: Optional[SecuritySubmissionCategory | str] = Field(alias="category", default=None,)
	clientSource: Optional[SecuritySubmissionClientSource | str] = Field(alias="clientSource", default=None,)
	contentType: Optional[SecuritySubmissionContentType | str] = Field(alias="contentType", default=None,)
	createdBy: Optional[SecuritySubmissionUserIdentity] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	result: Optional[SecuritySubmissionResult] = Field(alias="result", default=None,)
	source: Optional[SecuritySubmissionSource | str] = Field(alias="source", default=None,)
	status: Optional[SecurityLongRunningOperationStatus | str] = Field(alias="status", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	attackSimulationInfo: Optional[SecurityAttackSimulationInfo] = Field(alias="attackSimulationInfo", default=None,)
	internetMessageId: Optional[str] = Field(alias="internetMessageId", default=None,)
	originalCategory: Optional[SecuritySubmissionCategory | str] = Field(alias="originalCategory", default=None,)
	receivedDateTime: Optional[datetime] = Field(alias="receivedDateTime", default=None,)
	recipientEmailAddress: Optional[str] = Field(alias="recipientEmailAddress", default=None,)
	sender: Optional[str] = Field(alias="sender", default=None,)
	senderIP: Optional[str] = Field(alias="senderIP", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	tenantAllowOrBlockListAction: Optional[SecurityTenantAllowOrBlockListAction] = Field(alias="tenantAllowOrBlockListAction", default=None,)

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
			if mapping_key == "#microsoft.graph.security.emailContentThreatSubmission":
				from .security_email_content_threat_submission import SecurityEmailContentThreatSubmission
				return SecurityEmailContentThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.emailUrlThreatSubmission":
				from .security_email_url_threat_submission import SecurityEmailUrlThreatSubmission
				return SecurityEmailUrlThreatSubmission.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .security_submission_admin_review import SecuritySubmissionAdminReview
from .security_submission_category import SecuritySubmissionCategory
from .security_submission_client_source import SecuritySubmissionClientSource
from .security_submission_content_type import SecuritySubmissionContentType
from .security_submission_user_identity import SecuritySubmissionUserIdentity
from .security_submission_result import SecuritySubmissionResult
from .security_submission_source import SecuritySubmissionSource
from .security_long_running_operation_status import SecurityLongRunningOperationStatus
from .security_attack_simulation_info import SecurityAttackSimulationInfo
from .security_submission_category import SecuritySubmissionCategory
from .security_tenant_allow_or_block_list_action import SecurityTenantAllowOrBlockListAction

