# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .validate_properties import ValidatePropertiesRequest
	from .graph_user import GraphUserRequest
	from .graph_service_principal import GraphServicePrincipalRequest
	from .graph_group import GraphGroupRequest
	from .get_by_ids import GetByIdsRequest
	from .get_available_extension_properties import GetAvailableExtensionPropertiesRequest
	from .graph_device import GraphDeviceRequest
	from .graph_application import GraphApplicationRequest
	from .graph_administrative_unit import GraphAdministrativeUnitRequest
	from .count import CountRequest
	from .by_directory_object_id import ByDirectoryObjectIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.directory_object_collection_response import DirectoryObjectCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class DeletedItemsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/deletedItems", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryObjectCollectionResponse:
		"""
		Get deleted item (directory object)
		Retrieve the properties of a recently deleted application, group, servicePrincipal, administrative unit, or user object from deleted items.
		"""
		tags = ['directory.directoryObject']

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

	def with_url(self, raw_url: str) -> DeletedItemsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeletedItemsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeletedItemsRequest(self.request_adapter, self.path_parameters)

	def by_directory_object_id(self,
		directoryObject_id: str,
	) -> ByDirectoryObjectIdRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .by_directory_object_id import ByDirectoryObjectIdRequest
		return ByDirectoryObjectIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_administrative_unit(self,
	) -> GraphAdministrativeUnitRequest:
		from .graph_administrative_unit import GraphAdministrativeUnitRequest
		return GraphAdministrativeUnitRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_application(self,
	) -> GraphApplicationRequest:
		from .graph_application import GraphApplicationRequest
		return GraphApplicationRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_device(self,
	) -> GraphDeviceRequest:
		from .graph_device import GraphDeviceRequest
		return GraphDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def get_available_extension_properties(self,
	) -> GetAvailableExtensionPropertiesRequest:
		from .get_available_extension_properties import GetAvailableExtensionPropertiesRequest
		return GetAvailableExtensionPropertiesRequest(self.request_adapter, self.path_parameters)

	@property
	def get_by_ids(self,
	) -> GetByIdsRequest:
		from .get_by_ids import GetByIdsRequest
		return GetByIdsRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_group(self,
	) -> GraphGroupRequest:
		from .graph_group import GraphGroupRequest
		return GraphGroupRequest(self.request_adapter, self.path_parameters)

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

	@property
	def validate_properties(self,
	) -> ValidatePropertiesRequest:
		from .validate_properties import ValidatePropertiesRequest
		return ValidatePropertiesRequest(self.request_adapter, self.path_parameters)

