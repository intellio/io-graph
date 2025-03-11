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
	from ......request_adapter import HttpxRequestAdapter


class ByDirectoryObjectIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/administrativeUnits/{administrativeUnit-id}/members/{directoryObject-id}", path_parameters)

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
		administrativeUnit_id: str,
		directoryObject_id: str,
	) -> RefRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

	def graph_application(self,
		administrativeUnit_id: str,
		directoryObject_id: str,
	) -> GraphApplicationRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_application import GraphApplicationRequest
		return GraphApplicationRequest(self.request_adapter, path_parameters)

	def graph_device(self,
		administrativeUnit_id: str,
		directoryObject_id: str,
	) -> GraphDeviceRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_device import GraphDeviceRequest
		return GraphDeviceRequest(self.request_adapter, path_parameters)

	def graph_group(self,
		administrativeUnit_id: str,
		directoryObject_id: str,
	) -> GraphGroupRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_group import GraphGroupRequest
		return GraphGroupRequest(self.request_adapter, path_parameters)

	def graph_org_contact(self,
		administrativeUnit_id: str,
		directoryObject_id: str,
	) -> GraphOrgContactRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_org_contact import GraphOrgContactRequest
		return GraphOrgContactRequest(self.request_adapter, path_parameters)

	def graph_service_principal(self,
		administrativeUnit_id: str,
		directoryObject_id: str,
	) -> GraphServicePrincipalRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_service_principal import GraphServicePrincipalRequest
		return GraphServicePrincipalRequest(self.request_adapter, path_parameters)

	def graph_user(self,
		administrativeUnit_id: str,
		directoryObject_id: str,
	) -> GraphUserRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_user import GraphUserRequest
		return GraphUserRequest(self.request_adapter, path_parameters)

