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
	from .by_device_management_intent_user_state_id import ByDeviceManagementIntentUserStateIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management_intent_user_state import DeviceManagementIntentUserState
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.device_management_intent_user_state_collection_response import DeviceManagementIntentUserStateCollectionResponse


class UserStatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/intents/{deviceManagementIntent%2Did}/userStates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementIntentUserStateCollectionResponse:
		"""
		Get userStates from deviceManagement
		Collection of states of all users that the intent is applied to
		"""
		tags = ['deviceManagement.deviceManagementIntent']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementIntentUserStateCollectionResponse, error_mapping)

	async def post(
		self,
		body: DeviceManagementIntentUserState,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementIntentUserState:
		"""
		Create new navigation property to userStates for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementIntent']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementIntentUserState, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> UserStatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UserStatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UserStatesRequest(self.request_adapter, self.path_parameters)

	def by_device_management_intent_user_state_id(self,
		deviceManagementIntent_id: str,
		deviceManagementIntentUserState_id: str,
	) -> ByDeviceManagementIntentUserStateIdRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")
		if deviceManagementIntentUserState_id is None:
			raise TypeError("deviceManagementIntentUserState_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id
		path_parameters["deviceManagementIntentUserState%2Did"] =  deviceManagementIntentUserState_id

		from .by_device_management_intent_user_state_id import ByDeviceManagementIntentUserStateIdRequest
		return ByDeviceManagementIntentUserStateIdRequest(self.request_adapter, path_parameters)

	def count(self,
		deviceManagementIntent_id: str,
	) -> CountRequest:
		if deviceManagementIntent_id is None:
			raise TypeError("deviceManagementIntent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceManagementIntent%2Did"] =  deviceManagementIntent_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

