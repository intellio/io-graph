from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class ThreatAssessmentRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	category: Optional[ThreatCategory] = Field(default=None,alias="category",)
	contentType: Optional[ThreatAssessmentContentType] = Field(default=None,alias="contentType",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	expectedAssessment: Optional[ThreatExpectedAssessment] = Field(default=None,alias="expectedAssessment",)
	requestSource: Optional[ThreatAssessmentRequestSource] = Field(default=None,alias="requestSource",)
	status: Optional[ThreatAssessmentStatus] = Field(default=None,alias="status",)
	results: Optional[list[ThreatAssessmentResult]] = Field(default=None,alias="results",)

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
			if mapping_key == "#microsoft.graph.emailFileAssessmentRequest":
				from .email_file_assessment_request import EmailFileAssessmentRequest
				return EmailFileAssessmentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.fileAssessmentRequest":
				from .file_assessment_request import FileAssessmentRequest
				return FileAssessmentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.mailAssessmentRequest":
				from .mail_assessment_request import MailAssessmentRequest
				return MailAssessmentRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.urlAssessmentRequest":
				from .url_assessment_request import UrlAssessmentRequest
				return UrlAssessmentRequest.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .threat_category import ThreatCategory
from .threat_assessment_content_type import ThreatAssessmentContentType
from .identity_set import IdentitySet
from .threat_expected_assessment import ThreatExpectedAssessment
from .threat_assessment_request_source import ThreatAssessmentRequestSource
from .threat_assessment_status import ThreatAssessmentStatus
from .threat_assessment_result import ThreatAssessmentResult

