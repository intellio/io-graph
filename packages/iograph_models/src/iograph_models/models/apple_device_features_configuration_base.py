from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class AppleDeviceFeaturesConfigurationBase(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(default=None,alias="assignments",)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(default=None,alias="deviceSettingStateSummaries",)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(default=None,alias="deviceStatuses",)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(default=None,alias="deviceStatusOverview",)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(default=None,alias="userStatuses",)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(default=None,alias="userStatusOverview",)

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
			if mapping_key == "#microsoft.graph.iosDeviceFeaturesConfiguration":
				from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
				return IosDeviceFeaturesConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSDeviceFeaturesConfiguration":
				from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
				return MacOSDeviceFeaturesConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview

