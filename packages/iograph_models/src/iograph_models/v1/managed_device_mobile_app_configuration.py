from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedDeviceMobileAppConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	targetedMobileApps: Optional[list[str]] = Field(alias="targetedMobileApps",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[ManagedDeviceMobileAppConfigurationAssignment]] = Field(alias="assignments",default=None,)
	deviceStatuses: Optional[list[ManagedDeviceMobileAppConfigurationDeviceStatus]] = Field(alias="deviceStatuses",default=None,)
	deviceStatusSummary: Optional[ManagedDeviceMobileAppConfigurationDeviceSummary] = Field(alias="deviceStatusSummary",default=None,)
	userStatuses: Optional[list[ManagedDeviceMobileAppConfigurationUserStatus]] = Field(alias="userStatuses",default=None,)
	userStatusSummary: Optional[ManagedDeviceMobileAppConfigurationUserSummary] = Field(alias="userStatusSummary",default=None,)

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
			if mapping_key == "#microsoft.graph.iosMobileAppConfiguration":
				from .ios_mobile_app_configuration import IosMobileAppConfiguration
				return IosMobileAppConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary

