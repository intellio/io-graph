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
	from .presentation_values import PresentationValuesRequest
	from .definition import DefinitionRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.group_policy_definition_value import GroupPolicyDefinitionValue
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByGroupPolicyDefinitionValueIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/groupPolicyConfigurations/{groupPolicyConfiguration%2Did}/definitionValues/{groupPolicyDefinitionValue%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupPolicyDefinitionValue:
		"""
		Get definitionValues from deviceManagement
		The list of enabled or disabled group policy definition values for the configuration.
		"""
		tags = ['deviceManagement.groupPolicyConfiguration']

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
		return await self.request_adapter.send_async(request_info, GroupPolicyDefinitionValue, error_mapping)

	async def patch(
		self,
		body: GroupPolicyDefinitionValue,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GroupPolicyDefinitionValue:
		"""
		Update the navigation property definitionValues in deviceManagement
		
		"""
		tags = ['deviceManagement.groupPolicyConfiguration']

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
		return await self.request_adapter.send_async(request_info, GroupPolicyDefinitionValue, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property definitionValues for deviceManagement
		
		"""
		tags = ['deviceManagement.groupPolicyConfiguration']
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



	def with_url(self, raw_url: str) -> ByGroupPolicyDefinitionValueIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGroupPolicyDefinitionValueIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGroupPolicyDefinitionValueIdRequest(self.request_adapter, self.path_parameters)

	def definition(self,
		groupPolicyConfiguration_id: str,
		groupPolicyDefinitionValue_id: str,
	) -> DefinitionRequest:
		if groupPolicyConfiguration_id is None:
			raise TypeError("groupPolicyConfiguration_id cannot be null.")
		if groupPolicyDefinitionValue_id is None:
			raise TypeError("groupPolicyDefinitionValue_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyConfiguration%2Did"] =  groupPolicyConfiguration_id
		path_parameters["groupPolicyDefinitionValue%2Did"] =  groupPolicyDefinitionValue_id

		from .definition import DefinitionRequest
		return DefinitionRequest(self.request_adapter, path_parameters)

	def presentation_values(self,
		groupPolicyConfiguration_id: str,
		groupPolicyDefinitionValue_id: str,
	) -> PresentationValuesRequest:
		if groupPolicyConfiguration_id is None:
			raise TypeError("groupPolicyConfiguration_id cannot be null.")
		if groupPolicyDefinitionValue_id is None:
			raise TypeError("groupPolicyDefinitionValue_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyConfiguration%2Did"] =  groupPolicyConfiguration_id
		path_parameters["groupPolicyDefinitionValue%2Did"] =  groupPolicyDefinitionValue_id

		from .presentation_values import PresentationValuesRequest
		return PresentationValuesRequest(self.request_adapter, path_parameters)

