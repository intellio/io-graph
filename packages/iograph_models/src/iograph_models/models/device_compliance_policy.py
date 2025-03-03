from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceCompliancePolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: Optional[list[DeviceCompliancePolicyAssignment]] = Field(default=None,alias="assignments",)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(default=None,alias="deviceSettingStateSummaries",)
	deviceStatuses: Optional[list[DeviceComplianceDeviceStatus]] = Field(default=None,alias="deviceStatuses",)
	deviceStatusOverview: Optional[DeviceComplianceDeviceOverview] = Field(default=None,alias="deviceStatusOverview",)
	scheduledActionsForRule: Optional[list[DeviceComplianceScheduledActionForRule]] = Field(default=None,alias="scheduledActionsForRule",)
	userStatuses: Optional[list[DeviceComplianceUserStatus]] = Field(default=None,alias="userStatuses",)
	userStatusOverview: Optional[DeviceComplianceUserOverview] = Field(default=None,alias="userStatusOverview",)

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
			if mapping_key == "#microsoft.graph.androidCompliancePolicy":
				from .android_compliance_policy import AndroidCompliancePolicy
				return AndroidCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileCompliancePolicy":
				from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
				return AndroidWorkProfileCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.iosCompliancePolicy":
				from .ios_compliance_policy import IosCompliancePolicy
				return IosCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSCompliancePolicy":
				from .mac_o_s_compliance_policy import MacOSCompliancePolicy
				return MacOSCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10CompliancePolicy":
				from .windows10_compliance_policy import Windows10CompliancePolicy
				return Windows10CompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10MobileCompliancePolicy":
				from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
				return Windows10MobileCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windows81CompliancePolicy":
				from .windows81_compliance_policy import Windows81CompliancePolicy
				return Windows81CompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsPhone81CompliancePolicy":
				from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy
				return WindowsPhone81CompliancePolicy.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_compliance_device_status import DeviceComplianceDeviceStatus
from .device_compliance_device_overview import DeviceComplianceDeviceOverview
from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
from .device_compliance_user_status import DeviceComplianceUserStatus
from .device_compliance_user_overview import DeviceComplianceUserOverview

