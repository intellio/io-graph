# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
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
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.managed_device import ManagedDevice


class ByManagedDeviceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/managedDevices/{managedDevice%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedDevice:
		"""
		Get managedDevices from users
		The managed devices associated with the user.
		"""
		tags = ['users.managedDevice']

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
		Update the navigation property managedDevices in users
		
		"""
		tags = ['users.managedDevice']

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
		Delete navigation property managedDevices for users
		
		"""
		tags = ['users.managedDevice']
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

	def device_category(self,
		user_id: str,
		managedDevice_id: str,
	) -> DeviceCategoryRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .device_category import DeviceCategoryRequest
		return DeviceCategoryRequest(self.request_adapter, path_parameters)

	def device_compliance_policy_states(self,
		user_id: str,
		managedDevice_id: str,
	) -> DeviceCompliancePolicyStatesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .device_compliance_policy_states import DeviceCompliancePolicyStatesRequest
		return DeviceCompliancePolicyStatesRequest(self.request_adapter, path_parameters)

	def device_configuration_states(self,
		user_id: str,
		managedDevice_id: str,
	) -> DeviceConfigurationStatesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .device_configuration_states import DeviceConfigurationStatesRequest
		return DeviceConfigurationStatesRequest(self.request_adapter, path_parameters)

	def log_collection_requests(self,
		user_id: str,
		managedDevice_id: str,
	) -> LogCollectionRequestsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .log_collection_requests import LogCollectionRequestsRequest
		return LogCollectionRequestsRequest(self.request_adapter, path_parameters)

	def bypass_activation_lock(self,
		user_id: str,
		managedDevice_id: str,
	) -> BypassActivationLockRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .bypass_activation_lock import BypassActivationLockRequest
		return BypassActivationLockRequest(self.request_adapter, path_parameters)

	def clean_windows_device(self,
		user_id: str,
		managedDevice_id: str,
	) -> CleanWindowsDeviceRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .clean_windows_device import CleanWindowsDeviceRequest
		return CleanWindowsDeviceRequest(self.request_adapter, path_parameters)

	def delete_user_from_shared_apple_device(self,
		user_id: str,
		managedDevice_id: str,
	) -> DeleteUserFromSharedAppleDeviceRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .delete_user_from_shared_apple_device import DeleteUserFromSharedAppleDeviceRequest
		return DeleteUserFromSharedAppleDeviceRequest(self.request_adapter, path_parameters)

	def disable_lost_mode(self,
		user_id: str,
		managedDevice_id: str,
	) -> DisableLostModeRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .disable_lost_mode import DisableLostModeRequest
		return DisableLostModeRequest(self.request_adapter, path_parameters)

	def locate_device(self,
		user_id: str,
		managedDevice_id: str,
	) -> LocateDeviceRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .locate_device import LocateDeviceRequest
		return LocateDeviceRequest(self.request_adapter, path_parameters)

	def logout_shared_apple_device_active_user(self,
		user_id: str,
		managedDevice_id: str,
	) -> LogoutSharedAppleDeviceActiveUserRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .logout_shared_apple_device_active_user import LogoutSharedAppleDeviceActiveUserRequest
		return LogoutSharedAppleDeviceActiveUserRequest(self.request_adapter, path_parameters)

	def reboot_now(self,
		user_id: str,
		managedDevice_id: str,
	) -> RebootNowRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .reboot_now import RebootNowRequest
		return RebootNowRequest(self.request_adapter, path_parameters)

	def recover_passcode(self,
		user_id: str,
		managedDevice_id: str,
	) -> RecoverPasscodeRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .recover_passcode import RecoverPasscodeRequest
		return RecoverPasscodeRequest(self.request_adapter, path_parameters)

	def remote_lock(self,
		user_id: str,
		managedDevice_id: str,
	) -> RemoteLockRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .remote_lock import RemoteLockRequest
		return RemoteLockRequest(self.request_adapter, path_parameters)

	def request_remote_assistance(self,
		user_id: str,
		managedDevice_id: str,
	) -> RequestRemoteAssistanceRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .request_remote_assistance import RequestRemoteAssistanceRequest
		return RequestRemoteAssistanceRequest(self.request_adapter, path_parameters)

	def reset_passcode(self,
		user_id: str,
		managedDevice_id: str,
	) -> ResetPasscodeRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .reset_passcode import ResetPasscodeRequest
		return ResetPasscodeRequest(self.request_adapter, path_parameters)

	def retire(self,
		user_id: str,
		managedDevice_id: str,
	) -> RetireRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .retire import RetireRequest
		return RetireRequest(self.request_adapter, path_parameters)

	def shut_down(self,
		user_id: str,
		managedDevice_id: str,
	) -> ShutDownRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .shut_down import ShutDownRequest
		return ShutDownRequest(self.request_adapter, path_parameters)

	def sync_device(self,
		user_id: str,
		managedDevice_id: str,
	) -> SyncDeviceRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .sync_device import SyncDeviceRequest
		return SyncDeviceRequest(self.request_adapter, path_parameters)

	def update_windows_device_account(self,
		user_id: str,
		managedDevice_id: str,
	) -> UpdateWindowsDeviceAccountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .update_windows_device_account import UpdateWindowsDeviceAccountRequest
		return UpdateWindowsDeviceAccountRequest(self.request_adapter, path_parameters)

	def windows_defender_scan(self,
		user_id: str,
		managedDevice_id: str,
	) -> WindowsDefenderScanRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .windows_defender_scan import WindowsDefenderScanRequest
		return WindowsDefenderScanRequest(self.request_adapter, path_parameters)

	def windows_defender_update_signatures(self,
		user_id: str,
		managedDevice_id: str,
	) -> WindowsDefenderUpdateSignaturesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .windows_defender_update_signatures import WindowsDefenderUpdateSignaturesRequest
		return WindowsDefenderUpdateSignaturesRequest(self.request_adapter, path_parameters)

	def wipe(self,
		user_id: str,
		managedDevice_id: str,
	) -> WipeRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .wipe import WipeRequest
		return WipeRequest(self.request_adapter, path_parameters)

	def users(self,
		user_id: str,
		managedDevice_id: str,
	) -> UsersRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .users import UsersRequest
		return UsersRequest(self.request_adapter, path_parameters)

	def windows_protection_state(self,
		user_id: str,
		managedDevice_id: str,
	) -> WindowsProtectionStateRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .windows_protection_state import WindowsProtectionStateRequest
		return WindowsProtectionStateRequest(self.request_adapter, path_parameters)

