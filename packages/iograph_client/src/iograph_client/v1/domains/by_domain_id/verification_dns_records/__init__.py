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
	from .count import CountRequest
	from .by_domain_dns_record_id import ByDomainDnsRecordIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.domain_dns_record_collection_response import DomainDnsRecordCollectionResponse
from iograph_models.v1.domain_dns_record import DomainDnsRecord
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class VerificationDnsRecordsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/domains/{domain%2Did}/verificationDnsRecords", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DomainDnsRecordCollectionResponse:
		"""
		List verificationDnsRecords
		Retrieve a list of domainDnsRecord objects. You cannot use an associated domain with your Microsoft Entra tenant until ownership is verified. To verify the ownership of the domain, retrieve the domain verification records and add the details to the zone file of the domain. This can be done through the domain registrar or DNS server configuration. Root domains require verification. For example, contoso.com requires verification. If a root domain is verified, subdomains of the root domain are automatically verified. For example, subdomain.contoso.com is automatically be verified if contoso.com has been verified.
		Find more info here: https://learn.microsoft.com/graph/api/domain-list-verificationdnsrecords?view=graph-rest-1.0
		"""
		tags = ['domains.domainDnsRecord']

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
		return await self.request_adapter.send_async(request_info, DomainDnsRecordCollectionResponse, error_mapping)

	async def post(
		self,
		body: DomainDnsRecord,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DomainDnsRecord:
		"""
		Create new navigation property to verificationDnsRecords for domains
		
		"""
		tags = ['domains.domainDnsRecord']

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
		return await self.request_adapter.send_async(request_info, DomainDnsRecord, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> VerificationDnsRecordsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: VerificationDnsRecordsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return VerificationDnsRecordsRequest(self.request_adapter, self.path_parameters)

	def by_domain_dns_record_id(self,
		domain_id: str,
		domainDnsRecord_id: str,
	) -> ByDomainDnsRecordIdRequest:
		if domain_id is None:
			raise TypeError("domain_id cannot be null.")
		if domainDnsRecord_id is None:
			raise TypeError("domainDnsRecord_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["domain%2Did"] =  domain_id
		path_parameters["domainDnsRecord%2Did"] =  domainDnsRecord_id

		from .by_domain_dns_record_id import ByDomainDnsRecordIdRequest
		return ByDomainDnsRecordIdRequest(self.request_adapter, path_parameters)

	def count(self,
		domain_id: str,
	) -> CountRequest:
		if domain_id is None:
			raise TypeError("domain_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["domain%2Did"] =  domain_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

