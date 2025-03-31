# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .update_definition_values import UpdateDefinitionValuesRequest
	from .assign import AssignRequest
	from .definition_values import DefinitionValuesRequest
	from .assignments import AssignmentsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.group_policy_configuration import GroupPolicyConfiguration
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByGroupPolicyConfigurationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/groupPolicyConfigurations/{groupPolicyConfiguration%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupPolicyConfiguration:
		"""
		Get groupPolicyConfigurations from deviceManagement
		The group policy configurations created by this account.
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
		return await self.request_adapter.send_async(request_info, GroupPolicyConfiguration, error_mapping)

	async def patch(
		self,
		body: GroupPolicyConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GroupPolicyConfiguration:
		"""
		Update the navigation property groupPolicyConfigurations in deviceManagement
		
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
		return await self.request_adapter.send_async(request_info, GroupPolicyConfiguration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property groupPolicyConfigurations for deviceManagement
		
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



	def with_url(self, raw_url: str) -> ByGroupPolicyConfigurationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGroupPolicyConfigurationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGroupPolicyConfigurationIdRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		groupPolicyConfiguration_id: str,
	) -> AssignmentsRequest:
		if groupPolicyConfiguration_id is None:
			raise TypeError("groupPolicyConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyConfiguration%2Did"] =  groupPolicyConfiguration_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def definition_values(self,
		groupPolicyConfiguration_id: str,
	) -> DefinitionValuesRequest:
		if groupPolicyConfiguration_id is None:
			raise TypeError("groupPolicyConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyConfiguration%2Did"] =  groupPolicyConfiguration_id

		from .definition_values import DefinitionValuesRequest
		return DefinitionValuesRequest(self.request_adapter, path_parameters)

	def assign(self,
		groupPolicyConfiguration_id: str,
	) -> AssignRequest:
		if groupPolicyConfiguration_id is None:
			raise TypeError("groupPolicyConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyConfiguration%2Did"] =  groupPolicyConfiguration_id

		from .assign import AssignRequest
		return AssignRequest(self.request_adapter, path_parameters)

	def update_definition_values(self,
		groupPolicyConfiguration_id: str,
	) -> UpdateDefinitionValuesRequest:
		if groupPolicyConfiguration_id is None:
			raise TypeError("groupPolicyConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupPolicyConfiguration%2Did"] =  groupPolicyConfiguration_id

		from .update_definition_values import UpdateDefinitionValuesRequest
		return UpdateDefinitionValuesRequest(self.request_adapter, path_parameters)

