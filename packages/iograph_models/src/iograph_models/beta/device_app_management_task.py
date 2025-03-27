from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAppManagementTask(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	assignedTo: Optional[str] = Field(alias="assignedTo", default=None,)
	category: Optional[DeviceAppManagementTaskCategory | str] = Field(alias="category", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	creator: Optional[str] = Field(alias="creator", default=None,)
	creatorNotes: Optional[str] = Field(alias="creatorNotes", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	dueDateTime: Optional[datetime] = Field(alias="dueDateTime", default=None,)
	priority: Optional[DeviceAppManagementTaskPriority | str] = Field(alias="priority", default=None,)
	status: Optional[DeviceAppManagementTaskStatus | str] = Field(alias="status", default=None,)

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
			if mapping_key == "#microsoft.graph.appVulnerabilityTask":
				from .app_vulnerability_task import AppVulnerabilityTask
				return AppVulnerabilityTask.model_validate(data)
			if mapping_key == "#microsoft.graph.securityConfigurationTask":
				from .security_configuration_task import SecurityConfigurationTask
				return SecurityConfigurationTask.model_validate(data)
			if mapping_key == "#microsoft.graph.unmanagedDeviceDiscoveryTask":
				from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask
				return UnmanagedDeviceDiscoveryTask.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .device_app_management_task_category import DeviceAppManagementTaskCategory
from .device_app_management_task_priority import DeviceAppManagementTaskPriority
from .device_app_management_task_status import DeviceAppManagementTaskStatus

