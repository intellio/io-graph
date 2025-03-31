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
	from .assign_to import AssignToRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.hardware_oath_token_authentication_method_device import HardwareOathTokenAuthenticationMethodDevice
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByHardwareOathTokenAuthenticationMethodDeviceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/authenticationMethodDevices/hardwareOathDevices/{hardwareOathTokenAuthenticationMethodDevice%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> HardwareOathTokenAuthenticationMethodDevice:
		"""
		Get hardwareOathTokenAuthenticationMethodDevice
		Read the properties and relationships of a hardwareOathTokenAuthenticationMethodDevice object.
		Find more info here: https://learn.microsoft.com/graph/api/hardwareoathtokenauthenticationmethoddevice-get?view=graph-rest-beta
		"""
		tags = ['directory.authenticationMethodDevice']

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
		return await self.request_adapter.send_async(request_info, HardwareOathTokenAuthenticationMethodDevice, error_mapping)

	async def patch(
		self,
		body: HardwareOathTokenAuthenticationMethodDevice,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> HardwareOathTokenAuthenticationMethodDevice:
		"""
		Update hardwareOathTokenAuthenticationMethodDevice
		Update the properties of a hardwareOathTokenAuthenticationMethodDevice object. The token needs to unassigned.
		Find more info here: https://learn.microsoft.com/graph/api/hardwareoathtokenauthenticationmethoddevice-update?view=graph-rest-beta
		"""
		tags = ['directory.authenticationMethodDevice']

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
		return await self.request_adapter.send_async(request_info, HardwareOathTokenAuthenticationMethodDevice, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete hardwareOathTokenAuthenticationMethodDevice
		Delete a Hardware OATH token. Token needs to be unassigned.
		Find more info here: https://learn.microsoft.com/graph/api/authenticationmethoddevice-delete-hardwareoathdevices?view=graph-rest-beta
		"""
		tags = ['directory.authenticationMethodDevice']
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



	def with_url(self, raw_url: str) -> ByHardwareOathTokenAuthenticationMethodDeviceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByHardwareOathTokenAuthenticationMethodDeviceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByHardwareOathTokenAuthenticationMethodDeviceIdRequest(self.request_adapter, self.path_parameters)

	def assign_to(self,
		hardwareOathTokenAuthenticationMethodDevice_id: str,
	) -> AssignToRequest:
		if hardwareOathTokenAuthenticationMethodDevice_id is None:
			raise TypeError("hardwareOathTokenAuthenticationMethodDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["hardwareOathTokenAuthenticationMethodDevice%2Did"] =  hardwareOathTokenAuthenticationMethodDevice_id

		from .assign_to import AssignToRequest
		return AssignToRequest(self.request_adapter, path_parameters)

