# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .webparts import WebpartsRequest
	from ............request_adapter import HttpxRequestAdapter
from iograph_models.models.horizontal_section_column import HorizontalSectionColumn
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByHorizontalSectionColumnIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/pages/{baseSitePage%2Did}/graph.sitePage/canvasLayout/horizontalSections/{horizontalSection%2Did}/columns/{horizontalSectionColumn%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> HorizontalSectionColumn:
		"""
		Get columns from sites
		The set of vertical columns in this section.
		"""
		tags = ['sites.baseSitePage']

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
		return await self.request_adapter.send_async(request_info, HorizontalSectionColumn, error_mapping)

	async def patch(
		self,
		body: HorizontalSectionColumn,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> HorizontalSectionColumn:
		"""
		Update the navigation property columns in sites
		
		"""
		tags = ['sites.baseSitePage']

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
		return await self.request_adapter.send_async(request_info, HorizontalSectionColumn, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property columns for sites
		
		"""
		tags = ['sites.baseSitePage']
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



	def with_url(self, raw_url: str) -> ByHorizontalSectionColumnIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByHorizontalSectionColumnIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByHorizontalSectionColumnIdRequest(self.request_adapter, self.path_parameters)

	def webparts(self,
		site_id: str,
		baseSitePage_id: str,
		horizontalSection_id: str,
		horizontalSectionColumn_id: str,
	) -> WebpartsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if baseSitePage_id is None:
			raise TypeError("baseSitePage_id cannot be null.")
		if horizontalSection_id is None:
			raise TypeError("horizontalSection_id cannot be null.")
		if horizontalSectionColumn_id is None:
			raise TypeError("horizontalSectionColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["baseSitePage%2Did"] =  baseSitePage_id
		path_parameters["horizontalSection%2Did"] =  horizontalSection_id
		path_parameters["horizontalSectionColumn%2Did"] =  horizontalSectionColumn_id

		from .webparts import WebpartsRequest
		return WebpartsRequest(self.request_adapter, path_parameters)

