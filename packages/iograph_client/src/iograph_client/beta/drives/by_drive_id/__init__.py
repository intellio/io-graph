# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .special import SpecialRequest
	from .root import RootRequest
	from .shared_with_me import SharedWithMeRequest
	from .search_with_q import SearchWithQRequest
	from .recent import RecentRequest
	from .list import ListRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .items import ItemsRequest
	from .following import FollowingRequest
	from .created_by_user import CreatedByUserRequest
	from .bundles import BundlesRequest
	from .activities import ActivitiesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.drive import Drive
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDriveIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Drive:
		"""
		Get entity from drives by key
		
		"""
		tags = ['drives.drive']

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
		return await self.request_adapter.send_async(request_info, Drive, error_mapping)

	async def patch(
		self,
		body: Drive,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Drive:
		"""
		Update entity in drives
		
		"""
		tags = ['drives.drive']

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
		return await self.request_adapter.send_async(request_info, Drive, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from drives
		
		"""
		tags = ['drives.drive']
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



	def with_url(self, raw_url: str) -> ByDriveIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDriveIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDriveIdRequest(self.request_adapter, self.path_parameters)

	def activities(self,
		drive_id: str,
	) -> ActivitiesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .activities import ActivitiesRequest
		return ActivitiesRequest(self.request_adapter, path_parameters)

	def bundles(self,
		drive_id: str,
	) -> BundlesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .bundles import BundlesRequest
		return BundlesRequest(self.request_adapter, path_parameters)

	def created_by_user(self,
		drive_id: str,
	) -> CreatedByUserRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, path_parameters)

	def following(self,
		drive_id: str,
	) -> FollowingRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .following import FollowingRequest
		return FollowingRequest(self.request_adapter, path_parameters)

	def items(self,
		drive_id: str,
	) -> ItemsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .items import ItemsRequest
		return ItemsRequest(self.request_adapter, path_parameters)

	def last_modified_by_user(self,
		drive_id: str,
	) -> LastModifiedByUserRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, path_parameters)

	def list(self,
		drive_id: str,
	) -> ListRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .list import ListRequest
		return ListRequest(self.request_adapter, path_parameters)

	def recent(self,
		drive_id: str,
	) -> RecentRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .recent import RecentRequest
		return RecentRequest(self.request_adapter, path_parameters)

	def search_with_q(self,
		drive_id: str,
		q: str,
	) -> SearchWithQRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if q is None:
			raise TypeError("q cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["q"] =  q

		from .search_with_q import SearchWithQRequest
		return SearchWithQRequest(self.request_adapter, path_parameters)

	def shared_with_me(self,
		drive_id: str,
	) -> SharedWithMeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .shared_with_me import SharedWithMeRequest
		return SharedWithMeRequest(self.request_adapter, path_parameters)

	def root(self,
		drive_id: str,
	) -> RootRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .root import RootRequest
		return RootRequest(self.request_adapter, path_parameters)

	def special(self,
		drive_id: str,
	) -> SpecialRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id

		from .special import SpecialRequest
		return SpecialRequest(self.request_adapter, path_parameters)

