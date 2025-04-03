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
	from .by_directory_setting_template_id import ByDirectorySettingTemplateIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.directory_setting_template_collection_response import DirectorySettingTemplateCollectionResponse
from iograph_models.beta.directory_setting_template import DirectorySettingTemplate


class DirectorySettingTemplatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directorySettingTemplates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectorySettingTemplateCollectionResponse:
		"""
		List directorySettingTemplates
		Directory setting templates represents a set of templates of directory settings, from which directory settings may be created and used within a tenant.  This operation retrieves the list of available directorySettingTemplates objects.
		Find more info here: https://learn.microsoft.com/graph/api/directorysettingtemplate-list?view=graph-rest-beta
		"""
		tags = ['directorySettingTemplates.directorySettingTemplate']

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
		return await self.request_adapter.send_async(request_info, DirectorySettingTemplateCollectionResponse, error_mapping)

	async def post(
		self,
		body: DirectorySettingTemplate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DirectorySettingTemplate:
		"""
		Add new entity to directorySettingTemplates
		
		"""
		tags = ['directorySettingTemplates.directorySettingTemplate']

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
		return await self.request_adapter.send_async(request_info, DirectorySettingTemplate, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DirectorySettingTemplatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DirectorySettingTemplatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DirectorySettingTemplatesRequest(self.request_adapter, self.path_parameters)

	def by_directory_setting_template_id(self,
		directorySettingTemplate_id: str,
	) -> ByDirectorySettingTemplateIdRequest:
		if directorySettingTemplate_id is None:
			raise TypeError("directorySettingTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directorySettingTemplate%2Did"] =  directorySettingTemplate_id

		from .by_directory_setting_template_id import ByDirectorySettingTemplateIdRequest
		return ByDirectorySettingTemplateIdRequest(self.request_adapter, path_parameters)

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

