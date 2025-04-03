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
	from .sync_inventory import SyncInventoryRequest
	from .execute_action import ExecuteActionRequest
	from .assign import AssignRequest
	from .driver_inventories import DriverInventoriesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.windows_driver_update_profile import WindowsDriverUpdateProfile


class ByWindowsDriverUpdateProfileIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/windowsDriverUpdateProfiles/{windowsDriverUpdateProfile%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsDriverUpdateProfile:
		"""
		Get windowsDriverUpdateProfiles from deviceManagement
		A collection of windows driver update profiles
		"""
		tags = ['deviceManagement.windowsDriverUpdateProfile']

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
		return await self.request_adapter.send_async(request_info, WindowsDriverUpdateProfile, error_mapping)

	async def patch(
		self,
		body: WindowsDriverUpdateProfile,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsDriverUpdateProfile:
		"""
		Update the navigation property windowsDriverUpdateProfiles in deviceManagement
		
		"""
		tags = ['deviceManagement.windowsDriverUpdateProfile']

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
		return await self.request_adapter.send_async(request_info, WindowsDriverUpdateProfile, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property windowsDriverUpdateProfiles for deviceManagement
		
		"""
		tags = ['deviceManagement.windowsDriverUpdateProfile']
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



	def with_url(self, raw_url: str) -> ByWindowsDriverUpdateProfileIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWindowsDriverUpdateProfileIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWindowsDriverUpdateProfileIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		windowsDriverUpdateProfile_id: str,
	) -> AssignmentsRequest:
		if windowsDriverUpdateProfile_id is None:
			raise TypeError("windowsDriverUpdateProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsDriverUpdateProfile%2Did"] =  windowsDriverUpdateProfile_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def driver_inventories(self,
		windowsDriverUpdateProfile_id: str,
	) -> DriverInventoriesRequest:
		if windowsDriverUpdateProfile_id is None:
			raise TypeError("windowsDriverUpdateProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsDriverUpdateProfile%2Did"] =  windowsDriverUpdateProfile_id

		from .driver_inventories import DriverInventoriesRequest
		return DriverInventoriesRequest(self.request_adapter, path_parameters)

	def assign(self,
		windowsDriverUpdateProfile_id: str,
	) -> AssignRequest:
		if windowsDriverUpdateProfile_id is None:
			raise TypeError("windowsDriverUpdateProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsDriverUpdateProfile%2Did"] =  windowsDriverUpdateProfile_id

		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, path_parameters)

	def execute_action(self,
		windowsDriverUpdateProfile_id: str,
	) -> ExecuteActionRequest:
		if windowsDriverUpdateProfile_id is None:
			raise TypeError("windowsDriverUpdateProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsDriverUpdateProfile%2Did"] =  windowsDriverUpdateProfile_id

		from .execute_action import ExecuteActionRequest
		return ExecuteActionRequest(self.request_adapter, path_parameters)

	def sync_inventory(self,
		windowsDriverUpdateProfile_id: str,
	) -> SyncInventoryRequest:
		if windowsDriverUpdateProfile_id is None:
			raise TypeError("windowsDriverUpdateProfile_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["windowsDriverUpdateProfile%2Did"] =  windowsDriverUpdateProfile_id

		from .sync_inventory import SyncInventoryRequest
		return SyncInventoryRequest(self.request_adapter, path_parameters)

