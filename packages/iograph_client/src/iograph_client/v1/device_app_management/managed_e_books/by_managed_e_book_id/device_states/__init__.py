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
	from .count import CountRequest
	from .by_device_install_state_id import ByDeviceInstallStateIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.device_install_state import DeviceInstallState
from iograph_models.v1.device_install_state_collection_response import DeviceInstallStateCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class DeviceStatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/managedEBooks/{managedEBook%2Did}/deviceStates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceInstallStateCollectionResponse:
		"""
		List deviceInstallStates
		List properties and relationships of the deviceInstallState objects.
		Find more info here: https://learn.microsoft.com/graph/api/intune-books-deviceinstallstate-list?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.managedEBook']

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
		return await self.request_adapter.send_async(request_info, DeviceInstallStateCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceInstallState,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceInstallState:
		"""
		Create deviceInstallState
		Create a new deviceInstallState object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-books-deviceinstallstate-create?view=graph-rest-1.0
		"""
		tags = ['deviceAppManagement.managedEBook']

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
		return await self.request_adapter.send_async(request_info, DeviceInstallState, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceStatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceStatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceStatesRequest(self.request_adapter, self.path_parameters)

	def by_device_install_state_id(self,
		managedEBook_id: str,
		deviceInstallState_id: str,
	) -> ByDeviceInstallStateIdRequest:
		if managedEBook_id is None:
			raise TypeError("managedEBook_id cannot be null.")
		if deviceInstallState_id is None:
			raise TypeError("deviceInstallState_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedEBook%2Did"] =  managedEBook_id
		path_parameters["deviceInstallState%2Did"] =  deviceInstallState_id

		from .by_device_install_state_id import ByDeviceInstallStateIdRequest
		return ByDeviceInstallStateIdRequest(self.request_adapter, path_parameters)

	def count(self,
		managedEBook_id: str,
	) -> CountRequest:
		if managedEBook_id is None:
			raise TypeError("managedEBook_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["managedEBook%2Did"] =  managedEBook_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

