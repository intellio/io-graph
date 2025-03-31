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
	from .subscriptions import SubscriptionsRequest
	from .operations import OperationsRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .items import ItemsRequest
	from .drive import DriveRequest
	from .created_by_user import CreatedByUserRequest
	from .content_types import ContentTypesRequest
	from .columns import ColumnsRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.v1.list import List
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByListIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/lists/{list%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> List:
		"""
		Get lists from groups
		The collection of lists under this site.
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
		return await self.request_adapter.send_async(request_info, List, error_mapping)

	async def patch(
		self,
		body: List,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> List:
		"""
		Update the navigation property lists in groups
		
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
		return await self.request_adapter.send_async(request_info, List, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property lists for groups
		
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



	def with_url(self, raw_url: str) -> ByListIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByListIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByListIdRequest(self.request_adapter, self.path_parameters)

	def columns(self,
		group_id: str,
		site_id: str,
		list_id: str,
	) -> ColumnsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id

		from .columns import ColumnsRequest
		return ColumnsRequest(self.request_adapter, path_parameters)

	def content_types(self,
		group_id: str,
		site_id: str,
		list_id: str,
	) -> ContentTypesRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id

		from .content_types import ContentTypesRequest
		return ContentTypesRequest(self.request_adapter, path_parameters)

	def created_by_user(self,
		group_id: str,
		site_id: str,
		list_id: str,
	) -> CreatedByUserRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id

		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, path_parameters)

	def drive(self,
		group_id: str,
		site_id: str,
		list_id: str,
	) -> DriveRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id

		from .drive import DriveRequest
		return DriveRequest(self.request_adapter, path_parameters)

	def items(self,
		group_id: str,
		site_id: str,
		list_id: str,
	) -> ItemsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id

		from .items import ItemsRequest
		return ItemsRequest(self.request_adapter, path_parameters)

	def last_modified_by_user(self,
		group_id: str,
		site_id: str,
		list_id: str,
	) -> LastModifiedByUserRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id

		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, path_parameters)

	def operations(self,
		group_id: str,
		site_id: str,
		list_id: str,
	) -> OperationsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def subscriptions(self,
		group_id: str,
		site_id: str,
		list_id: str,
	) -> SubscriptionsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id

		from .subscriptions import SubscriptionsRequest
		return SubscriptionsRequest(self.request_adapter, path_parameters)

