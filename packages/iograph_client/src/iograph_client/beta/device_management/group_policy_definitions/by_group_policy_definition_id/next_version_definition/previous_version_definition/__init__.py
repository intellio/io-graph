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
	from .presentations import PresentationsRequest
	from .definition_file import DefinitionFileRequest
	from .category import CategoryRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.group_policy_definition import GroupPolicyDefinition
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class PreviousVersionDefinitionRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/groupPolicyDefinitions/{groupPolicyDefinition%2Did}/nextVersionDefinition/previousVersionDefinition", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupPolicyDefinition:
		"""
		Get previousVersionDefinition from deviceManagement
		Definition of the previous version of this definition
		"""
		tags = ['deviceManagement.groupPolicyDefinition']

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
		return await self.request_adapter.send_async(request_info, GroupPolicyDefinition, error_mapping)

	async def patch(
		self,
		body: GroupPolicyDefinition,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GroupPolicyDefinition:
		"""
		Update the navigation property previousVersionDefinition in deviceManagement
		
		"""
		tags = ['deviceManagement.groupPolicyDefinition']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, GroupPolicyDefinition, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property previousVersionDefinition for deviceManagement
		
		"""
		tags = ['deviceManagement.groupPolicyDefinition']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> PreviousVersionDefinitionRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PreviousVersionDefinitionRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PreviousVersionDefinitionRequest(self.request_adapter, self.path_parameters)

	def category(self,
		groupPolicyDefinition_id: str,
	) -> CategoryRequest:
		if groupPolicyDefinition_id is None:
			raise TypeError("groupPolicyDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyDefinition%2Did"] =  groupPolicyDefinition_id

		from .category import CategoryRequest
		return CategoryRequest(self.request_adapter, path_parameters)

	def definition_file(self,
		groupPolicyDefinition_id: str,
	) -> DefinitionFileRequest:
		if groupPolicyDefinition_id is None:
			raise TypeError("groupPolicyDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyDefinition%2Did"] =  groupPolicyDefinition_id

		from .definition_file import DefinitionFileRequest
		return DefinitionFileRequest(self.request_adapter, path_parameters)

	def presentations(self,
		groupPolicyDefinition_id: str,
	) -> PresentationsRequest:
		if groupPolicyDefinition_id is None:
			raise TypeError("groupPolicyDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyDefinition%2Did"] =  groupPolicyDefinition_id

		from .presentations import PresentationsRequest
		return PresentationsRequest(self.request_adapter, path_parameters)

