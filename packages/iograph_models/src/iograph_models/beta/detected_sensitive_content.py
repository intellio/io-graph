from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DetectedSensitiveContent(BaseModel):
	confidence: Optional[int] = Field(alias="confidence", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	recommendedConfidence: Optional[int] = Field(alias="recommendedConfidence", default=None,)
	uniqueCount: Optional[int] = Field(alias="uniqueCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	classificationAttributes: Optional[list[ClassificationAttribute]] = Field(alias="classificationAttributes", default=None,)
	classificationMethod: Optional[ClassificationMethod | str] = Field(alias="classificationMethod", default=None,)
	matches: Optional[list[SensitiveContentLocation]] = Field(alias="matches", default=None,)
	scope: Optional[SensitiveTypeScope | str] = Field(alias="scope", default=None,)
	sensitiveTypeSource: Optional[SensitiveTypeSource | str] = Field(alias="sensitiveTypeSource", default=None,)

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
			if mapping_key == "#microsoft.graph.machineLearningDetectedSensitiveContent":
				from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent
				return MachineLearningDetectedSensitiveContent.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .classification_attribute import ClassificationAttribute
from .classification_method import ClassificationMethod
from .sensitive_content_location import SensitiveContentLocation
from .sensitive_type_scope import SensitiveTypeScope
from .sensitive_type_source import SensitiveTypeSource
