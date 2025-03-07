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
	from .get_compatible_hub_content_types import GetCompatibleHubContentTypesRequest
	from .add_copy_from_content_type_hub import AddCopyFromContentTypeHubRequest
	from .add_copy import AddCopyRequest
	from .count import CountRequest
	from .by_content_type_id import ByContentTypeIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.content_type import ContentType
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.content_type_collection_response import ContentTypeCollectionResponse


class ContentTypesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/list/contentTypes", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ContentTypeCollectionResponse:
		"""
		Get contentTypes from drives
		The collection of content types present in this list.
		"""
		tags = ['drives.list']

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
		return await self.request_adapter.send_async(request_info, ContentTypeCollectionResponse, error_mapping)

	async def post(
		self,
		body: ContentType,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ContentType:
		"""
		Create new navigation property to contentTypes for drives
		
		"""
		tags = ['drives.list']

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
		return await self.request_adapter.send_async(request_info, ContentType, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ContentTypesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ContentTypesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ContentTypesRequest(self.request_adapter, self.path_parameters)

	def by_content_type_id(self,
		drive_id: str,
		contentType_id: str,
	) -> ByContentTypeIdRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .by_content_type_id import ByContentTypeIdRequest
		return ByContentTypeIdRequest(self.request_adapter, path_parameters)

	def count(self,
		drive_id: str,
	) -> CountRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def add_copy(self,
		drive_id: str,
	) -> AddCopyRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .add_copy import AddCopyRequest
		return AddCopyRequest(self.request_adapter, path_parameters)

	def add_copy_from_content_type_hub(self,
		drive_id: str,
	) -> AddCopyFromContentTypeHubRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .add_copy_from_content_type_hub import AddCopyFromContentTypeHubRequest
		return AddCopyFromContentTypeHubRequest(self.request_adapter, path_parameters)

	def get_compatible_hub_content_types(self,
		drive_id: str,
	) -> GetCompatibleHubContentTypesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .get_compatible_hub_content_types import GetCompatibleHubContentTypesRequest
		return GetCompatibleHubContentTypesRequest(self.request_adapter, path_parameters)

