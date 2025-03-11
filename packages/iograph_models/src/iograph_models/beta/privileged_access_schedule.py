from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessSchedule(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	createdUsing: Optional[str] = Field(alias="createdUsing",default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime",default=None,)
	scheduleInfo: Optional[RequestSchedule] = Field(alias="scheduleInfo",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)

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

