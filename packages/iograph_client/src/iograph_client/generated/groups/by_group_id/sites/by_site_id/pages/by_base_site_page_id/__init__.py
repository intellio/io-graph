# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .graph_site_page import GraphSitePageRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .created_by_user import CreatedByUserRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.base_site_page import BaseSitePage
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByBaseSitePageIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/pages/{baseSitePage%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BaseSitePage:
		"""
		Get pages from groups
		The collection of pages in the baseSitePages list in this site.
		"""
		tags = ['groups.site']

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
		return await self.request_adapter.send_async(request_info, BaseSitePage, error_mapping)

	async def patch(
		self,
		body: BaseSitePage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> BaseSitePage:
		"""
		Update the navigation property pages in groups
		
		"""
		tags = ['groups.site']

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
		return await self.request_adapter.send_async(request_info, BaseSitePage, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property pages for groups
		
		"""
		tags = ['groups.site']
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



	def with_url(self, raw_url: str) -> ByBaseSitePageIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByBaseSitePageIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByBaseSitePageIdRequest(self.request_adapter, self.path_parameters)

	@property
	def created_by_user(self,
	) -> CreatedByUserRequest:
		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def last_modified_by_user(self,
	) -> LastModifiedByUserRequest:
		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_site_page(self,
	) -> GraphSitePageRequest:
		from .graph_site_page import GraphSitePageRequest
		return GraphSitePageRequest(self.request_adapter, self.path_parameters)

