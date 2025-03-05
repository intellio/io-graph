from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessSchedule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	createdUsing: Optional[str] = Field(default=None,alias="createdUsing",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	scheduleInfo: Optional[RequestSchedule] = Field(default=None,alias="scheduleInfo",)
	status: Optional[str] = Field(default=None,alias="status",)

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
			if mapping_key == "#microsoft.graph.privilegedAccessGroupAssignmentSchedule":
				from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
				return PrivilegedAccessGroupAssignmentSchedule.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegedAccessGroupEligibilitySchedule":
				from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
				return PrivilegedAccessGroupEligibilitySchedule.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .request_schedule import RequestSchedule

