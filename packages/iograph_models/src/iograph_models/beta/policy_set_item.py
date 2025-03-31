from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class PolicySetItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	errorCode: Optional[ErrorCode | str] = Field(alias="errorCode", default=None,)
	guidedDeploymentTags: Optional[list[str]] = Field(alias="guidedDeploymentTags", default=None,)
	itemType: Optional[str] = Field(alias="itemType", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	payloadId: Optional[str] = Field(alias="payloadId", default=None,)
	status: Optional[PolicySetStatus | str] = Field(alias="status", default=None,)

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
			if mapping_key == "#microsoft.graph.deviceCompliancePolicyPolicySetItem":
				from .device_compliance_policy_policy_set_item import DeviceCompliancePolicyPolicySetItem
				return DeviceCompliancePolicyPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceConfigurationPolicySetItem":
				from .device_configuration_policy_set_item import DeviceConfigurationPolicySetItem
				return DeviceConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementConfigurationPolicyPolicySetItem":
				from .device_management_configuration_policy_policy_set_item import DeviceManagementConfigurationPolicyPolicySetItem
				return DeviceManagementConfigurationPolicyPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.deviceManagementScriptPolicySetItem":
				from .device_management_script_policy_set_item import DeviceManagementScriptPolicySetItem
				return DeviceManagementScriptPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.enrollmentRestrictionsConfigurationPolicySetItem":
				from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem
				return EnrollmentRestrictionsConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.iosLobAppProvisioningConfigurationPolicySetItem":
				from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem
				return IosLobAppProvisioningConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.managedAppProtectionPolicySetItem":
				from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem
				return ManagedAppProtectionPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.managedDeviceMobileAppConfigurationPolicySetItem":
				from .managed_device_mobile_app_configuration_policy_set_item import ManagedDeviceMobileAppConfigurationPolicySetItem
				return ManagedDeviceMobileAppConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.mdmWindowsInformationProtectionPolicyPolicySetItem":
				from .mdm_windows_information_protection_policy_policy_set_item import MdmWindowsInformationProtectionPolicyPolicySetItem
				return MdmWindowsInformationProtectionPolicyPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppPolicySetItem":
				from .mobile_app_policy_set_item import MobileAppPolicySetItem
				return MobileAppPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.targetedManagedAppConfigurationPolicySetItem":
				from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem
				return TargetedManagedAppConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.windows10EnrollmentCompletionPageConfigurationPolicySetItem":
				from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem
				return Windows10EnrollmentCompletionPageConfigurationPolicySetItem.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAutopilotDeploymentProfilePolicySetItem":
				from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem
				return WindowsAutopilotDeploymentProfilePolicySetItem.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .error_code import ErrorCode
from .policy_set_status import PolicySetStatus
