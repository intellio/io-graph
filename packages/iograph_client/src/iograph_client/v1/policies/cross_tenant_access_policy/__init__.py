# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .templates import TemplatesRequest
	from .partners import PartnersRequest
	from .default import DefaultRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.cross_tenant_access_policy import CrossTenantAccessPolicy
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class CrossTenantAccessPolicyRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/policies/crossTenantAccessPolicy", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CrossTenantAccessPolicy:
		"""
		Get crossTenantAccessPolicy
		Read the properties and relationships of a crossTenantAccessPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/crosstenantaccesspolicy-get?view=graph-rest-1.0
		"""
		tags = ['policies.crossTenantAccessPolicy']

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
		return await self.request_adapter.send_async(request_info, CrossTenantAccessPolicy, error_mapping)

	async def patch(
		self,
		body: CrossTenantAccessPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CrossTenantAccessPolicy:
		"""
		Update crossTenantAccessPolicy
		Update the properties of a cross-tenant access policy.
		Find more info here: https://learn.microsoft.com/graph/api/crosstenantaccesspolicy-update?view=graph-rest-1.0
		"""
		tags = ['policies.crossTenantAccessPolicy']

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
		return await self.request_adapter.send_async(request_info, CrossTenantAccessPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property crossTenantAccessPolicy for policies
		
		"""
		tags = ['policies.crossTenantAccessPolicy']
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



	def with_url(self, raw_url: str) -> CrossTenantAccessPolicyRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CrossTenantAccessPolicyRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CrossTenantAccessPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def default(self,
	) -> DefaultRequest:
		from .default import DefaultRequest
		return DefaultRequest(self.request_adapter, self.path_parameters)

	@property
	def partners(self,
	) -> PartnersRequest:
		from .partners import PartnersRequest
		return PartnersRequest(self.request_adapter, self.path_parameters)

	@property
	def templates(self,
	) -> TemplatesRequest:
		from .templates import TemplatesRequest
		return TemplatesRequest(self.request_adapter, self.path_parameters)

