# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .unbind import UnbindRequest
	from .sync_apps import SyncAppsRequest
	from .set_android_device_owner_fully_managed_enrollment_state import SetAndroidDeviceOwnerFullyManagedEnrollmentStateRequest
	from .request_signup_url import RequestSignupUrlRequest
	from .create_google_play_web_token import CreateGooglePlayWebTokenRequest
	from .complete_signup import CompleteSignupRequest
	from .approve_apps import ApproveAppsRequest
	from .add_apps import AddAppsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings


class AndroidManagedStoreAccountEnterpriseSettingsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/androidManagedStoreAccountEnterpriseSettings", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AndroidManagedStoreAccountEnterpriseSettings:
		"""
		Get androidManagedStoreAccountEnterpriseSettings from deviceManagement
		The singleton Android managed store account enterprise settings entity.
		"""
		tags = ['deviceManagement.androidManagedStoreAccountEnterpriseSettings']

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
		return await self.request_adapter.send_async(request_info, AndroidManagedStoreAccountEnterpriseSettings, error_mapping)

	async def patch(
		self,
		body: AndroidManagedStoreAccountEnterpriseSettings,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AndroidManagedStoreAccountEnterpriseSettings:
		"""
		Update the navigation property androidManagedStoreAccountEnterpriseSettings in deviceManagement
		
		"""
		tags = ['deviceManagement.androidManagedStoreAccountEnterpriseSettings']

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
		return await self.request_adapter.send_async(request_info, AndroidManagedStoreAccountEnterpriseSettings, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property androidManagedStoreAccountEnterpriseSettings for deviceManagement
		
		"""
		tags = ['deviceManagement.androidManagedStoreAccountEnterpriseSettings']
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



	def with_url(self, raw_url: str) -> AndroidManagedStoreAccountEnterpriseSettingsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AndroidManagedStoreAccountEnterpriseSettingsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AndroidManagedStoreAccountEnterpriseSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def add_apps(self,
	) -> AddAppsRequest:
		from .add_apps import AddAppsRequest
		return AddAppsRequest(self.request_adapter, self.path_parameters)

	@property
	def approve_apps(self,
	) -> ApproveAppsRequest:
		from .approve_apps import ApproveAppsRequest
		return ApproveAppsRequest(self.request_adapter, self.path_parameters)

	@property
	def complete_signup(self,
	) -> CompleteSignupRequest:
		from .complete_signup import CompleteSignupRequest
		return CompleteSignupRequest(self.request_adapter, self.path_parameters)

	@property
	def create_google_play_web_token(self,
	) -> CreateGooglePlayWebTokenRequest:
		from .create_google_play_web_token import CreateGooglePlayWebTokenRequest
		return CreateGooglePlayWebTokenRequest(self.request_adapter, self.path_parameters)

	@property
	def request_signup_url(self,
	) -> RequestSignupUrlRequest:
		from .request_signup_url import RequestSignupUrlRequest
		return RequestSignupUrlRequest(self.request_adapter, self.path_parameters)

	@property
	def set_android_device_owner_fully_managed_enrollment_state(self,
	) -> SetAndroidDeviceOwnerFullyManagedEnrollmentStateRequest:
		from .set_android_device_owner_fully_managed_enrollment_state import SetAndroidDeviceOwnerFullyManagedEnrollmentStateRequest
		return SetAndroidDeviceOwnerFullyManagedEnrollmentStateRequest(self.request_adapter, self.path_parameters)

	@property
	def sync_apps(self,
	) -> SyncAppsRequest:
		from .sync_apps import SyncAppsRequest
		return SyncAppsRequest(self.request_adapter, self.path_parameters)

	@property
	def unbind(self,
	) -> UnbindRequest:
		from .unbind import UnbindRequest
		return UnbindRequest(self.request_adapter, self.path_parameters)

