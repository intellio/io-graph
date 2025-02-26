from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class DeviceAndAppManagementAssignmentTarget(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

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
			if mapping_key == "#microsoft.graph.allDevicesAssignmentTarget":
				from .all_devices_assignment_target import AllDevicesAssignmentTarget
				return AllDevicesAssignmentTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.allLicensedUsersAssignmentTarget":
				from .all_licensed_users_assignment_target import AllLicensedUsersAssignmentTarget
				return AllLicensedUsersAssignmentTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.configurationManagerCollectionAssignmentTarget":
				from .configuration_manager_collection_assignment_target import ConfigurationManagerCollectionAssignmentTarget
				return ConfigurationManagerCollectionAssignmentTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.groupAssignmentTarget":
				from .group_assignment_target import GroupAssignmentTarget
				return GroupAssignmentTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.exclusionGroupAssignmentTarget":
				from .exclusion_group_assignment_target import ExclusionGroupAssignmentTarget
				return ExclusionGroupAssignmentTarget.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


