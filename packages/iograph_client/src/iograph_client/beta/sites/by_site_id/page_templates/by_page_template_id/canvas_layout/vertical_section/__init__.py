# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .webparts import WebpartsRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.vertical_section import VerticalSection
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class VerticalSectionRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/pageTemplates/{pageTemplate%2Did}/canvasLayout/verticalSection", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VerticalSection:
		"""
		Get verticalSection from sites
		Vertical section on the SharePoint page.
		"""
		tags = ['sites.pageTemplate']

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
		return await self.request_adapter.send_async(request_info, VerticalSection, error_mapping)

	async def patch(
		self,
		body: VerticalSection,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> VerticalSection:
		"""
		Update the navigation property verticalSection in sites
		
		"""
		tags = ['sites.pageTemplate']

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
		return await self.request_adapter.send_async(request_info, VerticalSection, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property verticalSection for sites
		
		"""
		tags = ['sites.pageTemplate']
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



	def with_url(self, raw_url: str) -> VerticalSectionRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: VerticalSectionRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return VerticalSectionRequest(self.request_adapter, self.path_parameters)

	def webparts(self,
		site_id: str,
		pageTemplate_id: str,
	) -> WebpartsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if pageTemplate_id is None:
			raise TypeError("pageTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["pageTemplate%2Did"] =  pageTemplate_id

		from .webparts import WebpartsRequest
		return WebpartsRequest(self.request_adapter, path_parameters)

