# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_device_compliance_policy_state_id import ByDeviceCompliancePolicyStateIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.device_compliance_policy_state import DeviceCompliancePolicyState
from iograph_models.models.device_compliance_policy_state_collection_response import DeviceCompliancePolicyStateCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class DeviceCompliancePolicyStatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/managedDevices/{managedDevice%2Did}/deviceCompliancePolicyStates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceCompliancePolicyStateCollectionResponse:
		"""
		Get deviceCompliancePolicyStates from users
		Device compliance policy states for this device.
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
		return await self.request_adapter.send_async(request_info, DeviceCompliancePolicyStateCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceCompliancePolicyState,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceCompliancePolicyState:
		"""
		Create new navigation property to deviceCompliancePolicyStates for users
		
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
		return await self.request_adapter.send_async(request_info, DeviceCompliancePolicyState, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceCompliancePolicyStatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceCompliancePolicyStatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceCompliancePolicyStatesRequest(self.request_adapter, self.path_parameters)

	def by_device_compliance_policy_state_id(self,
		user_id: str,
		managedDevice_id: str,
		deviceCompliancePolicyState_id: str,
	) -> ByDeviceCompliancePolicyStateIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if managedDevice_id is None:
			raise TypeError("managedDevice_id cannot be null.")
		if deviceCompliancePolicyState_id is None:
			raise TypeError("deviceCompliancePolicyState_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["managedDevice%2Did"] =  managedDevice_id
		path_parameters["deviceCompliancePolicyState%2Did"] =  deviceCompliancePolicyState_id

		from .by_device_compliance_policy_state_id import ByDeviceCompliancePolicyStateIdRequest
		return ByDeviceCompliancePolicyStateIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

