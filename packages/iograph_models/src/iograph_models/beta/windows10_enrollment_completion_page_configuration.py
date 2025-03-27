from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10EnrollmentCompletionPageConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windows10EnrollmentCompletionPageConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windows10EnrollmentCompletionPageConfiguration")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceEnrollmentConfigurationType: Optional[DeviceEnrollmentConfigurationType | str] = Field(alias="deviceEnrollmentConfigurationType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[EnrollmentConfigurationAssignment]] = Field(alias="assignments", default=None,)
	allowDeviceResetOnInstallFailure: Optional[bool] = Field(alias="allowDeviceResetOnInstallFailure", default=None,)
	allowDeviceUseOnInstallFailure: Optional[bool] = Field(alias="allowDeviceUseOnInstallFailure", default=None,)
	allowLogCollectionOnInstallFailure: Optional[bool] = Field(alias="allowLogCollectionOnInstallFailure", default=None,)
	allowNonBlockingAppInstallation: Optional[bool] = Field(alias="allowNonBlockingAppInstallation", default=None,)
	blockDeviceSetupRetryByUser: Optional[bool] = Field(alias="blockDeviceSetupRetryByUser", default=None,)
	customErrorMessage: Optional[str] = Field(alias="customErrorMessage", default=None,)
	disableUserStatusTrackingAfterFirstUser: Optional[bool] = Field(alias="disableUserStatusTrackingAfterFirstUser", default=None,)
	installProgressTimeoutInMinutes: Optional[int] = Field(alias="installProgressTimeoutInMinutes", default=None,)
	installQualityUpdates: Optional[bool] = Field(alias="installQualityUpdates", default=None,)
	selectedMobileAppIds: Optional[list[str]] = Field(alias="selectedMobileAppIds", default=None,)
	showInstallationProgress: Optional[bool] = Field(alias="showInstallationProgress", default=None,)
	trackInstallProgressForAutopilotOnly: Optional[bool] = Field(alias="trackInstallProgressForAutopilotOnly", default=None,)

from .device_enrollment_configuration_type import DeviceEnrollmentConfigurationType
from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment

