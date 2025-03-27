from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityThreatSubmission(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
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
			if mapping_key == "#microsoft.graph.security.emailThreatSubmission":
				from .security_email_threat_submission import SecurityEmailThreatSubmission
				return SecurityEmailThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.emailContentThreatSubmission":
				from .security_email_content_threat_submission import SecurityEmailContentThreatSubmission
				return SecurityEmailContentThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.emailUrlThreatSubmission":
				from .security_email_url_threat_submission import SecurityEmailUrlThreatSubmission
				return SecurityEmailUrlThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fileThreatSubmission":
				from .security_file_threat_submission import SecurityFileThreatSubmission
				return SecurityFileThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fileContentThreatSubmission":
				from .security_file_content_threat_submission import SecurityFileContentThreatSubmission
				return SecurityFileContentThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fileUrlThreatSubmission":
				from .security_file_url_threat_submission import SecurityFileUrlThreatSubmission
				return SecurityFileUrlThreatSubmission.model_validate(data)
			if mapping_key == "#microsoft.graph.security.urlThreatSubmission":
				from .security_url_threat_submission import SecurityUrlThreatSubmission
				return SecurityUrlThreatSubmission.model_validate(data)
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

