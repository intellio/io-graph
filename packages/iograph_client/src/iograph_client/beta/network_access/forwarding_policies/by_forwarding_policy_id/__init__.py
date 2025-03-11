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
	from .policy_rules import PolicyRulesRequest
	from .networkaccess_update_policy_rules import NetworkaccessUpdatePolicyRulesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.networkaccess_forwarding_policy import NetworkaccessForwardingPolicy


class ByForwardingPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/forwardingPolicies/{forwardingPolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessForwardingPolicy:
		"""
		Get forwardingPolicy
		Retrieve information about a specific forwarding policy.
		Find more info here: https://learn.microsoft.com/graph/api/networkaccess-forwardingpolicy-get?view=graph-rest-beta
		"""
		tags = ['networkAccess.forwardingPolicy']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessForwardingPolicy, error_mapping)

	async def patch(
		self,
		body: NetworkaccessForwardingPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessForwardingPolicy:
		"""
		Update the navigation property forwardingPolicies in networkAccess
		
		"""
		tags = ['networkAccess.forwardingPolicy']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessForwardingPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property forwardingPolicies for networkAccess
		
		"""
		tags = ['networkAccess.forwardingPolicy']
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



	def with_url(self, raw_url: str) -> ByForwardingPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByForwardingPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByForwardingPolicyIdRequest(self.request_adapter, self.path_parameters)

	def networkaccess_update_policy_rules(self,
		forwardingPolicy_id: str,
	) -> NetworkaccessUpdatePolicyRulesRequest:
		if forwardingPolicy_id is None:
			raise TypeError("forwardingPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["forwardingPolicy%2Did"] =  forwardingPolicy_id

		from .networkaccess_update_policy_rules import NetworkaccessUpdatePolicyRulesRequest
		return NetworkaccessUpdatePolicyRulesRequest(self.request_adapter, path_parameters)

	def policy_rules(self,
		forwardingPolicy_id: str,
	) -> PolicyRulesRequest:
		if forwardingPolicy_id is None:
			raise TypeError("forwardingPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["forwardingPolicy%2Did"] =  forwardingPolicy_id

		from .policy_rules import PolicyRulesRequest
		return PolicyRulesRequest(self.request_adapter, path_parameters)

