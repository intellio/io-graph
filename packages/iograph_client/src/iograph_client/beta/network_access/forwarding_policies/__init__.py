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
	from .count import CountRequest
	from .by_forwarding_policy_id import ByForwardingPolicyIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.networkaccess_forwarding_policy_collection_response import NetworkaccessForwardingPolicyCollectionResponse
from iograph_models.beta.networkaccess_forwarding_policy import NetworkaccessForwardingPolicy
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ForwardingPoliciesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/forwardingPolicies", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessForwardingPolicyCollectionResponse:
		"""
		List forwardingPolicies
		Retrieve a list of forwarding policies associated with a specific traffic forwarding profile.
		Find more info here: https://learn.microsoft.com/graph/api/networkaccess-networkaccessroot-list-forwardingpolicies?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, NetworkaccessForwardingPolicyCollectionResponse, error_mapping)

	async def post(
		self,
		body: NetworkaccessForwardingPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessForwardingPolicy:
		"""
		Create new navigation property to forwardingPolicies for networkAccess
		
		"""
		tags = ['networkAccess.forwardingPolicy']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessForwardingPolicy, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ForwardingPoliciesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ForwardingPoliciesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ForwardingPoliciesRequest(self.request_adapter, self.path_parameters)

	def by_forwarding_policy_id(self,
		forwardingPolicy_id: str,
	) -> ByForwardingPolicyIdRequest:
		if forwardingPolicy_id is None:
			raise TypeError("forwardingPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["forwardingPolicy%2Did"] =  forwardingPolicy_id

		from .by_forwarding_policy_id import ByForwardingPolicyIdRequest
		return ByForwardingPolicyIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

