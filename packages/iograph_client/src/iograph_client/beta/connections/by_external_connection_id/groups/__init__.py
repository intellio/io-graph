# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_external_group_id import ByExternalGroupIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.external_connectors_external_group_collection_response import ExternalConnectorsExternalGroupCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.external_connectors_external_group import ExternalConnectorsExternalGroup


class GroupsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/connections/{externalConnection%2Did}/groups", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExternalConnectorsExternalGroupCollectionResponse:
		"""
		Get groups from connections
		
		"""
		tags = ['connections.externalGroup']

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
		return await self.request_adapter.send_async(request_info, ExternalConnectorsExternalGroupCollectionResponse, error_mapping)

	async def post(
		self,
		body: ExternalConnectorsExternalGroup,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ExternalConnectorsExternalGroup:
		"""
		Create new navigation property to groups for connections
		
		"""
		tags = ['connections.externalGroup']

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
		return await self.request_adapter.send_async(request_info, ExternalConnectorsExternalGroup, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> GroupsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GroupsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GroupsRequest(self.request_adapter, self.path_parameters)

	def by_external_group_id(self,
		externalConnection_id: str,
		externalGroup_id: str,
	) -> ByExternalGroupIdRequest:
		if externalConnection_id is None:
			raise TypeError("externalConnection_id cannot be null.")
		if externalGroup_id is None:
			raise TypeError("externalGroup_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalConnection%2Did"] =  externalConnection_id
		path_parameters["externalGroup%2Did"] =  externalGroup_id

		from .by_external_group_id import ByExternalGroupIdRequest
		return ByExternalGroupIdRequest(self.request_adapter, path_parameters)

	def count(self,
		externalConnection_id: str,
	) -> CountRequest:
		if externalConnection_id is None:
			raise TypeError("externalConnection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["externalConnection%2Did"] =  externalConnection_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

