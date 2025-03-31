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
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.directory_object import DirectoryObject
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDirectoryObjectIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/transitiveMembers/{directoryObject%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryObject:
		"""
		Get transitiveMembers from groups
		The direct and transitive members of a group. Nullable.
		"""
		tags = ['groups.directoryObject']
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
		return await self.request_adapter.send_async(request_info, DirectoryObject, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByDirectoryObjectIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDirectoryObjectIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDirectoryObjectIdRequest(self.request_adapter, self.path_parameters)

	def graph_application(self,
		group_id: str,
		directoryObject_id: str,
	) -> GraphApplicationRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_application import GraphApplicationRequest
		return GraphApplicationRequest(self.request_adapter, path_parameters)

	def graph_device(self,
		group_id: str,
		directoryObject_id: str,
	) -> GraphDeviceRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_device import GraphDeviceRequest
		return GraphDeviceRequest(self.request_adapter, path_parameters)

	def graph_group(self,
		group_id: str,
		directoryObject_id: str,
	) -> GraphGroupRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_group import GraphGroupRequest
		return GraphGroupRequest(self.request_adapter, path_parameters)

	def graph_org_contact(self,
		group_id: str,
		directoryObject_id: str,
	) -> GraphOrgContactRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_org_contact import GraphOrgContactRequest
		return GraphOrgContactRequest(self.request_adapter, path_parameters)

	def graph_service_principal(self,
		group_id: str,
		directoryObject_id: str,
	) -> GraphServicePrincipalRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_service_principal import GraphServicePrincipalRequest
		return GraphServicePrincipalRequest(self.request_adapter, path_parameters)

	def graph_user(self,
		group_id: str,
		directoryObject_id: str,
	) -> GraphUserRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_user import GraphUserRequest
		return GraphUserRequest(self.request_adapter, path_parameters)

