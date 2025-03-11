# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .windows_protection_state import WindowsProtectionStateRequest
	from .users import UsersRequest
	from .security_baseline_states import SecurityBaselineStatesRequest
	from .wipe import WipeRequest
	from .windows_defender_update_signatures import WindowsDefenderUpdateSignaturesRequest
	from .windows_defender_scan import WindowsDefenderScanRequest
	from .update_windows_device_account import UpdateWindowsDeviceAccountRequest
	from .trigger_configuration_manager_action import TriggerConfigurationManagerActionRequest
	from .sync_device import SyncDeviceRequest
	from .shut_down import ShutDownRequest
	from .set_device_name import SetDeviceNameRequest
	from .set_cloud_pc_review_status import SetCloudPcReviewStatusRequest
	from .send_custom_notification_to_company_portal import SendCustomNotificationToCompanyPortalRequest
	from .rotate_local_admin_password import RotateLocalAdminPasswordRequest
	from .rotate_file_vault_key import RotateFileVaultKeyRequest
	from .rotate_bit_locker_keys import RotateBitLockerKeysRequest
	from .revoke_apple_vpp_licenses import RevokeAppleVppLicensesRequest
	from .retire import RetireRequest
	from .reset_passcode import ResetPasscodeRequest
	from .request_remote_assistance import RequestRemoteAssistanceRequest
	from .remove_device_firmware_configuration_interface_management import RemoveDeviceFirmwareConfigurationInterfaceManagementRequest
	from .remote_lock import RemoteLockRequest
	from .reenable import ReenableRequest
	from .recover_passcode import RecoverPasscodeRequest
	from .reboot_now import RebootNowRequest
	from .play_lost_mode_sound import PlayLostModeSoundRequest
	from .pause_configuration_refresh import PauseConfigurationRefreshRequest
	from .override_compliance_state import OverrideComplianceStateRequest
	from .logout_shared_apple_device_active_user import LogoutSharedAppleDeviceActiveUserRequest
	from .locate_device import LocateDeviceRequest
	from .initiate_on_demand_proactive_remediation import InitiateOnDemandProactiveRemediationRequest
	from .initiate_mobile_device_management_key_recovery import InitiateMobileDeviceManagementKeyRecoveryRequest
	from .initiate_device_attestation import InitiateDeviceAttestationRequest
	from .get_non_compliant_settings import GetNonCompliantSettingsRequest
	from .get_file_vault_key import GetFileVaultKeyRequest
	from .get_cloud_pc_review_status import GetCloudPcReviewStatusRequest
	from .get_cloud_pc_remote_action_results import GetCloudPcRemoteActionResultsRequest
	from .enroll_now_action import EnrollNowActionRequest
	from .enable_lost_mode import EnableLostModeRequest
	from .disable_lost_mode import DisableLostModeRequest
	from .disable import DisableRequest
	from .deprovision import DeprovisionRequest
	from .delete_user_from_shared_apple_device import DeleteUserFromSharedAppleDeviceRequest
	from .create_device_log_collection_request import CreateDeviceLogCollectionRequestRequest
	from .clean_windows_device import CleanWindowsDeviceRequest
	from .change_assignments import ChangeAssignmentsRequest
	from .bypass_activation_lock import BypassActivationLockRequest
	from .activate_device_esim import ActivateDeviceEsimRequest
	from .managed_device_mobile_app_configuration_states import ManagedDeviceMobileAppConfigurationStatesRequest
	from .log_collection_requests import LogCollectionRequestsRequest
	from .device_health_script_states import DeviceHealthScriptStatesRequest
	from .device_configuration_states import DeviceConfigurationStatesRequest
	from .device_compliance_policy_states import DeviceCompliancePolicyStatesRequest
	from .device_category import DeviceCategoryRequest
	from .detected_apps import DetectedAppsRequest
	from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetailsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.managed_device import ManagedDevice


class ByManagedDeviceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/comanagedDevices/{managedDevice%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedDevice:
		"""
		Get comanagedDevices from deviceManagement
		The list of co-managed devices report
		"""
		tags = ['deviceManagement.managedDevice']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, ManagedDevice, error_mapping)

	async def patch(
		self,
		body: ManagedDevice,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedDevice:
		"""
		Update the navigation property comanagedDevices in deviceManagement
		
		"""
		tags = ['deviceManagement.managedDevice']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, ManagedDevice, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property comanagedDevices for deviceManagement
		
		"""
		tags = ['deviceManagement.managedDevice']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByManagedDeviceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByManagedDeviceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByManagedDeviceIdRequest(self.request_adapter, self.path_parameters)

	def assignment_filter_evaluation_status_details(self,
		managedDevice_id: str,
	) -> AssignmentFilterEvaluationStatusDetailsRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .assignment_filter_evaluation_status_details import AssignmentFilterEvaluationStatusDetailsRequest
		return AssignmentFilterEvaluationStatusDetailsRequest(self.request_adapter, path_parameters)

	def detected_apps(self,
		managedDevice_id: str,
	) -> DetectedAppsRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .detected_apps import DetectedAppsRequest
		return DetectedAppsRequest(self.request_adapter, path_parameters)

	def device_category(self,
		managedDevice_id: str,
	) -> DeviceCategoryRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .device_category import DeviceCategoryRequest
		return DeviceCategoryRequest(self.request_adapter, path_parameters)

	def device_compliance_policy_states(self,
		managedDevice_id: str,
	) -> DeviceCompliancePolicyStatesRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .device_compliance_policy_states import DeviceCompliancePolicyStatesRequest
		return DeviceCompliancePolicyStatesRequest(self.request_adapter, path_parameters)

	def device_configuration_states(self,
		managedDevice_id: str,
	) -> DeviceConfigurationStatesRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .device_configuration_states import DeviceConfigurationStatesRequest
		return DeviceConfigurationStatesRequest(self.request_adapter, path_parameters)

	def device_health_script_states(self,
		managedDevice_id: str,
	) -> DeviceHealthScriptStatesRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .device_health_script_states import DeviceHealthScriptStatesRequest
		return DeviceHealthScriptStatesRequest(self.request_adapter, path_parameters)

	def log_collection_requests(self,
		managedDevice_id: str,
	) -> LogCollectionRequestsRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .log_collection_requests import LogCollectionRequestsRequest
		return LogCollectionRequestsRequest(self.request_adapter, path_parameters)

	def managed_device_mobile_app_configuration_states(self,
		managedDevice_id: str,
	) -> ManagedDeviceMobileAppConfigurationStatesRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .managed_device_mobile_app_configuration_states import ManagedDeviceMobileAppConfigurationStatesRequest
		return ManagedDeviceMobileAppConfigurationStatesRequest(self.request_adapter, path_parameters)

	def activate_device_esim(self,
		managedDevice_id: str,
	) -> ActivateDeviceEsimRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .activate_device_esim import ActivateDeviceEsimRequest
		return ActivateDeviceEsimRequest(self.request_adapter, path_parameters)

	def bypass_activation_lock(self,
		managedDevice_id: str,
	) -> BypassActivationLockRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .bypass_activation_lock import BypassActivationLockRequest
		return BypassActivationLockRequest(self.request_adapter, path_parameters)

	def change_assignments(self,
		managedDevice_id: str,
	) -> ChangeAssignmentsRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .change_assignments import ChangeAssignmentsRequest
		return ChangeAssignmentsRequest(self.request_adapter, path_parameters)

	def clean_windows_device(self,
		managedDevice_id: str,
	) -> CleanWindowsDeviceRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .clean_windows_device import CleanWindowsDeviceRequest
		return CleanWindowsDeviceRequest(self.request_adapter, path_parameters)

	def create_device_log_collection_request(self,
		managedDevice_id: str,
	) -> CreateDeviceLogCollectionRequestRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .create_device_log_collection_request import CreateDeviceLogCollectionRequestRequest
		return CreateDeviceLogCollectionRequestRequest(self.request_adapter, path_parameters)

	def delete_user_from_shared_apple_device(self,
		managedDevice_id: str,
	) -> DeleteUserFromSharedAppleDeviceRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .delete_user_from_shared_apple_device import DeleteUserFromSharedAppleDeviceRequest
		return DeleteUserFromSharedAppleDeviceRequest(self.request_adapter, path_parameters)

	def deprovision(self,
		managedDevice_id: str,
	) -> DeprovisionRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .deprovision import DeprovisionRequest
		return DeprovisionRequest(self.request_adapter, path_parameters)

	def disable(self,
		managedDevice_id: str,
	) -> DisableRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .disable import DisableRequest
		return DisableRequest(self.request_adapter, path_parameters)

	def disable_lost_mode(self,
		managedDevice_id: str,
	) -> DisableLostModeRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .disable_lost_mode import DisableLostModeRequest
		return DisableLostModeRequest(self.request_adapter, path_parameters)

	def enable_lost_mode(self,
		managedDevice_id: str,
	) -> EnableLostModeRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .enable_lost_mode import EnableLostModeRequest
		return EnableLostModeRequest(self.request_adapter, path_parameters)

	def enroll_now_action(self,
		managedDevice_id: str,
	) -> EnrollNowActionRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .enroll_now_action import EnrollNowActionRequest
		return EnrollNowActionRequest(self.request_adapter, path_parameters)

	def get_cloud_pc_remote_action_results(self,
		managedDevice_id: str,
	) -> GetCloudPcRemoteActionResultsRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .get_cloud_pc_remote_action_results import GetCloudPcRemoteActionResultsRequest
		return GetCloudPcRemoteActionResultsRequest(self.request_adapter, path_parameters)

	def get_cloud_pc_review_status(self,
		managedDevice_id: str,
	) -> GetCloudPcReviewStatusRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .get_cloud_pc_review_status import GetCloudPcReviewStatusRequest
		return GetCloudPcReviewStatusRequest(self.request_adapter, path_parameters)

	def get_file_vault_key(self,
		managedDevice_id: str,
	) -> GetFileVaultKeyRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .get_file_vault_key import GetFileVaultKeyRequest
		return GetFileVaultKeyRequest(self.request_adapter, path_parameters)

	def get_non_compliant_settings(self,
		managedDevice_id: str,
	) -> GetNonCompliantSettingsRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .get_non_compliant_settings import GetNonCompliantSettingsRequest
		return GetNonCompliantSettingsRequest(self.request_adapter, path_parameters)

	def initiate_device_attestation(self,
		managedDevice_id: str,
	) -> InitiateDeviceAttestationRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .initiate_device_attestation import InitiateDeviceAttestationRequest
		return InitiateDeviceAttestationRequest(self.request_adapter, path_parameters)

	def initiate_mobile_device_management_key_recovery(self,
		managedDevice_id: str,
	) -> InitiateMobileDeviceManagementKeyRecoveryRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .initiate_mobile_device_management_key_recovery import InitiateMobileDeviceManagementKeyRecoveryRequest
		return InitiateMobileDeviceManagementKeyRecoveryRequest(self.request_adapter, path_parameters)

	def initiate_on_demand_proactive_remediation(self,
		managedDevice_id: str,
	) -> InitiateOnDemandProactiveRemediationRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .initiate_on_demand_proactive_remediation import InitiateOnDemandProactiveRemediationRequest
		return InitiateOnDemandProactiveRemediationRequest(self.request_adapter, path_parameters)

	def locate_device(self,
		managedDevice_id: str,
	) -> LocateDeviceRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .locate_device import LocateDeviceRequest
		return LocateDeviceRequest(self.request_adapter, path_parameters)

	def logout_shared_apple_device_active_user(self,
		managedDevice_id: str,
	) -> LogoutSharedAppleDeviceActiveUserRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .logout_shared_apple_device_active_user import LogoutSharedAppleDeviceActiveUserRequest
		return LogoutSharedAppleDeviceActiveUserRequest(self.request_adapter, path_parameters)

	def override_compliance_state(self,
		managedDevice_id: str,
	) -> OverrideComplianceStateRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .override_compliance_state import OverrideComplianceStateRequest
		return OverrideComplianceStateRequest(self.request_adapter, path_parameters)

	def pause_configuration_refresh(self,
		managedDevice_id: str,
	) -> PauseConfigurationRefreshRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .pause_configuration_refresh import PauseConfigurationRefreshRequest
		return PauseConfigurationRefreshRequest(self.request_adapter, path_parameters)

	def play_lost_mode_sound(self,
		managedDevice_id: str,
	) -> PlayLostModeSoundRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .play_lost_mode_sound import PlayLostModeSoundRequest
		return PlayLostModeSoundRequest(self.request_adapter, path_parameters)

	def reboot_now(self,
		managedDevice_id: str,
	) -> RebootNowRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .reboot_now import RebootNowRequest
		return RebootNowRequest(self.request_adapter, path_parameters)

	def recover_passcode(self,
		managedDevice_id: str,
	) -> RecoverPasscodeRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .recover_passcode import RecoverPasscodeRequest
		return RecoverPasscodeRequest(self.request_adapter, path_parameters)

	def reenable(self,
		managedDevice_id: str,
	) -> ReenableRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .reenable import ReenableRequest
		return ReenableRequest(self.request_adapter, path_parameters)

	def remote_lock(self,
		managedDevice_id: str,
	) -> RemoteLockRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .remote_lock import RemoteLockRequest
		return RemoteLockRequest(self.request_adapter, path_parameters)

	def remove_device_firmware_configuration_interface_management(self,
		managedDevice_id: str,
	) -> RemoveDeviceFirmwareConfigurationInterfaceManagementRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .remove_device_firmware_configuration_interface_management import RemoveDeviceFirmwareConfigurationInterfaceManagementRequest
		return RemoveDeviceFirmwareConfigurationInterfaceManagementRequest(self.request_adapter, path_parameters)

	def request_remote_assistance(self,
		managedDevice_id: str,
	) -> RequestRemoteAssistanceRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .request_remote_assistance import RequestRemoteAssistanceRequest
		return RequestRemoteAssistanceRequest(self.request_adapter, path_parameters)

	def reset_passcode(self,
		managedDevice_id: str,
	) -> ResetPasscodeRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .reset_passcode import ResetPasscodeRequest
		return ResetPasscodeRequest(self.request_adapter, path_parameters)

	def retire(self,
		managedDevice_id: str,
	) -> RetireRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .retire import RetireRequest
		return RetireRequest(self.request_adapter, path_parameters)

	def revoke_apple_vpp_licenses(self,
		managedDevice_id: str,
	) -> RevokeAppleVppLicensesRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .revoke_apple_vpp_licenses import RevokeAppleVppLicensesRequest
		return RevokeAppleVppLicensesRequest(self.request_adapter, path_parameters)

	def rotate_bit_locker_keys(self,
		managedDevice_id: str,
	) -> RotateBitLockerKeysRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .rotate_bit_locker_keys import RotateBitLockerKeysRequest
		return RotateBitLockerKeysRequest(self.request_adapter, path_parameters)

	def rotate_file_vault_key(self,
		managedDevice_id: str,
	) -> RotateFileVaultKeyRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .rotate_file_vault_key import RotateFileVaultKeyRequest
		return RotateFileVaultKeyRequest(self.request_adapter, path_parameters)

	def rotate_local_admin_password(self,
		managedDevice_id: str,
	) -> RotateLocalAdminPasswordRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .rotate_local_admin_password import RotateLocalAdminPasswordRequest
		return RotateLocalAdminPasswordRequest(self.request_adapter, path_parameters)

	def send_custom_notification_to_company_portal(self,
		managedDevice_id: str,
	) -> SendCustomNotificationToCompanyPortalRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .send_custom_notification_to_company_portal import SendCustomNotificationToCompanyPortalRequest
		return SendCustomNotificationToCompanyPortalRequest(self.request_adapter, path_parameters)

	def set_cloud_pc_review_status(self,
		managedDevice_id: str,
	) -> SetCloudPcReviewStatusRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .set_cloud_pc_review_status import SetCloudPcReviewStatusRequest
		return SetCloudPcReviewStatusRequest(self.request_adapter, path_parameters)

	def set_device_name(self,
		managedDevice_id: str,
	) -> SetDeviceNameRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .set_device_name import SetDeviceNameRequest
		return SetDeviceNameRequest(self.request_adapter, path_parameters)

	def shut_down(self,
		managedDevice_id: str,
	) -> ShutDownRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .shut_down import ShutDownRequest
		return ShutDownRequest(self.request_adapter, path_parameters)

	def sync_device(self,
		managedDevice_id: str,
	) -> SyncDeviceRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .sync_device import SyncDeviceRequest
		return SyncDeviceRequest(self.request_adapter, path_parameters)

	def trigger_configuration_manager_action(self,
		managedDevice_id: str,
	) -> TriggerConfigurationManagerActionRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .trigger_configuration_manager_action import TriggerConfigurationManagerActionRequest
		return TriggerConfigurationManagerActionRequest(self.request_adapter, path_parameters)

	def update_windows_device_account(self,
		managedDevice_id: str,
	) -> UpdateWindowsDeviceAccountRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .update_windows_device_account import UpdateWindowsDeviceAccountRequest
		return UpdateWindowsDeviceAccountRequest(self.request_adapter, path_parameters)

	def windows_defender_scan(self,
		managedDevice_id: str,
	) -> WindowsDefenderScanRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .windows_defender_scan import WindowsDefenderScanRequest
		return WindowsDefenderScanRequest(self.request_adapter, path_parameters)

	def windows_defender_update_signatures(self,
		managedDevice_id: str,
	) -> WindowsDefenderUpdateSignaturesRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .windows_defender_update_signatures import WindowsDefenderUpdateSignaturesRequest
		return WindowsDefenderUpdateSignaturesRequest(self.request_adapter, path_parameters)

	def wipe(self,
		managedDevice_id: str,
	) -> WipeRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .wipe import WipeRequest
		return WipeRequest(self.request_adapter, path_parameters)

	def security_baseline_states(self,
		managedDevice_id: str,
	) -> SecurityBaselineStatesRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .security_baseline_states import SecurityBaselineStatesRequest
		return SecurityBaselineStatesRequest(self.request_adapter, path_parameters)

	def users(self,
		managedDevice_id: str,
	) -> UsersRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .users import UsersRequest
		return UsersRequest(self.request_adapter, path_parameters)

	def windows_protection_state(self,
		managedDevice_id: str,
	) -> WindowsProtectionStateRequest:
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .windows_protection_state import WindowsProtectionStateRequest
		return WindowsProtectionStateRequest(self.request_adapter, path_parameters)

