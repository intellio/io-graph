from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class PrivilegedAccessScheduleInstance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)

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
			if mapping_key == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleInstance":
				from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
				return PrivilegedAccessGroupAssignmentScheduleInstance.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleInstance":
				from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
				return PrivilegedAccessGroupEligibilityScheduleInstance.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


