from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsManagedDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsManagedDevice"] = Field(alias="@odata.type", default="#microsoft.graph.windowsManagedDevice")
	aadRegistered: Optional[bool] = Field(alias="aadRegistered", default=None,)
	activationLockBypassCode: Optional[str] = Field(alias="activationLockBypassCode", default=None,)
	androidSecurityPatchLevel: Optional[str] = Field(alias="androidSecurityPatchLevel", default=None,)
	autopilotEnrolled: Optional[bool] = Field(alias="autopilotEnrolled", default=None,)
	azureActiveDirectoryDeviceId: Optional[str] = Field(alias="azureActiveDirectoryDeviceId", default=None,)
	azureADDeviceId: Optional[str] = Field(alias="azureADDeviceId", default=None,)
	azureADRegistered: Optional[bool] = Field(alias="azureADRegistered", default=None,)
	bootstrapTokenEscrowed: Optional[bool] = Field(alias="bootstrapTokenEscrowed", default=None,)
	chassisType: Optional[ChassisType | str] = Field(alias="chassisType", default=None,)
	chromeOSDeviceInfo: Optional[list[ChromeOSDeviceProperty]] = Field(alias="chromeOSDeviceInfo", default=None,)
	cloudPcRemoteActionResults: Optional[list[CloudPcRemoteActionResult]] = Field(alias="cloudPcRemoteActionResults", default=None,)
	complianceGracePeriodExpirationDateTime: Optional[datetime] = Field(alias="complianceGracePeriodExpirationDateTime", default=None,)
	complianceState: Optional[ComplianceState | str] = Field(alias="complianceState", default=None,)
	configurationManagerClientEnabledFeatures: Optional[ConfigurationManagerClientEnabledFeatures] = Field(alias="configurationManagerClientEnabledFeatures", default=None,)
	configurationManagerClientHealthState: Optional[ConfigurationManagerClientHealthState] = Field(alias="configurationManagerClientHealthState", default=None,)
	configurationManagerClientInformation: Optional[ConfigurationManagerClientInformation] = Field(alias="configurationManagerClientInformation", default=None,)
	deviceActionResults: Optional[list[Annotated[Union[ActivateDeviceEsimActionResult, ChangeAssignmentsActionResult, ConfigurationManagerActionResult, DeleteUserFromSharedAppleDeviceActionResult, LocateDeviceActionResult, RemoteLockActionResult, ResetPasscodeActionResult, RevokeAppleVppLicensesActionResult, RotateBitLockerKeysDeviceActionResult, WindowsDefenderScanActionResult]],Field(discriminator="odata_type")]]] = Field(alias="deviceActionResults", default=None,)
	deviceCategoryDisplayName: Optional[str] = Field(alias="deviceCategoryDisplayName", default=None,)
	deviceEnrollmentType: Optional[DeviceEnrollmentType | str] = Field(alias="deviceEnrollmentType", default=None,)
	deviceFirmwareConfigurationInterfaceManaged: Optional[bool] = Field(alias="deviceFirmwareConfigurationInterfaceManaged", default=None,)
	deviceHealthAttestationState: Optional[DeviceHealthAttestationState] = Field(alias="deviceHealthAttestationState", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	deviceRegistrationState: Optional[DeviceRegistrationState | str] = Field(alias="deviceRegistrationState", default=None,)
	deviceType: Optional[DeviceType | str] = Field(alias="deviceType", default=None,)
	easActivated: Optional[bool] = Field(alias="easActivated", default=None,)
	easActivationDateTime: Optional[datetime] = Field(alias="easActivationDateTime", default=None,)
	easDeviceId: Optional[str] = Field(alias="easDeviceId", default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress", default=None,)
	enrolledByUserPrincipalName: Optional[str] = Field(alias="enrolledByUserPrincipalName", default=None,)
	enrolledDateTime: Optional[datetime] = Field(alias="enrolledDateTime", default=None,)
	enrollmentProfileName: Optional[str] = Field(alias="enrollmentProfileName", default=None,)
	ethernetMacAddress: Optional[str] = Field(alias="ethernetMacAddress", default=None,)
	exchangeAccessState: Optional[DeviceManagementExchangeAccessState | str] = Field(alias="exchangeAccessState", default=None,)
	exchangeAccessStateReason: Optional[DeviceManagementExchangeAccessStateReason | str] = Field(alias="exchangeAccessStateReason", default=None,)
	exchangeLastSuccessfulSyncDateTime: Optional[datetime] = Field(alias="exchangeLastSuccessfulSyncDateTime", default=None,)
	freeStorageSpaceInBytes: Optional[int] = Field(alias="freeStorageSpaceInBytes", default=None,)
	hardwareInformation: Optional[HardwareInformation] = Field(alias="hardwareInformation", default=None,)
	iccid: Optional[str] = Field(alias="iccid", default=None,)
	imei: Optional[str] = Field(alias="imei", default=None,)
	isEncrypted: Optional[bool] = Field(alias="isEncrypted", default=None,)
	isSupervised: Optional[bool] = Field(alias="isSupervised", default=None,)
	jailBroken: Optional[str] = Field(alias="jailBroken", default=None,)
	joinType: Optional[JoinType | str] = Field(alias="joinType", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	lostModeState: Optional[LostModeState | str] = Field(alias="lostModeState", default=None,)
	managedDeviceName: Optional[str] = Field(alias="managedDeviceName", default=None,)
	managedDeviceOwnerType: Optional[ManagedDeviceOwnerType | str] = Field(alias="managedDeviceOwnerType", default=None,)
	managementAgent: Optional[ManagementAgentType | str] = Field(alias="managementAgent", default=None,)
	managementCertificateExpirationDate: Optional[datetime] = Field(alias="managementCertificateExpirationDate", default=None,)
	managementFeatures: Optional[ManagedDeviceManagementFeatures | str] = Field(alias="managementFeatures", default=None,)
	managementState: Optional[ManagementState | str] = Field(alias="managementState", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	meid: Optional[str] = Field(alias="meid", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	notes: Optional[str] = Field(alias="notes", default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	ownerType: Optional[OwnerType | str] = Field(alias="ownerType", default=None,)
	partnerReportedThreatState: Optional[ManagedDevicePartnerReportedHealthState | str] = Field(alias="partnerReportedThreatState", default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber", default=None,)
	physicalMemoryInBytes: Optional[int] = Field(alias="physicalMemoryInBytes", default=None,)
	preferMdmOverGroupPolicyAppliedDateTime: Optional[datetime] = Field(alias="preferMdmOverGroupPolicyAppliedDateTime", default=None,)
	processorArchitecture: Optional[ManagedDeviceArchitecture | str] = Field(alias="processorArchitecture", default=None,)
	remoteAssistanceSessionErrorDetails: Optional[str] = Field(alias="remoteAssistanceSessionErrorDetails", default=None,)
	remoteAssistanceSessionUrl: Optional[str] = Field(alias="remoteAssistanceSessionUrl", default=None,)
	requireUserEnrollmentApproval: Optional[bool] = Field(alias="requireUserEnrollmentApproval", default=None,)
	retireAfterDateTime: Optional[datetime] = Field(alias="retireAfterDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	securityPatchLevel: Optional[str] = Field(alias="securityPatchLevel", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	skuFamily: Optional[str] = Field(alias="skuFamily", default=None,)
	skuNumber: Optional[int] = Field(alias="skuNumber", default=None,)
	specificationVersion: Optional[str] = Field(alias="specificationVersion", default=None,)
	subscriberCarrier: Optional[str] = Field(alias="subscriberCarrier", default=None,)
	totalStorageSpaceInBytes: Optional[int] = Field(alias="totalStorageSpaceInBytes", default=None,)
	udid: Optional[str] = Field(alias="udid", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	usersLoggedOn: Optional[list[LoggedOnUser]] = Field(alias="usersLoggedOn", default=None,)
	wiFiMacAddress: Optional[str] = Field(alias="wiFiMacAddress", default=None,)
	windowsActiveMalwareCount: Optional[int] = Field(alias="windowsActiveMalwareCount", default=None,)
	windowsRemediatedMalwareCount: Optional[int] = Field(alias="windowsRemediatedMalwareCount", default=None,)
	assignmentFilterEvaluationStatusDetails: Optional[list[AssignmentFilterEvaluationStatusDetails]] = Field(alias="assignmentFilterEvaluationStatusDetails", default=None,)
	detectedApps: Optional[list[DetectedApp]] = Field(alias="detectedApps", default=None,)
	deviceCategory: Optional[DeviceCategory] = Field(alias="deviceCategory", default=None,)
	deviceCompliancePolicyStates: Optional[list[DeviceCompliancePolicyState]] = Field(alias="deviceCompliancePolicyStates", default=None,)
	deviceConfigurationStates: Optional[list[DeviceConfigurationState]] = Field(alias="deviceConfigurationStates", default=None,)
	deviceHealthScriptStates: Optional[list[DeviceHealthScriptPolicyState]] = Field(alias="deviceHealthScriptStates", default=None,)
	logCollectionRequests: Optional[list[DeviceLogCollectionResponse]] = Field(alias="logCollectionRequests", default=None,)
	managedDeviceMobileAppConfigurationStates: Optional[list[ManagedDeviceMobileAppConfigurationState]] = Field(alias="managedDeviceMobileAppConfigurationStates", default=None,)
	securityBaselineStates: Optional[list[SecurityBaselineState]] = Field(alias="securityBaselineStates", default=None,)
	users: Optional[list[User]] = Field(alias="users", default=None,)
	windowsProtectionState: Optional[WindowsProtectionState] = Field(alias="windowsProtectionState", default=None,)

from .chassis_type import ChassisType
from .chrome_o_s_device_property import ChromeOSDeviceProperty
from .cloud_pc_remote_action_result import CloudPcRemoteActionResult
from .compliance_state import ComplianceState
from .configuration_manager_client_enabled_features import ConfigurationManagerClientEnabledFeatures
from .configuration_manager_client_health_state import ConfigurationManagerClientHealthState
from .configuration_manager_client_information import ConfigurationManagerClientInformation
from .activate_device_esim_action_result import ActivateDeviceEsimActionResult
from .change_assignments_action_result import ChangeAssignmentsActionResult
from .configuration_manager_action_result import ConfigurationManagerActionResult
from .delete_user_from_shared_apple_device_action_result import DeleteUserFromSharedAppleDeviceActionResult
from .locate_device_action_result import LocateDeviceActionResult
from .remote_lock_action_result import RemoteLockActionResult
from .reset_passcode_action_result import ResetPasscodeActionResult
from .revoke_apple_vpp_licenses_action_result import RevokeAppleVppLicensesActionResult
from .rotate_bit_locker_keys_device_action_result import RotateBitLockerKeysDeviceActionResult
from .windows_defender_scan_action_result import WindowsDefenderScanActionResult
from .device_enrollment_type import DeviceEnrollmentType
from .device_health_attestation_state import DeviceHealthAttestationState
from .device_registration_state import DeviceRegistrationState
from .device_type import DeviceType
from .device_management_exchange_access_state import DeviceManagementExchangeAccessState
from .device_management_exchange_access_state_reason import DeviceManagementExchangeAccessStateReason
from .hardware_information import HardwareInformation
from .join_type import JoinType
from .lost_mode_state import LostModeState
from .managed_device_owner_type import ManagedDeviceOwnerType
from .management_agent_type import ManagementAgentType
from .managed_device_management_features import ManagedDeviceManagementFeatures
from .management_state import ManagementState
from .owner_type import OwnerType
from .managed_device_partner_reported_health_state import ManagedDevicePartnerReportedHealthState
from .managed_device_architecture import ManagedDeviceArchitecture
from .logged_on_user import LoggedOnUser
from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetails
from .detected_app import DetectedApp
from .device_category import DeviceCategory
from .device_compliance_policy_state import DeviceCompliancePolicyState
from .device_configuration_state import DeviceConfigurationState
from .device_health_script_policy_state import DeviceHealthScriptPolicyState
from .device_log_collection_response import DeviceLogCollectionResponse
from .managed_device_mobile_app_configuration_state import ManagedDeviceMobileAppConfigurationState
from .security_baseline_state import SecurityBaselineState
from .user import User
from .windows_protection_state import WindowsProtectionState

