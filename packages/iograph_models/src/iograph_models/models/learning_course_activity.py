from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class LearningCourseActivity(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	completedDateTime: Optional[datetime] = Field(default=None,alias="completedDateTime",)
	completionPercentage: Optional[int] = Field(default=None,alias="completionPercentage",)
	externalcourseActivityId: Optional[str] = Field(default=None,alias="externalcourseActivityId",)
	learnerUserId: Optional[str] = Field(default=None,alias="learnerUserId",)
	learningContentId: Optional[str] = Field(default=None,alias="learningContentId",)
	learningProviderId: Optional[str] = Field(default=None,alias="learningProviderId",)
	status: Optional[CourseStatus] = Field(default=None,alias="status",)

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
			if mapping_key == "#microsoft.graph.learningAssignment":
				from .learning_assignment import LearningAssignment
				return LearningAssignment.model_validate(data)
			if mapping_key == "#microsoft.graph.learningSelfInitiatedCourse":
				from .learning_self_initiated_course import LearningSelfInitiatedCourse
				return LearningSelfInitiatedCourse.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .course_status import CourseStatus

