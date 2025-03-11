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
	from .unpublish import UnpublishRequest
	from .publish import PublishRequest
	from .is_published import IsPublishedRequest
	from .copy_to_default_content_location import CopyToDefaultContentLocationRequest
	from .associate_with_hub_sites import AssociateWithHubSitesRequest
	from .columns import ColumnsRequest
	from .column_positions import ColumnPositionsRequest
	from .column_links import ColumnLinksRequest
	from .base_types import BaseTypesRequest
	from .base import BaseRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.content_type import ContentType


class ByContentTypeIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/contentTypes/{contentType%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ContentType:
		"""
		Get contentType
		Retrieve the metadata for a content type in a site or a list.
		Find more info here: https://learn.microsoft.com/graph/api/contenttype-get?view=graph-rest-beta
		"""
		tags = ['sites.contentType']

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
		Update contentType
		
		Find more info here: https://learn.microsoft.com/graph/api/contenttype-update?view=graph-rest-beta
		"""
		tags = ['sites.contentType']

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
		Delete contentType
		Remove a content type from a list or a site.
		Find more info here: https://learn.microsoft.com/graph/api/contenttype-delete?view=graph-rest-beta
		"""
		tags = ['sites.contentType']
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

	def base(self,
		site_id: str,
		contentType_id: str,
	) -> BaseRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .base import BaseRequest
		return BaseRequest(self.request_adapter, path_parameters)

	def base_types(self,
		site_id: str,
		contentType_id: str,
	) -> BaseTypesRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .base_types import BaseTypesRequest
		return BaseTypesRequest(self.request_adapter, path_parameters)

	def column_links(self,
		site_id: str,
		contentType_id: str,
	) -> ColumnLinksRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .column_links import ColumnLinksRequest
		return ColumnLinksRequest(self.request_adapter, path_parameters)

	def column_positions(self,
		site_id: str,
		contentType_id: str,
	) -> ColumnPositionsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .column_positions import ColumnPositionsRequest
		return ColumnPositionsRequest(self.request_adapter, path_parameters)

	def columns(self,
		site_id: str,
		contentType_id: str,
	) -> ColumnsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .columns import ColumnsRequest
		return ColumnsRequest(self.request_adapter, path_parameters)

	def associate_with_hub_sites(self,
		site_id: str,
		contentType_id: str,
	) -> AssociateWithHubSitesRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .associate_with_hub_sites import AssociateWithHubSitesRequest
		return AssociateWithHubSitesRequest(self.request_adapter, path_parameters)

	def copy_to_default_content_location(self,
		site_id: str,
		contentType_id: str,
	) -> CopyToDefaultContentLocationRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .copy_to_default_content_location import CopyToDefaultContentLocationRequest
		return CopyToDefaultContentLocationRequest(self.request_adapter, path_parameters)

	def is_published(self,
		site_id: str,
		contentType_id: str,
	) -> IsPublishedRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .is_published import IsPublishedRequest
		return IsPublishedRequest(self.request_adapter, path_parameters)

	def publish(self,
		site_id: str,
		contentType_id: str,
	) -> PublishRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .publish import PublishRequest
		return PublishRequest(self.request_adapter, path_parameters)

	def unpublish(self,
		site_id: str,
		contentType_id: str,
	) -> UnpublishRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .unpublish import UnpublishRequest
		return UnpublishRequest(self.request_adapter, path_parameters)

