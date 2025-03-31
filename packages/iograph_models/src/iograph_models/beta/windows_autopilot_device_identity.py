from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsAutopilotDeviceIdentity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsAutopilotDeviceIdentity"] = Field(alias="@odata.type",)
	addressableUserName: Optional[str] = Field(alias="addressableUserName", default=None,)
	azureActiveDirectoryDeviceId: Optional[str] = Field(alias="azureActiveDirectoryDeviceId", default=None,)
	azureAdDeviceId: Optional[str] = Field(alias="azureAdDeviceId", default=None,)
	deploymentProfileAssignedDateTime: Optional[datetime] = Field(alias="deploymentProfileAssignedDateTime", default=None,)
	deploymentProfileAssignmentDetailedStatus: Optional[WindowsAutopilotProfileAssignmentDetailedStatus | str] = Field(alias="deploymentProfileAssignmentDetailedStatus", default=None,)
	deploymentProfileAssignmentStatus: Optional[WindowsAutopilotProfileAssignmentStatus | str] = Field(alias="deploymentProfileAssignmentStatus", default=None,)
	deviceAccountPassword: Optional[str] = Field(alias="deviceAccountPassword", default=None,)
	deviceAccountUpn: Optional[str] = Field(alias="deviceAccountUpn", default=None,)
	deviceFriendlyName: Optional[str] = Field(alias="deviceFriendlyName", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enrollmentState: Optional[EnrollmentState | str] = Field(alias="enrollmentState", default=None,)
	groupTag: Optional[str] = Field(alias="groupTag", default=None,)
	lastContactedDateTime: Optional[datetime] = Field(alias="lastContactedDateTime", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	productKey: Optional[str] = Field(alias="productKey", default=None,)
	purchaseOrderIdentifier: Optional[str] = Field(alias="purchaseOrderIdentifier", default=None,)
	remediationState: Optional[WindowsAutopilotDeviceRemediationState | str] = Field(alias="remediationState", default=None,)
	remediationStateLastModifiedDateTime: Optional[datetime] = Field(alias="remediationStateLastModifiedDateTime", default=None,)
	resourceName: Optional[str] = Field(alias="resourceName", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	skuNumber: Optional[str] = Field(alias="skuNumber", default=None,)
	systemFamily: Optional[str] = Field(alias="systemFamily", default=None,)
	userlessEnrollmentStatus: Optional[WindowsAutopilotUserlessEnrollmentStatus | str] = Field(alias="userlessEnrollmentStatus", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	deploymentProfile: Optional[Union[ActiveDirectoryWindowsAutopilotDeploymentProfile, AzureADWindowsAutopilotDeploymentProfile]] = Field(alias="deploymentProfile", default=None,discriminator="odata_type", )
	intendedDeploymentProfile: Optional[Union[ActiveDirectoryWindowsAutopilotDeploymentProfile, AzureADWindowsAutopilotDeploymentProfile]] = Field(alias="intendedDeploymentProfile", default=None,discriminator="odata_type", )

from .windows_autopilot_profile_assignment_detailed_status import WindowsAutopilotProfileAssignmentDetailedStatus
from .windows_autopilot_profile_assignment_status import WindowsAutopilotProfileAssignmentStatus
from .enrollment_state import EnrollmentState
from .windows_autopilot_device_remediation_state import WindowsAutopilotDeviceRemediationState
from .windows_autopilot_userless_enrollment_status import WindowsAutopilotUserlessEnrollmentStatus
from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile
from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile
