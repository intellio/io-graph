from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class LearningCourseActivity(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime",default=None,)
	completionPercentage: Optional[int] = Field(alias="completionPercentage",default=None,)
	externalcourseActivityId: Optional[str] = Field(alias="externalcourseActivityId",default=None,)
	learnerUserId: Optional[str] = Field(alias="learnerUserId",default=None,)
	learningContentId: Optional[str] = Field(alias="learningContentId",default=None,)
	learningProviderId: Optional[str] = Field(alias="learningProviderId",default=None,)
	status: Optional[CourseStatus | str] = Field(alias="status",default=None,)

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

