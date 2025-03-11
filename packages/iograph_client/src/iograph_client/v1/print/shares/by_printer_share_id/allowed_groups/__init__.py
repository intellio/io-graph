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
	from .ref import RefRequest
	from .count import CountRequest
	from .by_group_id import ByGroupIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.group_collection_response import GroupCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class AllowedGroupsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print/shares/{printerShare%2Did}/allowedGroups", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupCollectionResponse:
		"""
		List allowedGroups
		Retrieve a list of groups that have been granted access to submit print jobs to the associated printerShare.
		Find more info here: https://learn.microsoft.com/graph/api/printershare-list-allowedgroups?view=graph-rest-1.0
		"""
		tags = ['print.printerShare']

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
		return await self.request_adapter.send_async(request_info, GroupCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> AllowedGroupsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AllowedGroupsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AllowedGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def by_group_id(self,
	) -> ByGroupIdRequest:
		from .by_group_id import ByGroupIdRequest
		return ByGroupIdRequest(self.request_adapter, self.path_parameters)

	def count(self,
		printerShare_id: str,
	) -> CountRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def ref(self,
		printerShare_id: str,
	) -> RefRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

