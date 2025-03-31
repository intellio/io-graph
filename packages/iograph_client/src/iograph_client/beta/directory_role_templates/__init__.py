# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .validate_properties import ValidatePropertiesRequest
	from .get_user_owned_objects import GetUserOwnedObjectsRequest
	from .get_by_ids import GetByIdsRequest
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_directory_role_template_id import ByDirectoryRoleTemplateIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.directory_role_template_collection_response import DirectoryRoleTemplateCollectionResponse
from iograph_models.beta.directory_role_template import DirectoryRoleTemplate
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DirectoryRoleTemplatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directoryRoleTemplates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryRoleTemplateCollectionResponse:
		"""
		List directoryRoleTemplates
		Retrieve a list of directoryroletemplate objects.
		Find more info here: https://learn.microsoft.com/graph/api/directoryroletemplate-list?view=graph-rest-beta
		"""
		tags = ['directoryRoleTemplates.directoryRoleTemplate']

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
		return await self.request_adapter.send_async(request_info, DirectoryRoleTemplateCollectionResponse, error_mapping)

	async def post(
		self,
		body: DirectoryRoleTemplate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DirectoryRoleTemplate:
		"""
		Add new entity to directoryRoleTemplates
		
		"""
		tags = ['directoryRoleTemplates.directoryRoleTemplate']

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
		return await self.request_adapter.send_async(request_info, DirectoryRoleTemplate, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DirectoryRoleTemplatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DirectoryRoleTemplatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DirectoryRoleTemplatesRequest(self.request_adapter, self.path_parameters)

	def by_directory_role_template_id(self,
		directoryRoleTemplate_id: str,
	) -> ByDirectoryRoleTemplateIdRequest:
		if directoryRoleTemplate_id is None:
			raise TypeError("directoryRoleTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryRoleTemplate%2Did"] =  directoryRoleTemplate_id

		from .by_directory_role_template_id import ByDirectoryRoleTemplateIdRequest
		return ByDirectoryRoleTemplateIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def delta(self,
	) -> DeltaRequest:
		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, self.path_parameters)

	@property
	def get_by_ids(self,
	) -> GetByIdsRequest:
		from .get_by_ids import GetByIdsRequest
		return GetByIdsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_user_owned_objects(self,
	) -> GetUserOwnedObjectsRequest:
		from .get_user_owned_objects import GetUserOwnedObjectsRequest
		return GetUserOwnedObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def validate_properties(self,
	) -> ValidatePropertiesRequest:
		from .validate_properties import ValidatePropertiesRequest
		return ValidatePropertiesRequest(self.request_adapter, self.path_parameters)

