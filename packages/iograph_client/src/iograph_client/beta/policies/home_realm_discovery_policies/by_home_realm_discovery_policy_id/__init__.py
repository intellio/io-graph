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
	from .applies_to import AppliesToRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.home_realm_discovery_policy import HomeRealmDiscoveryPolicy


class ByHomeRealmDiscoveryPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/policies/homeRealmDiscoveryPolicies/{homeRealmDiscoveryPolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> HomeRealmDiscoveryPolicy:
		"""
		Get homeRealmDiscoveryPolicy
		Retrieve the properties and relationships of a homeRealmDiscoveryPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/homerealmdiscoverypolicy-get?view=graph-rest-beta
		"""
		tags = ['policies.homeRealmDiscoveryPolicy']

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
		return await self.request_adapter.send_async(request_info, HomeRealmDiscoveryPolicy, error_mapping)

	async def patch(
		self,
		body: HomeRealmDiscoveryPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> HomeRealmDiscoveryPolicy:
		"""
		Update homerealmdiscoverypolicy
		Update the properties of a homeRealmDiscoveryPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/homerealmdiscoverypolicy-update?view=graph-rest-beta
		"""
		tags = ['policies.homeRealmDiscoveryPolicy']

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
		return await self.request_adapter.send_async(request_info, HomeRealmDiscoveryPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete homeRealmDiscoveryPolicy
		Delete a homeRealmDiscoveryPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/homerealmdiscoverypolicy-delete?view=graph-rest-beta
		"""
		tags = ['policies.homeRealmDiscoveryPolicy']
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



	def with_url(self, raw_url: str) -> ByHomeRealmDiscoveryPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByHomeRealmDiscoveryPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByHomeRealmDiscoveryPolicyIdRequest(self.request_adapter, self.path_parameters)

	def applies_to(self,
		homeRealmDiscoveryPolicy_id: str,
	) -> AppliesToRequest:
		if homeRealmDiscoveryPolicy_id is None:
			raise TypeError("homeRealmDiscoveryPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["homeRealmDiscoveryPolicy%2Did"] =  homeRealmDiscoveryPolicy_id

		from .applies_to import AppliesToRequest
		return AppliesToRequest(self.request_adapter, path_parameters)

