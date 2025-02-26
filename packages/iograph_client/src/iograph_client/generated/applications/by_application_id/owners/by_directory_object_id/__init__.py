# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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


class ByDirectoryObjectIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/applications/{application-id}/owners/{directoryObject-id}"
		self.path_parameters: dict[str, Any] = path_parameters

	@property
	def ref(self,
	) -> RefRequest:
		from .ref import RefRequest
		return RefRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_app_role_assignment(self,
	) -> GraphAppRoleAssignmentRequest:
		from .graph_app_role_assignment import GraphAppRoleAssignmentRequest
		return GraphAppRoleAssignmentRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_endpoint(self,
	) -> GraphEndpointRequest:
		from .graph_endpoint import GraphEndpointRequest
		return GraphEndpointRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_service_principal(self,
	) -> GraphServicePrincipalRequest:
		from .graph_service_principal import GraphServicePrincipalRequest
		return GraphServicePrincipalRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_user(self,
	) -> GraphUserRequest:
		from .graph_user import GraphUserRequest
		return GraphUserRequest(self.request_adapter, self.path_parameters)

