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
	from .includes import IncludesRequest
	from .excludes import ExcludesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.service_principal_creation_policy import ServicePrincipalCreationPolicy
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByServicePrincipalCreationPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/policies/servicePrincipalCreationPolicies/{servicePrincipalCreationPolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ServicePrincipalCreationPolicy:
		"""
		Get servicePrincipalCreationPolicies from policies
		
		"""
		tags = ['policies.servicePrincipalCreationPolicy']

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
		return await self.request_adapter.send_async(request_info, ServicePrincipalCreationPolicy, error_mapping)

	async def patch(
		self,
		body: ServicePrincipalCreationPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ServicePrincipalCreationPolicy:
		"""
		Update the navigation property servicePrincipalCreationPolicies in policies
		
		"""
		tags = ['policies.servicePrincipalCreationPolicy']

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
		return await self.request_adapter.send_async(request_info, ServicePrincipalCreationPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property servicePrincipalCreationPolicies for policies
		
		"""
		tags = ['policies.servicePrincipalCreationPolicy']
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



	def with_url(self, raw_url: str) -> ByServicePrincipalCreationPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByServicePrincipalCreationPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByServicePrincipalCreationPolicyIdRequest(self.request_adapter, self.path_parameters)

	def excludes(self,
		servicePrincipalCreationPolicy_id: str,
	) -> ExcludesRequest:
		if servicePrincipalCreationPolicy_id is None:
			raise TypeError("servicePrincipalCreationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipalCreationPolicy%2Did"] =  servicePrincipalCreationPolicy_id

		from .excludes import ExcludesRequest
		return ExcludesRequest(self.request_adapter, path_parameters)

	def includes(self,
		servicePrincipalCreationPolicy_id: str,
	) -> IncludesRequest:
		if servicePrincipalCreationPolicy_id is None:
			raise TypeError("servicePrincipalCreationPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipalCreationPolicy%2Did"] =  servicePrincipalCreationPolicy_id

		from .includes import IncludesRequest
		return IncludesRequest(self.request_adapter, path_parameters)

