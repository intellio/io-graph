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
	from .ref import RefRequest
	from .count import CountRequest
	from .by_home_realm_discovery_policy_id import ByHomeRealmDiscoveryPolicyIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.home_realm_discovery_policy_collection_response import HomeRealmDiscoveryPolicyCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class HomeRealmDiscoveryPoliciesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/homeRealmDiscoveryPolicies", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> HomeRealmDiscoveryPolicyCollectionResponse:
		"""
		List assigned homeRealmDiscoveryPolicy
		List the homeRealmDiscoveryPolicy objects that are assigned to a servicePrincipal.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-list-homerealmdiscoverypolicies?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.homeRealmDiscoveryPolicy']

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
		return await self.request_adapter.send_async(request_info, HomeRealmDiscoveryPolicyCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> HomeRealmDiscoveryPoliciesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: HomeRealmDiscoveryPoliciesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return HomeRealmDiscoveryPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def by_home_realm_discovery_policy_id(self,
	) -> ByHomeRealmDiscoveryPolicyIdRequest:
		from .by_home_realm_discovery_policy_id import ByHomeRealmDiscoveryPolicyIdRequest
		return ByHomeRealmDiscoveryPolicyIdRequest(self.request_adapter, self.path_parameters)

	def count(self,
		servicePrincipal_id: str,
	) -> CountRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def ref(self,
		servicePrincipal_id: str,
	) -> RefRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

