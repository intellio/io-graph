from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class UpdatePostRequest(BaseModel):
	addedPolicySetItems: Optional[list[Annotated[Union[DeviceCompliancePolicyPolicySetItem, DeviceConfigurationPolicySetItem, DeviceManagementConfigurationPolicyPolicySetItem, DeviceManagementScriptPolicySetItem, EnrollmentRestrictionsConfigurationPolicySetItem, IosLobAppProvisioningConfigurationPolicySetItem, ManagedAppProtectionPolicySetItem, ManagedDeviceMobileAppConfigurationPolicySetItem, MdmWindowsInformationProtectionPolicyPolicySetItem, MobileAppPolicySetItem, TargetedManagedAppConfigurationPolicySetItem, Windows10EnrollmentCompletionPageConfigurationPolicySetItem, WindowsAutopilotDeploymentProfilePolicySetItem],Field(discriminator="odata_type")]]] = Field(alias="addedPolicySetItems", default=None,)
	updatedPolicySetItems: Optional[list[Annotated[Union[DeviceCompliancePolicyPolicySetItem, DeviceConfigurationPolicySetItem, DeviceManagementConfigurationPolicyPolicySetItem, DeviceManagementScriptPolicySetItem, EnrollmentRestrictionsConfigurationPolicySetItem, IosLobAppProvisioningConfigurationPolicySetItem, ManagedAppProtectionPolicySetItem, ManagedDeviceMobileAppConfigurationPolicySetItem, MdmWindowsInformationProtectionPolicyPolicySetItem, MobileAppPolicySetItem, TargetedManagedAppConfigurationPolicySetItem, Windows10EnrollmentCompletionPageConfigurationPolicySetItem, WindowsAutopilotDeploymentProfilePolicySetItem],Field(discriminator="odata_type")]]] = Field(alias="updatedPolicySetItems", default=None,)
	deletedPolicySetItems: Optional[list[str]] = Field(alias="deletedPolicySetItems", default=None,)
	assignments: Optional[list[PolicySetAssignment]] = Field(alias="assignments", default=None,)

from .device_compliance_policy_policy_set_item import DeviceCompliancePolicyPolicySetItem
from .device_configuration_policy_set_item import DeviceConfigurationPolicySetItem
from .device_management_configuration_policy_policy_set_item import DeviceManagementConfigurationPolicyPolicySetItem
from .device_management_script_policy_set_item import DeviceManagementScriptPolicySetItem
from .enrollment_restrictions_configuration_policy_set_item import EnrollmentRestrictionsConfigurationPolicySetItem
from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem
from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem
from .managed_device_mobile_app_configuration_policy_set_item import ManagedDeviceMobileAppConfigurationPolicySetItem
from .mdm_windows_information_protection_policy_policy_set_item import MdmWindowsInformationProtectionPolicyPolicySetItem
from .mobile_app_policy_set_item import MobileAppPolicySetItem
from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem
from .windows10_enrollment_completion_page_configuration_policy_set_item import Windows10EnrollmentCompletionPageConfigurationPolicySetItem
from .windows_autopilot_deployment_profile_policy_set_item import WindowsAutopilotDeploymentProfilePolicySetItem
from .policy_set_assignment import PolicySetAssignment
