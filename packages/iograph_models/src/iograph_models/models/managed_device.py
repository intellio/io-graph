from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedDevice(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activationLockBypassCode: Optional[str] = Field(alias="activationLockBypassCode",default=None,)
	androidSecurityPatchLevel: Optional[str] = Field(alias="androidSecurityPatchLevel",default=None,)
	azureADDeviceId: Optional[str] = Field(alias="azureADDeviceId",default=None,)
	azureADRegistered: Optional[bool] = Field(alias="azureADRegistered",default=None,)
	complianceGracePeriodExpirationDateTime: Optional[datetime] = Field(alias="complianceGracePeriodExpirationDateTime",default=None,)
	complianceState: Optional[str | ComplianceState] = Field(alias="complianceState",default=None,)
	configurationManagerClientEnabledFeatures: Optional[ConfigurationManagerClientEnabledFeatures] = Field(alias="configurationManagerClientEnabledFeatures",default=None,)
	deviceActionResults: SerializeAsAny[Optional[list[DeviceActionResult]]] = Field(alias="deviceActionResults",default=None,)
	deviceCategoryDisplayName: Optional[str] = Field(alias="deviceCategoryDisplayName",default=None,)
	deviceEnrollmentType: Optional[str | DeviceEnrollmentType] = Field(alias="deviceEnrollmentType",default=None,)
	deviceHealthAttestationState: Optional[DeviceHealthAttestationState] = Field(alias="deviceHealthAttestationState",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	deviceRegistrationState: Optional[str | DeviceRegistrationState] = Field(alias="deviceRegistrationState",default=None,)
	easActivated: Optional[bool] = Field(alias="easActivated",default=None,)
	easActivationDateTime: Optional[datetime] = Field(alias="easActivationDateTime",default=None,)
	easDeviceId: Optional[str] = Field(alias="easDeviceId",default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress",default=None,)
	enrolledDateTime: Optional[datetime] = Field(alias="enrolledDateTime",default=None,)
	enrollmentProfileName: Optional[str] = Field(alias="enrollmentProfileName",default=None,)
	ethernetMacAddress: Optional[str] = Field(alias="ethernetMacAddress",default=None,)
	exchangeAccessState: Optional[str | DeviceManagementExchangeAccessState] = Field(alias="exchangeAccessState",default=None,)
	exchangeAccessStateReason: Optional[str | DeviceManagementExchangeAccessStateReason] = Field(alias="exchangeAccessStateReason",default=None,)
	exchangeLastSuccessfulSyncDateTime: Optional[datetime] = Field(alias="exchangeLastSuccessfulSyncDateTime",default=None,)
	freeStorageSpaceInBytes: Optional[int] = Field(alias="freeStorageSpaceInBytes",default=None,)
	iccid: Optional[str] = Field(alias="iccid",default=None,)
	imei: Optional[str] = Field(alias="imei",default=None,)
	isEncrypted: Optional[bool] = Field(alias="isEncrypted",default=None,)
	isSupervised: Optional[bool] = Field(alias="isSupervised",default=None,)
	jailBroken: Optional[str] = Field(alias="jailBroken",default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime",default=None,)
	managedDeviceName: Optional[str] = Field(alias="managedDeviceName",default=None,)
	managedDeviceOwnerType: Optional[str | ManagedDeviceOwnerType] = Field(alias="managedDeviceOwnerType",default=None,)
	managementAgent: Optional[str | ManagementAgentType] = Field(alias="managementAgent",default=None,)
	managementCertificateExpirationDate: Optional[datetime] = Field(alias="managementCertificateExpirationDate",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	meid: Optional[str] = Field(alias="meid",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)
	notes: Optional[str] = Field(alias="notes",default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem",default=None,)
	osVersion: Optional[str] = Field(alias="osVersion",default=None,)
	partnerReportedThreatState: Optional[str | ManagedDevicePartnerReportedHealthState] = Field(alias="partnerReportedThreatState",default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber",default=None,)
	physicalMemoryInBytes: Optional[int] = Field(alias="physicalMemoryInBytes",default=None,)
	remoteAssistanceSessionErrorDetails: Optional[str] = Field(alias="remoteAssistanceSessionErrorDetails",default=None,)
	remoteAssistanceSessionUrl: Optional[str] = Field(alias="remoteAssistanceSessionUrl",default=None,)
	requireUserEnrollmentApproval: Optional[bool] = Field(alias="requireUserEnrollmentApproval",default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber",default=None,)
	subscriberCarrier: Optional[str] = Field(alias="subscriberCarrier",default=None,)
	totalStorageSpaceInBytes: Optional[int] = Field(alias="totalStorageSpaceInBytes",default=None,)
	udid: Optional[str] = Field(alias="udid",default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	wiFiMacAddress: Optional[str] = Field(alias="wiFiMacAddress",default=None,)
	deviceCategory: Optional[DeviceCategory] = Field(alias="deviceCategory",default=None,)
	deviceCompliancePolicyStates: Optional[list[DeviceCompliancePolicyState]] = Field(alias="deviceCompliancePolicyStates",default=None,)
	deviceConfigurationStates: Optional[list[DeviceConfigurationState]] = Field(alias="deviceConfigurationStates",default=None,)
	logCollectionRequests: Optional[list[DeviceLogCollectionResponse]] = Field(alias="logCollectionRequests",default=None,)
	users: Optional[list[User]] = Field(alias="users",default=None,)
	windowsProtectionState: Optional[WindowsProtectionState] = Field(alias="windowsProtectionState",default=None,)

from .compliance_state import ComplianceState
from .configuration_manager_client_enabled_features import ConfigurationManagerClientEnabledFeatures
from .device_action_result import DeviceActionResult
from .device_enrollment_type import DeviceEnrollmentType
from .device_health_attestation_state import DeviceHealthAttestationState
from .device_registration_state import DeviceRegistrationState
from .device_management_exchange_access_state import DeviceManagementExchangeAccessState
from .device_management_exchange_access_state_reason import DeviceManagementExchangeAccessStateReason
from .managed_device_owner_type import ManagedDeviceOwnerType
from .management_agent_type import ManagementAgentType
from .managed_device_partner_reported_health_state import ManagedDevicePartnerReportedHealthState
from .device_category import DeviceCategory
from .device_compliance_policy_state import DeviceCompliancePolicyState
from .device_configuration_state import DeviceConfigurationState
from .device_log_collection_response import DeviceLogCollectionResponse
from .user import User
from .windows_protection_state import WindowsProtectionState

