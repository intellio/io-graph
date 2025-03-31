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
	from .retrieve_powerlift_app_diagnostics_details_with_userprincipalname import RetrievePowerliftAppDiagnosticsDetailsWithUserPrincipalNameRequest
	from .move_devices_to_o_u import MoveDevicesToOURequest
	from .execute_action import ExecuteActionRequest
	from .download_powerlift_app_diagnostic import DownloadPowerliftAppDiagnosticRequest
	from .download_app_diagnostics import DownloadAppDiagnosticsRequest
	from .bulk_set_cloud_pc_review_status import BulkSetCloudPcReviewStatusRequest
	from .bulk_restore_cloud_pc import BulkRestoreCloudPcRequest
	from .bulk_reprovision_cloud_pc import BulkReprovisionCloudPcRequest
	from .app_diagnostics_with_upn import AppDiagnosticsWithUpnRequest
	from .count import CountRequest
	from .by_managed_device_id import ByManagedDeviceIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.managed_device_collection_response import ManagedDeviceCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.managed_device import ManagedDevice


class ManagedDevicesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/managedDevices", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ManagedDeviceCollectionResponse:
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
		return await self.request_adapter.send_async(request_info, ManagedDeviceCollectionResponse, error_mapping)

	async def post(
		self,
		body: ManagedDevice,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ManagedDevice:
		"""
		Create new navigation property to managedDevices for users
		
		"""
		tags = ['users.managedDevice']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, ManagedDevice, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ManagedDevicesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ManagedDevicesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ManagedDevicesRequest(self.request_adapter, self.path_parameters)

	def by_managed_device_id(self,
		user_id: str,
		managedDevice_id: str,
	) -> ByManagedDeviceIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id

		from .by_managed_device_id import ByManagedDeviceIdRequest
		return ByManagedDeviceIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def app_diagnostics_with_upn(self,
		user_id: str,
		upn: str,
	) -> AppDiagnosticsWithUpnRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if upn is None:
			raise TypeError("upn cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["upn"] =  upn

		from .app_diagnostics_with_upn import AppDiagnosticsWithUpnRequest
		return AppDiagnosticsWithUpnRequest(self.request_adapter, path_parameters)

	def bulk_reprovision_cloud_pc(self,
		user_id: str,
	) -> BulkReprovisionCloudPcRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .bulk_reprovision_cloud_pc import BulkReprovisionCloudPcRequest
		return BulkReprovisionCloudPcRequest(self.request_adapter, path_parameters)

	def bulk_restore_cloud_pc(self,
		user_id: str,
	) -> BulkRestoreCloudPcRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .bulk_restore_cloud_pc import BulkRestoreCloudPcRequest
		return BulkRestoreCloudPcRequest(self.request_adapter, path_parameters)

	def bulk_set_cloud_pc_review_status(self,
		user_id: str,
	) -> BulkSetCloudPcReviewStatusRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .bulk_set_cloud_pc_review_status import BulkSetCloudPcReviewStatusRequest
		return BulkSetCloudPcReviewStatusRequest(self.request_adapter, path_parameters)

	def download_app_diagnostics(self,
		user_id: str,
	) -> DownloadAppDiagnosticsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .download_app_diagnostics import DownloadAppDiagnosticsRequest
		return DownloadAppDiagnosticsRequest(self.request_adapter, path_parameters)

	def download_powerlift_app_diagnostic(self,
		user_id: str,
	) -> DownloadPowerliftAppDiagnosticRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .download_powerlift_app_diagnostic import DownloadPowerliftAppDiagnosticRequest
		return DownloadPowerliftAppDiagnosticRequest(self.request_adapter, path_parameters)

	def execute_action(self,
		user_id: str,
	) -> ExecuteActionRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .execute_action import ExecuteActionRequest
		return ExecuteActionRequest(self.request_adapter, path_parameters)

	def move_devices_to_o_u(self,
		user_id: str,
	) -> MoveDevicesToOURequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .move_devices_to_o_u import MoveDevicesToOURequest
		return MoveDevicesToOURequest(self.request_adapter, path_parameters)

	def retrieve_powerlift_app_diagnostics_details_with_userprincipalname(self,
		user_id: str,
		userPrincipalName: str,
	) -> RetrievePowerliftAppDiagnosticsDetailsWithUserPrincipalNameRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if userPrincipalName is None:
			raise TypeError("userPrincipalName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["userPrincipalName"] =  userPrincipalName

		from .retrieve_powerlift_app_diagnostics_details_with_userprincipalname import RetrievePowerliftAppDiagnosticsDetailsWithUserPrincipalNameRequest
		return RetrievePowerliftAppDiagnosticsDetailsWithUserPrincipalNameRequest(self.request_adapter, path_parameters)

