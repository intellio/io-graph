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
	from .graph_service_principal import GraphServicePrincipalRequest
	from .graph_group import GraphGroupRequest
	from .graph_endpoint import GraphEndpointRequest
	from .graph_app_role_assignment import GraphAppRoleAssignmentRequest
	from .graph_application import GraphApplicationRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.directory_object import DirectoryObject
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDirectoryObjectIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/ownedObjects/{directoryObject%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryObject:
		"""
		Get ownedObjects from servicePrincipals
		Directory objects that are owned by this service principal. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
		"""
		tags = ['servicePrincipals.directoryObject']

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
		servicePrincipal_id: str,
		directoryObject_id: str,
	) -> GraphApplicationRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_application import GraphApplicationRequest
		return GraphApplicationRequest(self.request_adapter, path_parameters)

	def graph_app_role_assignment(self,
		servicePrincipal_id: str,
		directoryObject_id: str,
	) -> GraphAppRoleAssignmentRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_app_role_assignment import GraphAppRoleAssignmentRequest
		return GraphAppRoleAssignmentRequest(self.request_adapter, path_parameters)

	def graph_endpoint(self,
		servicePrincipal_id: str,
		directoryObject_id: str,
	) -> GraphEndpointRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_endpoint import GraphEndpointRequest
		return GraphEndpointRequest(self.request_adapter, path_parameters)

	def graph_group(self,
		servicePrincipal_id: str,
		directoryObject_id: str,
	) -> GraphGroupRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_group import GraphGroupRequest
		return GraphGroupRequest(self.request_adapter, path_parameters)

	def graph_service_principal(self,
		servicePrincipal_id: str,
		directoryObject_id: str,
	) -> GraphServicePrincipalRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_service_principal import GraphServicePrincipalRequest
		return GraphServicePrincipalRequest(self.request_adapter, path_parameters)

