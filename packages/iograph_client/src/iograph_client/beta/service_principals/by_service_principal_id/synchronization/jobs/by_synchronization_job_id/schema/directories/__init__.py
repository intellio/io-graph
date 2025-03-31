# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_directory_definition_id import ByDirectoryDefinitionIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.directory_definition_collection_response import DirectoryDefinitionCollectionResponse
from iograph_models.beta.directory_definition import DirectoryDefinition
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DirectoriesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/synchronization/jobs/{synchronizationJob%2Did}/schema/directories", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryDefinitionCollectionResponse:
		"""
		Get directories from servicePrincipals
		Contains the collection of directories and all of their objects.
		"""
		tags = ['servicePrincipals.synchronization']

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
		return await self.request_adapter.send_async(request_info, DirectoryDefinitionCollectionResponse, error_mapping)

	async def post(
		self,
		body: DirectoryDefinition,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DirectoryDefinition:
		"""
		Create new navigation property to directories for servicePrincipals
		
		"""
		tags = ['servicePrincipals.synchronization']

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
		return await self.request_adapter.send_async(request_info, DirectoryDefinition, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DirectoriesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DirectoriesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DirectoriesRequest(self.request_adapter, self.path_parameters)

	def by_directory_definition_id(self,
		servicePrincipal_id: str,
		synchronizationJob_id: str,
		directoryDefinition_id: str,
	) -> ByDirectoryDefinitionIdRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")
		if directoryDefinition_id is None:
			raise TypeError("directoryDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id
		path_parameters["directoryDefinition%2Did"] =  directoryDefinition_id

		from .by_directory_definition_id import ByDirectoryDefinitionIdRequest
		return ByDirectoryDefinitionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		servicePrincipal_id: str,
		synchronizationJob_id: str,
	) -> CountRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if synchronizationJob_id is None:
			raise TypeError("synchronizationJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["synchronizationJob%2Did"] =  synchronizationJob_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

