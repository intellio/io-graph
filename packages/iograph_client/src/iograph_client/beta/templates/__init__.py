# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .device_templates import DeviceTemplatesRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.template import Template
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class TemplatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/templates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Template:
		"""
		Get templates
		
		"""
		tags = ['templates.template']

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
		return await self.request_adapter.send_async(request_info, Template, error_mapping)

	async def patch(
		self,
		body: Template,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Template:
		"""
		Update templates
		
		"""
		tags = ['templates.template']

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
		return await self.request_adapter.send_async(request_info, Template, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TemplatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TemplatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_templates(self,
	) -> DeviceTemplatesRequest:
		from .device_templates import DeviceTemplatesRequest
		return DeviceTemplatesRequest(self.request_adapter, self.path_parameters)

