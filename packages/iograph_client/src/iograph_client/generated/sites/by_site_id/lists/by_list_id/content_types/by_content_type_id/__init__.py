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
	from .unpublish import UnpublishRequest
	from .publish import PublishRequest
	from .copy_to_default_content_location import CopyToDefaultContentLocationRequest
	from .associate_with_hub_sites import AssociateWithHubSitesRequest
	from .columns import ColumnsRequest
	from .column_positions import ColumnPositionsRequest
	from .column_links import ColumnLinksRequest
	from .base_types import BaseTypesRequest
	from .base import BaseRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.content_type import ContentType
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByContentTypeIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/lists/{list%2Did}/contentTypes/{contentType%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ContentType:
		"""
		Get contentTypes from sites
		The collection of content types present in this list.
		"""
		tags = ['sites.list']

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
		return await self.request_adapter.send_async(request_info, ContentType, error_mapping)

	async def patch(
		self,
		body: ContentType,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ContentType:
		"""
		Update the navigation property contentTypes in sites
		
		"""
		tags = ['sites.list']

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
		return await self.request_adapter.send_async(request_info, ContentType, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property contentTypes for sites
		
		"""
		tags = ['sites.list']
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



	def with_url(self, raw_url: str) -> ByContentTypeIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByContentTypeIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByContentTypeIdRequest(self.request_adapter, self.path_parameters)

	@property
	def base(self,
	) -> BaseRequest:
		from .base import BaseRequest
		return BaseRequest(self.request_adapter, self.path_parameters)

	@property
	def base_types(self,
	) -> BaseTypesRequest:
		from .base_types import BaseTypesRequest
		return BaseTypesRequest(self.request_adapter, self.path_parameters)

	@property
	def column_links(self,
	) -> ColumnLinksRequest:
		from .column_links import ColumnLinksRequest
		return ColumnLinksRequest(self.request_adapter, self.path_parameters)

	@property
	def column_positions(self,
	) -> ColumnPositionsRequest:
		from .column_positions import ColumnPositionsRequest
		return ColumnPositionsRequest(self.request_adapter, self.path_parameters)

	@property
	def columns(self,
	) -> ColumnsRequest:
		from .columns import ColumnsRequest
		return ColumnsRequest(self.request_adapter, self.path_parameters)

	@property
	def associate_with_hub_sites(self,
	) -> AssociateWithHubSitesRequest:
		from .associate_with_hub_sites import AssociateWithHubSitesRequest
		return AssociateWithHubSitesRequest(self.request_adapter, self.path_parameters)

	@property
	def copy_to_default_content_location(self,
	) -> CopyToDefaultContentLocationRequest:
		from .copy_to_default_content_location import CopyToDefaultContentLocationRequest
		return CopyToDefaultContentLocationRequest(self.request_adapter, self.path_parameters)

	@property
	def publish(self,
	) -> PublishRequest:
		from .publish import PublishRequest
		return PublishRequest(self.request_adapter, self.path_parameters)

	@property
	def unpublish(self,
	) -> UnpublishRequest:
		from .unpublish import UnpublishRequest
		return UnpublishRequest(self.request_adapter, self.path_parameters)

