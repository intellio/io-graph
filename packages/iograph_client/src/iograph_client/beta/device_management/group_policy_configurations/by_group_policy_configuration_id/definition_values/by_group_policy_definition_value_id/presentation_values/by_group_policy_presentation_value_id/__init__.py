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
	from .presentation import PresentationRequest
	from .definition_value import DefinitionValueRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.group_policy_presentation_value import GroupPolicyPresentationValue


class ByGroupPolicyPresentationValueIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/groupPolicyConfigurations/{groupPolicyConfiguration%2Did}/definitionValues/{groupPolicyDefinitionValue%2Did}/presentationValues/{groupPolicyPresentationValue%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupPolicyPresentationValue:
		"""
		Get presentationValues from deviceManagement
		The associated group policy presentation values with the definition value.
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
		return await self.request_adapter.send_async(request_info, GroupPolicyPresentationValue, error_mapping)

	async def patch(
		self,
		body: GroupPolicyPresentationValue,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GroupPolicyPresentationValue:
		"""
		Update the navigation property presentationValues in deviceManagement
		
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
		return await self.request_adapter.send_async(request_info, GroupPolicyPresentationValue, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property presentationValues for deviceManagement
		
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



	def with_url(self, raw_url: str) -> ByGroupPolicyPresentationValueIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGroupPolicyPresentationValueIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGroupPolicyPresentationValueIdRequest(self.request_adapter, self.path_parameters)

	def definition_value(self,
		groupPolicyConfiguration_id: str,
		groupPolicyDefinitionValue_id: str,
		groupPolicyPresentationValue_id: str,
	) -> DefinitionValueRequest:
		if groupPolicyConfiguration_id is None:
			raise TypeError("groupPolicyConfiguration_id cannot be null.")
		if groupPolicyDefinitionValue_id is None:
			raise TypeError("groupPolicyDefinitionValue_id cannot be null.")
		if groupPolicyPresentationValue_id is None:
			raise TypeError("groupPolicyPresentationValue_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyConfiguration%2Did"] =  groupPolicyConfiguration_id
		path_parameters["groupPolicyDefinitionValue%2Did"] =  groupPolicyDefinitionValue_id
		path_parameters["groupPolicyPresentationValue%2Did"] =  groupPolicyPresentationValue_id

		from .definition_value import DefinitionValueRequest
		return DefinitionValueRequest(self.request_adapter, path_parameters)

	def presentation(self,
		groupPolicyConfiguration_id: str,
		groupPolicyDefinitionValue_id: str,
		groupPolicyPresentationValue_id: str,
	) -> PresentationRequest:
		if groupPolicyConfiguration_id is None:
			raise TypeError("groupPolicyConfiguration_id cannot be null.")
		if groupPolicyDefinitionValue_id is None:
			raise TypeError("groupPolicyDefinitionValue_id cannot be null.")
		if groupPolicyPresentationValue_id is None:
			raise TypeError("groupPolicyPresentationValue_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyConfiguration%2Did"] =  groupPolicyConfiguration_id
		path_parameters["groupPolicyDefinitionValue%2Did"] =  groupPolicyDefinitionValue_id
		path_parameters["groupPolicyPresentationValue%2Did"] =  groupPolicyPresentationValue_id

		from .presentation import PresentationRequest
		return PresentationRequest(self.request_adapter, path_parameters)

