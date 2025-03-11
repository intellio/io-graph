from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementAutopilotEvent(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accountSetupDuration: Optional[str] = Field(alias="accountSetupDuration",default=None,)
	accountSetupStatus: Optional[WindowsAutopilotDeploymentState | str] = Field(alias="accountSetupStatus",default=None,)
	deploymentDuration: Optional[str] = Field(alias="deploymentDuration",default=None,)
	deploymentEndDateTime: Optional[datetime] = Field(alias="deploymentEndDateTime",default=None,)
	deploymentStartDateTime: Optional[datetime] = Field(alias="deploymentStartDateTime",default=None,)
	deploymentState: Optional[WindowsAutopilotDeploymentState | str] = Field(alias="deploymentState",default=None,)
	deploymentTotalDuration: Optional[str] = Field(alias="deploymentTotalDuration",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	deviceRegisteredDateTime: Optional[datetime] = Field(alias="deviceRegisteredDateTime",default=None,)
	deviceSerialNumber: Optional[str] = Field(alias="deviceSerialNumber",default=None,)
	deviceSetupDuration: Optional[str] = Field(alias="deviceSetupDuration",default=None,)
	deviceSetupStatus: Optional[WindowsAutopilotDeploymentState | str] = Field(alias="deviceSetupStatus",default=None,)
	enrollmentFailureDetails: Optional[str] = Field(alias="enrollmentFailureDetails",default=None,)
	enrollmentStartDateTime: Optional[datetime] = Field(alias="enrollmentStartDateTime",default=None,)
	enrollmentState: Optional[EnrollmentState | str] = Field(alias="enrollmentState",default=None,)
	enrollmentType: Optional[WindowsAutopilotEnrollmentType | str] = Field(alias="enrollmentType",default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime",default=None,)
	managedDeviceName: Optional[str] = Field(alias="managedDeviceName",default=None,)
	osVersion: Optional[str] = Field(alias="osVersion",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	windows10EnrollmentCompletionPageConfigurationDisplayName: Optional[str] = Field(alias="windows10EnrollmentCompletionPageConfigurationDisplayName",default=None,)
	windows10EnrollmentCompletionPageConfigurationId: Optional[str] = Field(alias="windows10EnrollmentCompletionPageConfigurationId",default=None,)
	windowsAutopilotDeploymentProfileDisplayName: Optional[str] = Field(alias="windowsAutopilotDeploymentProfileDisplayName",default=None,)

from .windows_autopilot_deployment_state import WindowsAutopilotDeploymentState
from .windows_autopilot_deployment_state import WindowsAutopilotDeploymentState
from .windows_autopilot_deployment_state import WindowsAutopilotDeploymentState
from .enrollment_state import EnrollmentState
from .windows_autopilot_enrollment_type import WindowsAutopilotEnrollmentType

