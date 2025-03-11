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
	from .assign_and_activate_by_serial_number import AssignAndActivateBySerialNumberRequest
	from .assign_and_activate import AssignAndActivateRequest
	from .count import CountRequest
	from .by_hardware_oath_authentication_method_id import ByHardwareOathAuthenticationMethodIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.hardware_oath_authentication_method import HardwareOathAuthenticationMethod
from iograph_models.beta.hardware_oath_authentication_method_collection_response import HardwareOathAuthenticationMethodCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class HardwareOathMethodsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/authentication/hardwareOathMethods", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> HardwareOathAuthenticationMethodCollectionResponse:
		"""
		List hardwareOathAuthenticationMethod objects
		Get a list of the hardware tokens assigned to a user.
		Find more info here: https://learn.microsoft.com/graph/api/authentication-list-hardwareoathmethods?view=graph-rest-beta
		"""
		tags = ['me.authentication']

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
		return await self.request_adapter.send_async(request_info, HardwareOathAuthenticationMethodCollectionResponse, error_mapping)

	async def post(
		self,
		body: HardwareOathAuthenticationMethod,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> HardwareOathAuthenticationMethod:
		"""
		Create hardwareOathAuthenticationMethod
		Assign a hardware token to a user without activation. To activate, use the activation API operation.
		Find more info here: https://learn.microsoft.com/graph/api/authentication-post-hardwareoathmethods?view=graph-rest-beta
		"""
		tags = ['me.authentication']

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
		return await self.request_adapter.send_async(request_info, HardwareOathAuthenticationMethod, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> HardwareOathMethodsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: HardwareOathMethodsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return HardwareOathMethodsRequest(self.request_adapter, self.path_parameters)

	def by_hardware_oath_authentication_method_id(self,
		hardwareOathAuthenticationMethod_id: str,
	) -> ByHardwareOathAuthenticationMethodIdRequest:
		if hardwareOathAuthenticationMethod_id is None:
			raise TypeError("hardwareOathAuthenticationMethod_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["hardwareOathAuthenticationMethod%2Did"] =  hardwareOathAuthenticationMethod_id

		from .by_hardware_oath_authentication_method_id import ByHardwareOathAuthenticationMethodIdRequest
		return ByHardwareOathAuthenticationMethodIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def assign_and_activate(self,
	) -> AssignAndActivateRequest:
		from .assign_and_activate import AssignAndActivateRequest
		return AssignAndActivateRequest(self.request_adapter, self.path_parameters)

	@property
	def assign_and_activate_by_serial_number(self,
	) -> AssignAndActivateBySerialNumberRequest:
		from .assign_and_activate_by_serial_number import AssignAndActivateBySerialNumberRequest
		return AssignAndActivateBySerialNumberRequest(self.request_adapter, self.path_parameters)

