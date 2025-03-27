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
	from .graph_group import GraphGroupRequest
	from .graph_administrative_unit import GraphAdministrativeUnitRequest
	from .count import CountRequest
	from .by_directory_object_id import ByDirectoryObjectIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.directory_object_collection_response import DirectoryObjectCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class MemberOfRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/contacts/{orgContact%2Did}/memberOf", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryObjectCollectionResponse:
		"""
		List memberOf
		List the groups that this organizational contact is a member of.
		Find more info here: https://learn.microsoft.com/graph/api/orgcontact-list-memberof?view=graph-rest-1.0
		"""
		tags = ['contacts.directoryObject']
		header_parameters = [{'name': 'ConsistencyLevel', 'in': 'header', 'description': 'Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries', 'schema': {'type': 'string'}, 'examples': {'example-1': {'description': "$search and $count queries require the client to set the ConsistencyLevel HTTP header to 'eventual'.", 'value': 'eventual'}}}]

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
		return await self.request_adapter.send_async(request_info, DirectoryObjectCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> MemberOfRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MemberOfRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MemberOfRequest(self.request_adapter, self.path_parameters)

	def by_directory_object_id(self,
		orgContact_id: str,
		directoryObject_id: str,
	) -> ByDirectoryObjectIdRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .by_directory_object_id import ByDirectoryObjectIdRequest
		return ByDirectoryObjectIdRequest(self.request_adapter, path_parameters)

	def count(self,
		orgContact_id: str,
	) -> CountRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def graph_administrative_unit(self,
		orgContact_id: str,
	) -> GraphAdministrativeUnitRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .graph_administrative_unit import GraphAdministrativeUnitRequest
		return GraphAdministrativeUnitRequest(self.request_adapter, path_parameters)

	def graph_group(self,
		orgContact_id: str,
	) -> GraphGroupRequest:
		if orgContact_id is None:
			raise TypeError("orgContact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["orgContact%2Did"] =  orgContact_id

		from .graph_group import GraphGroupRequest
		return GraphGroupRequest(self.request_adapter, path_parameters)

