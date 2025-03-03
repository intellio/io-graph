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
	from .verification_dns_records import VerificationDnsRecordsRequest
	from .service_configuration_records import ServiceConfigurationRecordsRequest
	from .root_domain import RootDomainRequest
	from .verify import VerifyRequest
	from .promote import PromoteRequest
	from .force_delete import ForceDeleteRequest
	from .federation_configuration import FederationConfigurationRequest
	from .domain_name_references import DomainNameReferencesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.domain import Domain
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByDomainIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/domains/{domain%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Domain:
		"""
		Get domain
		Retrieve the properties and relationships of domain object.
		Find more info here: https://learn.microsoft.com/graph/api/domain-get?view=graph-rest-1.0
		"""
		tags = ['domains.domain']

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
		return await self.request_adapter.send_async(request_info, Domain, error_mapping)

	async def patch(
		self,
		body: Domain,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Domain:
		"""
		Update domain
		Update the properties of domain object. Only verified domains can be updated.
		Find more info here: https://learn.microsoft.com/graph/api/domain-update?view=graph-rest-1.0
		"""
		tags = ['domains.domain']

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
		return await self.request_adapter.send_async(request_info, Domain, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete domain
		Delete a domain from a tenant.
		Find more info here: https://learn.microsoft.com/graph/api/domain-delete?view=graph-rest-1.0
		"""
		tags = ['domains.domain']
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



	def with_url(self, raw_url: str) -> ByDomainIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDomainIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDomainIdRequest(self.request_adapter, self.path_parameters)

	@property
	def domain_name_references(self,
	) -> DomainNameReferencesRequest:
		from .domain_name_references import DomainNameReferencesRequest
		return DomainNameReferencesRequest(self.request_adapter, self.path_parameters)

	@property
	def federation_configuration(self,
	) -> FederationConfigurationRequest:
		from .federation_configuration import FederationConfigurationRequest
		return FederationConfigurationRequest(self.request_adapter, self.path_parameters)

	@property
	def force_delete(self,
	) -> ForceDeleteRequest:
		from .force_delete import ForceDeleteRequest
		return ForceDeleteRequest(self.request_adapter, self.path_parameters)

	@property
	def promote(self,
	) -> PromoteRequest:
		from .promote import PromoteRequest
		return PromoteRequest(self.request_adapter, self.path_parameters)

	@property
	def verify(self,
	) -> VerifyRequest:
		from .verify import VerifyRequest
		return VerifyRequest(self.request_adapter, self.path_parameters)

	@property
	def root_domain(self,
	) -> RootDomainRequest:
		from .root_domain import RootDomainRequest
		return RootDomainRequest(self.request_adapter, self.path_parameters)

	@property
	def service_configuration_records(self,
	) -> ServiceConfigurationRecordsRequest:
		from .service_configuration_records import ServiceConfigurationRecordsRequest
		return ServiceConfigurationRecordsRequest(self.request_adapter, self.path_parameters)

	@property
	def verification_dns_records(self,
	) -> VerificationDnsRecordsRequest:
		from .verification_dns_records import VerificationDnsRecordsRequest
		return VerificationDnsRecordsRequest(self.request_adapter, self.path_parameters)

