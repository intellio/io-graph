from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAndAppManagementAssignmentFilter(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	assignmentFilterManagementType: Optional[AssignmentFilterManagementType | str] = Field(alias="assignmentFilterManagementType", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	payloads: Optional[list[PayloadByFilter]] = Field(alias="payloads", default=None,)
	platform: Optional[DevicePlatformType | str] = Field(alias="platform", default=None,)
	roleScopeTags: Optional[list[str]] = Field(alias="roleScopeTags", default=None,)
	rule: Optional[str] = Field(alias="rule", default=None,)

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
			if mapping_key == "#microsoft.graph.payloadCompatibleAssignmentFilter":
				from .payload_compatible_assignment_filter import PayloadCompatibleAssignmentFilter
				return PayloadCompatibleAssignmentFilter.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .assignment_filter_management_type import AssignmentFilterManagementType
from .payload_by_filter import PayloadByFilter
from .device_platform_type import DevicePlatformType

