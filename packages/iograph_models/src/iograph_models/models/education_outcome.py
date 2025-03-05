from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationOutcome(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)

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
			if mapping_key == "#microsoft.graph.educationFeedbackOutcome":
				from .education_feedback_outcome import EducationFeedbackOutcome
				return EducationFeedbackOutcome.model_validate(data)
			if mapping_key == "#microsoft.graph.educationFeedbackResourceOutcome":
				from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
				return EducationFeedbackResourceOutcome.model_validate(data)
			if mapping_key == "#microsoft.graph.educationPointsOutcome":
				from .education_points_outcome import EducationPointsOutcome
				return EducationPointsOutcome.model_validate(data)
			if mapping_key == "#microsoft.graph.educationRubricOutcome":
				from .education_rubric_outcome import EducationRubricOutcome
				return EducationRubricOutcome.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_set import IdentitySet

