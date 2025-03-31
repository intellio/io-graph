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
	from .owners import OwnersRequest
	from .create_device_from_template import CreateDeviceFromTemplateRequest
	from .device_instances_with_deviceid import DeviceInstancesWithDeviceIdRequest
	from .device_instances import DeviceInstancesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_template import DeviceTemplate
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDeviceTemplateIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/templates/deviceTemplates/{deviceTemplate%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceTemplate:
		"""
		Get deviceTemplates from templates
		Defines the templates that are common to a set of device objects, such as IoT devices.
		"""
		tags = ['templates.deviceTemplate']

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
		return await self.request_adapter.send_async(request_info, DeviceTemplate, error_mapping)

	async def patch(
		self,
		body: DeviceTemplate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceTemplate:
		"""
		Update the navigation property deviceTemplates in templates
		
		"""
		tags = ['templates.deviceTemplate']

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
		return await self.request_adapter.send_async(request_info, DeviceTemplate, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property deviceTemplates for templates
		
		"""
		tags = ['templates.deviceTemplate']
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



	def with_url(self, raw_url: str) -> ByDeviceTemplateIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDeviceTemplateIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDeviceTemplateIdRequest(self.request_adapter, self.path_parameters)

	def device_instances(self,
		deviceTemplate_id: str,
	) -> DeviceInstancesRequest:
		if deviceTemplate_id is None:
			raise TypeError("deviceTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceTemplate%2Did"] =  deviceTemplate_id

		from .device_instances import DeviceInstancesRequest
		return DeviceInstancesRequest(self.request_adapter, path_parameters)

	def device_instances_with_deviceid(self,
		deviceTemplate_id: str,
		deviceId: str,
	) -> DeviceInstancesWithDeviceIdRequest:
		if deviceTemplate_id is None:
			raise TypeError("deviceTemplate_id cannot be null.")
		if deviceId is None:
			raise TypeError("deviceId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceTemplate%2Did"] =  deviceTemplate_id
		path_parameters["deviceId"] =  deviceId

		from .device_instances_with_deviceid import DeviceInstancesWithDeviceIdRequest
		return DeviceInstancesWithDeviceIdRequest(self.request_adapter, path_parameters)

	def create_device_from_template(self,
		deviceTemplate_id: str,
	) -> CreateDeviceFromTemplateRequest:
		if deviceTemplate_id is None:
			raise TypeError("deviceTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceTemplate%2Did"] =  deviceTemplate_id

		from .create_device_from_template import CreateDeviceFromTemplateRequest
		return CreateDeviceFromTemplateRequest(self.request_adapter, path_parameters)

	def owners(self,
		deviceTemplate_id: str,
	) -> OwnersRequest:
		if deviceTemplate_id is None:
			raise TypeError("deviceTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["deviceTemplate%2Did"] =  deviceTemplate_id

		from .owners import OwnersRequest
		return OwnersRequest(self.request_adapter, path_parameters)

