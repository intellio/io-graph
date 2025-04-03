from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class PolicySet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.policySet"] = Field(alias="@odata.type", default="#microsoft.graph.policySet")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	errorCode: Optional[ErrorCode | str] = Field(alias="errorCode", default=None,)
	guidedDeploymentTags: Optional[list[str]] = Field(alias="guidedDeploymentTags", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTags: Optional[list[str]] = Field(alias="roleScopeTags", default=None,)
	status: Optional[PolicySetStatus | str] = Field(alias="status", default=None,)
	assignments: Optional[list[PolicySetAssignment]] = Field(alias="assignments", default=None,)
	items: Optional[list[Annotated[Union[DeviceCompliancePolicyPolicySetItem, DeviceConfigurationPolicySetItem, DeviceManagementConfigurationPolicyPolicySetItem, DeviceManagementScriptPolicySetItem, EnrollmentRestrictionsConfigurationPolicySetItem, IosLobAppProvisioningConfigurationPolicySetItem, ManagedAppProtectionPolicySetItem, ManagedDeviceMobileAppConfigurationPolicySetItem, MdmWindowsInformationProtectionPolicyPolicySetItem, MobileAppPolicySetItem, TargetedManagedAppConfigurationPolicySetItem, Windows10EnrollmentCompletionPageConfigurationPolicySetItem, WindowsAutopilotDeploymentProfilePolicySetItem],Field(discriminator="odata_type")]]] = Field(alias="items", default=None,)

from .error_code import ErrorCode
from .policy_set_status import PolicySetStatus
from .policy_set_assignment import PolicySetAssignment
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
