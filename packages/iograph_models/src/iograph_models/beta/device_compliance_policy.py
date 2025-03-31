from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DeviceCompliancePolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceCompliancePolicyAssignment]] = Field(alias="assignments", default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries", default=None,)
	deviceStatuses: Optional[list[DeviceComplianceDeviceStatus]] = Field(alias="deviceStatuses", default=None,)
	deviceStatusOverview: Optional[DeviceComplianceDeviceOverview] = Field(alias="deviceStatusOverview", default=None,)
	scheduledActionsForRule: Optional[list[DeviceComplianceScheduledActionForRule]] = Field(alias="scheduledActionsForRule", default=None,)
	userStatuses: Optional[list[DeviceComplianceUserStatus]] = Field(alias="userStatuses", default=None,)
	userStatusOverview: Optional[DeviceComplianceUserOverview] = Field(alias="userStatusOverview", default=None,)

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
			if mapping_key == "#microsoft.graph.androidDeviceOwnerCompliancePolicy":
				from .android_device_owner_compliance_policy import AndroidDeviceOwnerCompliancePolicy
				return AndroidDeviceOwnerCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.androidForWorkCompliancePolicy":
				from .android_for_work_compliance_policy import AndroidForWorkCompliancePolicy
				return AndroidForWorkCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.androidWorkProfileCompliancePolicy":
				from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
				return AndroidWorkProfileCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.aospDeviceOwnerCompliancePolicy":
				from .aosp_device_owner_compliance_policy import AospDeviceOwnerCompliancePolicy
				return AospDeviceOwnerCompliancePolicy.model_validate(data)
			if mapping_key == "#microsoft.graph.defaultDeviceCompliancePolicy":
				from .default_device_compliance_policy import DefaultDeviceCompliancePolicy
				return DefaultDeviceCompliancePolicy.model_validate(data)
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
