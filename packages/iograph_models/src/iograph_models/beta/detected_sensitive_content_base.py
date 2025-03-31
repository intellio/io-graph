from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DetectedSensitiveContentBase(BaseModel):
	confidence: Optional[int] = Field(alias="confidence", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	recommendedConfidence: Optional[int] = Field(alias="recommendedConfidence", default=None,)
	uniqueCount: Optional[int] = Field(alias="uniqueCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.exactMatchDetectedSensitiveContent":
				from .exact_match_detected_sensitive_content import ExactMatchDetectedSensitiveContent
				return ExactMatchDetectedSensitiveContent.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

