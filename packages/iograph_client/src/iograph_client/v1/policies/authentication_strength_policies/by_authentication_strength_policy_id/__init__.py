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
	from .usage import UsageRequest
	from .update_allowed_combinations import UpdateAllowedCombinationsRequest
	from .combination_configurations import CombinationConfigurationsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.authentication_strength_policy import AuthenticationStrengthPolicy
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByAuthenticationStrengthPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/policies/authenticationStrengthPolicies/{authenticationStrengthPolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AuthenticationStrengthPolicy:
		"""
		Get authenticationStrengthPolicy
		Read the properties and relationships of an authenticationStrengthPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/authenticationstrengthpolicy-get?view=graph-rest-1.0
		"""
		tags = ['policies.authenticationStrengthPolicy']

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
		return await self.request_adapter.send_async(request_info, AuthenticationStrengthPolicy, error_mapping)

	async def patch(
		self,
		body: AuthenticationStrengthPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AuthenticationStrengthPolicy:
		"""
		Update authenticationStrengthPolicy
		Update the properties of an authenticationStrengthPolicy object. You cannot update the allowed auth method combinations using this request. To do so, use the Update allowed combinations action.
		Find more info here: https://learn.microsoft.com/graph/api/authenticationstrengthpolicy-update?view=graph-rest-1.0
		"""
		tags = ['policies.authenticationStrengthPolicy']

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
		return await self.request_adapter.send_async(request_info, AuthenticationStrengthPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete authenticationStrengthPolicy
		Delete a custom authenticationStrengthPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/authenticationstrengthroot-delete-policies?view=graph-rest-1.0
		"""
		tags = ['policies.authenticationStrengthPolicy']
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



	def with_url(self, raw_url: str) -> ByAuthenticationStrengthPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAuthenticationStrengthPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAuthenticationStrengthPolicyIdRequest(self.request_adapter, self.path_parameters)

	def combination_configurations(self,
		authenticationStrengthPolicy_id: str,
	) -> CombinationConfigurationsRequest:
		if authenticationStrengthPolicy_id is None:
			raise TypeError("authenticationStrengthPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationStrengthPolicy%2Did"] =  authenticationStrengthPolicy_id

		from .combination_configurations import CombinationConfigurationsRequest
		return CombinationConfigurationsRequest(self.request_adapter, path_parameters)

	def update_allowed_combinations(self,
		authenticationStrengthPolicy_id: str,
	) -> UpdateAllowedCombinationsRequest:
		if authenticationStrengthPolicy_id is None:
			raise TypeError("authenticationStrengthPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationStrengthPolicy%2Did"] =  authenticationStrengthPolicy_id

		from .update_allowed_combinations import UpdateAllowedCombinationsRequest
		return UpdateAllowedCombinationsRequest(self.request_adapter, path_parameters)

	def usage(self,
		authenticationStrengthPolicy_id: str,
	) -> UsageRequest:
		if authenticationStrengthPolicy_id is None:
			raise TypeError("authenticationStrengthPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationStrengthPolicy%2Did"] =  authenticationStrengthPolicy_id

		from .usage import UsageRequest
		return UsageRequest(self.request_adapter, path_parameters)

