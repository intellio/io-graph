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
	from .graph_endpoint import GraphEndpointRequest
	from .graph_app_role_assignment import GraphAppRoleAssignmentRequest
	from .ref import RefRequest
	from ......request_adapter import HttpxRequestAdapter


class ByDirectoryObjectIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applications/{application-id}/owners/{directoryObject-id}", path_parameters)

	def with_url(self, raw_url: str) -> ByDirectoryObjectIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDirectoryObjectIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDirectoryObjectIdRequest(self.request_adapter, self.path_parameters)

	def ref(self,
		application_id: str,
		directoryObject_id: str,
	) -> RefRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

	def graph_app_role_assignment(self,
		application_id: str,
		directoryObject_id: str,
	) -> GraphAppRoleAssignmentRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_app_role_assignment import GraphAppRoleAssignmentRequest
		return GraphAppRoleAssignmentRequest(self.request_adapter, path_parameters)

	def graph_endpoint(self,
		application_id: str,
		directoryObject_id: str,
	) -> GraphEndpointRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_endpoint import GraphEndpointRequest
		return GraphEndpointRequest(self.request_adapter, path_parameters)

	def graph_service_principal(self,
		application_id: str,
		directoryObject_id: str,
	) -> GraphServicePrincipalRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_service_principal import GraphServicePrincipalRequest
		return GraphServicePrincipalRequest(self.request_adapter, path_parameters)

	def graph_user(self,
		application_id: str,
		directoryObject_id: str,
	) -> GraphUserRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_user import GraphUserRequest
		return GraphUserRequest(self.request_adapter, path_parameters)

