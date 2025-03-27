from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerCompliancePolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidDeviceOwnerCompliancePolicy"] = Field(alias="@odata.type", default="#microsoft.graph.androidDeviceOwnerCompliancePolicy")
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
	advancedThreatProtectionRequiredSecurityLevel: Optional[DeviceThreatProtectionLevel | str] = Field(alias="advancedThreatProtectionRequiredSecurityLevel", default=None,)
	deviceThreatProtectionEnabled: Optional[bool] = Field(alias="deviceThreatProtectionEnabled", default=None,)
	deviceThreatProtectionRequiredSecurityLevel: Optional[DeviceThreatProtectionLevel | str] = Field(alias="deviceThreatProtectionRequiredSecurityLevel", default=None,)
	minAndroidSecurityPatchLevel: Optional[str] = Field(alias="minAndroidSecurityPatchLevel", default=None,)
	osMaximumVersion: Optional[str] = Field(alias="osMaximumVersion", default=None,)
	osMinimumVersion: Optional[str] = Field(alias="osMinimumVersion", default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays", default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength", default=None,)
	passwordMinimumLetterCharacters: Optional[int] = Field(alias="passwordMinimumLetterCharacters", default=None,)
	passwordMinimumLowerCaseCharacters: Optional[int] = Field(alias="passwordMinimumLowerCaseCharacters", default=None,)
	passwordMinimumNonLetterCharacters: Optional[int] = Field(alias="passwordMinimumNonLetterCharacters", default=None,)
	passwordMinimumNumericCharacters: Optional[int] = Field(alias="passwordMinimumNumericCharacters", default=None,)
	passwordMinimumSymbolCharacters: Optional[int] = Field(alias="passwordMinimumSymbolCharacters", default=None,)
	passwordMinimumUpperCaseCharacters: Optional[int] = Field(alias="passwordMinimumUpperCaseCharacters", default=None,)
	passwordMinutesOfInactivityBeforeLock: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeLock", default=None,)
	passwordPreviousPasswordCountToBlock: Optional[int] = Field(alias="passwordPreviousPasswordCountToBlock", default=None,)
	passwordRequired: Optional[bool] = Field(alias="passwordRequired", default=None,)
	passwordRequiredType: Optional[AndroidDeviceOwnerRequiredPasswordType | str] = Field(alias="passwordRequiredType", default=None,)
	requireNoPendingSystemUpdates: Optional[bool] = Field(alias="requireNoPendingSystemUpdates", default=None,)
	securityRequiredAndroidSafetyNetEvaluationType: Optional[AndroidSafetyNetEvaluationType | str] = Field(alias="securityRequiredAndroidSafetyNetEvaluationType", default=None,)
	securityRequireIntuneAppIntegrity: Optional[bool] = Field(alias="securityRequireIntuneAppIntegrity", default=None,)
	securityRequireSafetyNetAttestationBasicIntegrity: Optional[bool] = Field(alias="securityRequireSafetyNetAttestationBasicIntegrity", default=None,)
	securityRequireSafetyNetAttestationCertifiedDevice: Optional[bool] = Field(alias="securityRequireSafetyNetAttestationCertifiedDevice", default=None,)
	storageRequireEncryption: Optional[bool] = Field(alias="storageRequireEncryption", default=None,)

from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_compliance_device_status import DeviceComplianceDeviceStatus
from .device_compliance_device_overview import DeviceComplianceDeviceOverview
from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
from .device_compliance_user_status import DeviceComplianceUserStatus
from .device_compliance_user_overview import DeviceComplianceUserOverview
from .device_threat_protection_level import DeviceThreatProtectionLevel
from .device_threat_protection_level import DeviceThreatProtectionLevel
from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
from .android_safety_net_evaluation_type import AndroidSafetyNetEvaluationType

