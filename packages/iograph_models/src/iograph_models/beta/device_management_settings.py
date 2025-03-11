from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettings(BaseModel):
	androidDeviceAdministratorEnrollmentEnabled: Optional[bool] = Field(alias="androidDeviceAdministratorEnrollmentEnabled",default=None,)
	derivedCredentialProvider: Optional[DerivedCredentialProviderType | str] = Field(alias="derivedCredentialProvider",default=None,)
	derivedCredentialUrl: Optional[str] = Field(alias="derivedCredentialUrl",default=None,)
	deviceComplianceCheckinThresholdDays: Optional[int] = Field(alias="deviceComplianceCheckinThresholdDays",default=None,)
	deviceInactivityBeforeRetirementInDay: Optional[int] = Field(alias="deviceInactivityBeforeRetirementInDay",default=None,)
	enableAutopilotDiagnostics: Optional[bool] = Field(alias="enableAutopilotDiagnostics",default=None,)
	enableDeviceGroupMembershipReport: Optional[bool] = Field(alias="enableDeviceGroupMembershipReport",default=None,)
	enableEnhancedTroubleshootingExperience: Optional[bool] = Field(alias="enableEnhancedTroubleshootingExperience",default=None,)
	enableLogCollection: Optional[bool] = Field(alias="enableLogCollection",default=None,)
	enhancedJailBreak: Optional[bool] = Field(alias="enhancedJailBreak",default=None,)
	ignoreDevicesForUnsupportedSettingsEnabled: Optional[bool] = Field(alias="ignoreDevicesForUnsupportedSettingsEnabled",default=None,)
	isScheduledActionEnabled: Optional[bool] = Field(alias="isScheduledActionEnabled",default=None,)
	m365AppDiagnosticsEnabled: Optional[bool] = Field(alias="m365AppDiagnosticsEnabled",default=None,)
	secureByDefault: Optional[bool] = Field(alias="secureByDefault",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .derived_credential_provider_type import DerivedCredentialProviderType

