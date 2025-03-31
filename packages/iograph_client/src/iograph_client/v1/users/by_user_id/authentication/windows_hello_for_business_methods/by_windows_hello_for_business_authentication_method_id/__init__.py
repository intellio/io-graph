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
	from .device import DeviceRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByWindowsHelloForBusinessAuthenticationMethodIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/authentication/windowsHelloForBusinessMethods/{windowsHelloForBusinessAuthenticationMethod%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsHelloForBusinessAuthenticationMethod:
		"""
		Get windowsHelloForBusinessAuthenticationMethod
		Read the properties and relationships of a windowsHelloForBusinessAuthenticationMethod object.
		Find more info here: https://learn.microsoft.com/graph/api/windowshelloforbusinessauthenticationmethod-get?view=graph-rest-1.0
		"""
		tags = ['users.authentication']

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
		return await self.request_adapter.send_async(request_info, WindowsHelloForBusinessAuthenticationMethod, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete windowsHelloForBusinessAuthenticationMethod
		Deletes a windowsHelloForBusinessAuthenticationMethod object.
		Find more info here: https://learn.microsoft.com/graph/api/windowshelloforbusinessauthenticationmethod-delete?view=graph-rest-1.0
		"""
		tags = ['users.authentication']
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


	def with_url(self, raw_url: str) -> ByWindowsHelloForBusinessAuthenticationMethodIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWindowsHelloForBusinessAuthenticationMethodIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWindowsHelloForBusinessAuthenticationMethodIdRequest(self.request_adapter, self.path_parameters)

	def device(self,
		user_id: str,
		windowsHelloForBusinessAuthenticationMethod_id: str,
	) -> DeviceRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if windowsHelloForBusinessAuthenticationMethod_id is None:
			raise TypeError("windowsHelloForBusinessAuthenticationMethod_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["windowsHelloForBusinessAuthenticationMethod%2Did"] =  windowsHelloForBusinessAuthenticationMethod_id

		from .device import DeviceRequest
		return DeviceRequest(self.request_adapter, path_parameters)

