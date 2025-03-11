# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .graph_user import GraphUserRequest
	from .graph_service_principal import GraphServicePrincipalRequest
	from .graph_endpoint import GraphEndpointRequest
	from .graph_app_role_assignment import GraphAppRoleAssignmentRequest
	from .ref import RefRequest
	from .count import CountRequest
	from .by_directory_object_id import ByDirectoryObjectIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.directory_object_collection_response import DirectoryObjectCollectionResponse


class RegisteredOwnersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/devices/{device%2Did}/registeredOwners", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryObjectCollectionResponse:
		"""
		Get registeredOwners from users
		The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Read-only. Nullable. Supports $expand.
		"""
		tags = ['users.device']
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

	def with_url(self, raw_url: str) -> RegisteredOwnersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RegisteredOwnersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RegisteredOwnersRequest(self.request_adapter, self.path_parameters)

	@property
	def by_directory_object_id(self,
	) -> ByDirectoryObjectIdRequest:
		from .by_directory_object_id import ByDirectoryObjectIdRequest
		return ByDirectoryObjectIdRequest(self.request_adapter, self.path_parameters)

	def count(self,
		user_id: str,
		device_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def ref(self,
		user_id: str,
		device_id: str,
	) -> RefRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

	def graph_app_role_assignment(self,
		user_id: str,
		device_id: str,
	) -> GraphAppRoleAssignmentRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .graph_app_role_assignment import GraphAppRoleAssignmentRequest
		return GraphAppRoleAssignmentRequest(self.request_adapter, path_parameters)

	def graph_endpoint(self,
		user_id: str,
		device_id: str,
	) -> GraphEndpointRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .graph_endpoint import GraphEndpointRequest
		return GraphEndpointRequest(self.request_adapter, path_parameters)

	def graph_service_principal(self,
		user_id: str,
		device_id: str,
	) -> GraphServicePrincipalRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .graph_service_principal import GraphServicePrincipalRequest
		return GraphServicePrincipalRequest(self.request_adapter, path_parameters)

	def graph_user(self,
		user_id: str,
		device_id: str,
	) -> GraphUserRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if device_id is None:
			raise TypeError("device_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["device%2Did"] =  device_id

		from .graph_user import GraphUserRequest
		return GraphUserRequest(self.request_adapter, path_parameters)

