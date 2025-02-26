# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .windows_protection_state import WindowsProtectionStateRequest
	from .users import UsersRequest
	from .wipe import WipeRequest
	from .windows_defender_update_signatures import WindowsDefenderUpdateSignaturesRequest
	from .windows_defender_scan import WindowsDefenderScanRequest
	from .update_windows_device_account import UpdateWindowsDeviceAccountRequest
	from .sync_device import SyncDeviceRequest
	from .shut_down import ShutDownRequest
	from .retire import RetireRequest
	from .reset_passcode import ResetPasscodeRequest
	from .request_remote_assistance import RequestRemoteAssistanceRequest
	from .remote_lock import RemoteLockRequest
	from .recover_passcode import RecoverPasscodeRequest
	from .reboot_now import RebootNowRequest
	from .logout_shared_apple_device_active_user import LogoutSharedAppleDeviceActiveUserRequest
	from .locate_device import LocateDeviceRequest
	from .disable_lost_mode import DisableLostModeRequest
	from .delete_user_from_shared_apple_device import DeleteUserFromSharedAppleDeviceRequest
	from .clean_windows_device import CleanWindowsDeviceRequest
	from .bypass_activation_lock import BypassActivationLockRequest
	from .log_collection_requests import LogCollectionRequestsRequest
	from .device_configuration_states import DeviceConfigurationStatesRequest
	from .device_compliance_policy_states import DeviceCompliancePolicyStatesRequest
	from .device_category import DeviceCategoryRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.managed_device import ManagedDevice


class ByManagedDeviceIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/managedDevices/{managedDevice%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedDevice:
		"""
		Get managedDevices from deviceManagement
		The list of managed devices.
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
		Update the navigation property managedDevices in deviceManagement
		
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
		Delete managedDevice
		Deletes a managedDevice.
		Find more info here: https://learn.microsoft.com/graph/api/intune-devices-manageddevice-delete?view=graph-rest-1.0
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



	@property
	def device_category(self,
	) -> DeviceCategoryRequest:
		from .device_category import DeviceCategoryRequest
		return DeviceCategoryRequest(self.request_adapter, self.path_parameters)

	@property
	def device_compliance_policy_states(self,
	) -> DeviceCompliancePolicyStatesRequest:
		from .device_compliance_policy_states import DeviceCompliancePolicyStatesRequest
		return DeviceCompliancePolicyStatesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_configuration_states(self,
	) -> DeviceConfigurationStatesRequest:
		from .device_configuration_states import DeviceConfigurationStatesRequest
		return DeviceConfigurationStatesRequest(self.request_adapter, self.path_parameters)

	@property
	def log_collection_requests(self,
	) -> LogCollectionRequestsRequest:
		from .log_collection_requests import LogCollectionRequestsRequest
		return LogCollectionRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def bypass_activation_lock(self,
	) -> BypassActivationLockRequest:
		from .bypass_activation_lock import BypassActivationLockRequest
		return BypassActivationLockRequest(self.request_adapter, self.path_parameters)

	@property
	def clean_windows_device(self,
	) -> CleanWindowsDeviceRequest:
		from .clean_windows_device import CleanWindowsDeviceRequest
		return CleanWindowsDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def delete_user_from_shared_apple_device(self,
	) -> DeleteUserFromSharedAppleDeviceRequest:
		from .delete_user_from_shared_apple_device import DeleteUserFromSharedAppleDeviceRequest
		return DeleteUserFromSharedAppleDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def disable_lost_mode(self,
	) -> DisableLostModeRequest:
		from .disable_lost_mode import DisableLostModeRequest
		return DisableLostModeRequest(self.request_adapter, self.path_parameters)

	@property
	def locate_device(self,
	) -> LocateDeviceRequest:
		from .locate_device import LocateDeviceRequest
		return LocateDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def logout_shared_apple_device_active_user(self,
	) -> LogoutSharedAppleDeviceActiveUserRequest:
		from .logout_shared_apple_device_active_user import LogoutSharedAppleDeviceActiveUserRequest
		return LogoutSharedAppleDeviceActiveUserRequest(self.request_adapter, self.path_parameters)

	@property
	def reboot_now(self,
	) -> RebootNowRequest:
		from .reboot_now import RebootNowRequest
		return RebootNowRequest(self.request_adapter, self.path_parameters)

	@property
	def recover_passcode(self,
	) -> RecoverPasscodeRequest:
		from .recover_passcode import RecoverPasscodeRequest
		return RecoverPasscodeRequest(self.request_adapter, self.path_parameters)

	@property
	def remote_lock(self,
	) -> RemoteLockRequest:
		from .remote_lock import RemoteLockRequest
		return RemoteLockRequest(self.request_adapter, self.path_parameters)

	@property
	def request_remote_assistance(self,
	) -> RequestRemoteAssistanceRequest:
		from .request_remote_assistance import RequestRemoteAssistanceRequest
		return RequestRemoteAssistanceRequest(self.request_adapter, self.path_parameters)

	@property
	def reset_passcode(self,
	) -> ResetPasscodeRequest:
		from .reset_passcode import ResetPasscodeRequest
		return ResetPasscodeRequest(self.request_adapter, self.path_parameters)

	@property
	def retire(self,
	) -> RetireRequest:
		from .retire import RetireRequest
		return RetireRequest(self.request_adapter, self.path_parameters)

	@property
	def shut_down(self,
	) -> ShutDownRequest:
		from .shut_down import ShutDownRequest
		return ShutDownRequest(self.request_adapter, self.path_parameters)

	@property
	def sync_device(self,
	) -> SyncDeviceRequest:
		from .sync_device import SyncDeviceRequest
		return SyncDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def update_windows_device_account(self,
	) -> UpdateWindowsDeviceAccountRequest:
		from .update_windows_device_account import UpdateWindowsDeviceAccountRequest
		return UpdateWindowsDeviceAccountRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_defender_scan(self,
	) -> WindowsDefenderScanRequest:
		from .windows_defender_scan import WindowsDefenderScanRequest
		return WindowsDefenderScanRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_defender_update_signatures(self,
	) -> WindowsDefenderUpdateSignaturesRequest:
		from .windows_defender_update_signatures import WindowsDefenderUpdateSignaturesRequest
		return WindowsDefenderUpdateSignaturesRequest(self.request_adapter, self.path_parameters)

	@property
	def wipe(self,
	) -> WipeRequest:
		from .wipe import WipeRequest
		return WipeRequest(self.request_adapter, self.path_parameters)

	@property
	def users(self,
	) -> UsersRequest:
		from .users import UsersRequest
		return UsersRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_protection_state(self,
	) -> WindowsProtectionStateRequest:
		from .windows_protection_state import WindowsProtectionStateRequest
		return WindowsProtectionStateRequest(self.request_adapter, self.path_parameters)

