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
	from .graph_user import GraphUserRequest
	from .graph_service_principal import GraphServicePrincipalRequest
	from .graph_org_contact import GraphOrgContactRequest
	from .graph_group import GraphGroupRequest
	from .graph_device import GraphDeviceRequest
	from .graph_application import GraphApplicationRequest
	from .ref import RefRequest
	from .count import CountRequest
	from .by_directory_object_id import ByDirectoryObjectIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.directory_object import DirectoryObject
from iograph_models.models.directory_object_collection_response import DirectoryObjectCollectionResponse


class MembersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/administrativeUnits/{administrativeUnit%2Did}/members", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryObjectCollectionResponse:
		"""
		List members
		Use this API to get the members list (users, groups, or devices) in an administrative unit.
		Find more info here: https://learn.microsoft.com/graph/api/administrativeunit-list-members?view=graph-rest-1.0
		"""
		tags = ['directory.administrativeUnit']
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

	async def post(
		self,
		body: DirectoryObject,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DirectoryObject:
		"""
		Add a member
		Use this API to add a member (user, group, or device) to an administrative unit. Currently it's only possible to add one member at a time to an administrative unit.
		Find more info here: https://learn.microsoft.com/graph/api/administrativeunit-post-members?view=graph-rest-1.0
		"""
		tags = ['directory.administrativeUnit']

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
		return await self.request_adapter.send_async(request_info, DirectoryObject, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MembersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MembersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MembersRequest(self.request_adapter, self.path_parameters)

	@property
	def by_directory_object_id(self,
	) -> ByDirectoryObjectIdRequest:
		from .by_directory_object_id import ByDirectoryObjectIdRequest
		return ByDirectoryObjectIdRequest(self.request_adapter, self.path_parameters)

	def count(self,
		administrativeUnit_id: str,
	) -> CountRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def ref(self,
		administrativeUnit_id: str,
	) -> RefRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

	def graph_application(self,
		administrativeUnit_id: str,
	) -> GraphApplicationRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .graph_application import GraphApplicationRequest
		return GraphApplicationRequest(self.request_adapter, path_parameters)

	def graph_device(self,
		administrativeUnit_id: str,
	) -> GraphDeviceRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .graph_device import GraphDeviceRequest
		return GraphDeviceRequest(self.request_adapter, path_parameters)

	def graph_group(self,
		administrativeUnit_id: str,
	) -> GraphGroupRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .graph_group import GraphGroupRequest
		return GraphGroupRequest(self.request_adapter, path_parameters)

	def graph_org_contact(self,
		administrativeUnit_id: str,
	) -> GraphOrgContactRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .graph_org_contact import GraphOrgContactRequest
		return GraphOrgContactRequest(self.request_adapter, path_parameters)

	def graph_service_principal(self,
		administrativeUnit_id: str,
	) -> GraphServicePrincipalRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .graph_service_principal import GraphServicePrincipalRequest
		return GraphServicePrincipalRequest(self.request_adapter, path_parameters)

	def graph_user(self,
		administrativeUnit_id: str,
	) -> GraphUserRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .graph_user import GraphUserRequest
		return GraphUserRequest(self.request_adapter, path_parameters)

