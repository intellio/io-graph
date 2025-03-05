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
	from .whois_records import WhoisRecordsRequest
	from .whois_history_records import WhoisHistoryRecordsRequest
	from .vulnerabilities import VulnerabilitiesRequest
	from .subdomains import SubdomainsRequest
	from .ssl_certificates import SslCertificatesRequest
	from .passive_dns_records import PassiveDnsRecordsRequest
	from .intel_profiles import IntelProfilesRequest
	from .intelligence_profile_indicators import IntelligenceProfileIndicatorsRequest
	from .host_trackers import HostTrackersRequest
	from .host_ssl_certificates import HostSslCertificatesRequest
	from .hosts import HostsRequest
	from .host_ports import HostPortsRequest
	from .host_pairs import HostPairsRequest
	from .host_cookies import HostCookiesRequest
	from .host_components import HostComponentsRequest
	from .articles import ArticlesRequest
	from .article_indicators import ArticleIndicatorsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.security_threat_intelligence import SecurityThreatIntelligence


class ThreatIntelligenceRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/threatIntelligence", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityThreatIntelligence:
		"""
		Get threatIntelligence from security
		
		"""
		tags = ['security.threatIntelligence']

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
		return await self.request_adapter.send_async(request_info, SecurityThreatIntelligence, error_mapping)

	async def patch(
		self,
		body: SecurityThreatIntelligence,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityThreatIntelligence:
		"""
		Update the navigation property threatIntelligence in security
		
		"""
		tags = ['security.threatIntelligence']

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
		return await self.request_adapter.send_async(request_info, SecurityThreatIntelligence, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property threatIntelligence for security
		
		"""
		tags = ['security.threatIntelligence']
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



	def with_url(self, raw_url: str) -> ThreatIntelligenceRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ThreatIntelligenceRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ThreatIntelligenceRequest(self.request_adapter, self.path_parameters)

	@property
	def article_indicators(self,
	) -> ArticleIndicatorsRequest:
		from .article_indicators import ArticleIndicatorsRequest
		return ArticleIndicatorsRequest(self.request_adapter, self.path_parameters)

	@property
	def articles(self,
	) -> ArticlesRequest:
		from .articles import ArticlesRequest
		return ArticlesRequest(self.request_adapter, self.path_parameters)

	@property
	def host_components(self,
	) -> HostComponentsRequest:
		from .host_components import HostComponentsRequest
		return HostComponentsRequest(self.request_adapter, self.path_parameters)

	@property
	def host_cookies(self,
	) -> HostCookiesRequest:
		from .host_cookies import HostCookiesRequest
		return HostCookiesRequest(self.request_adapter, self.path_parameters)

	@property
	def host_pairs(self,
	) -> HostPairsRequest:
		from .host_pairs import HostPairsRequest
		return HostPairsRequest(self.request_adapter, self.path_parameters)

	@property
	def host_ports(self,
	) -> HostPortsRequest:
		from .host_ports import HostPortsRequest
		return HostPortsRequest(self.request_adapter, self.path_parameters)

	@property
	def hosts(self,
	) -> HostsRequest:
		from .hosts import HostsRequest
		return HostsRequest(self.request_adapter, self.path_parameters)

	@property
	def host_ssl_certificates(self,
	) -> HostSslCertificatesRequest:
		from .host_ssl_certificates import HostSslCertificatesRequest
		return HostSslCertificatesRequest(self.request_adapter, self.path_parameters)

	@property
	def host_trackers(self,
	) -> HostTrackersRequest:
		from .host_trackers import HostTrackersRequest
		return HostTrackersRequest(self.request_adapter, self.path_parameters)

	@property
	def intelligence_profile_indicators(self,
	) -> IntelligenceProfileIndicatorsRequest:
		from .intelligence_profile_indicators import IntelligenceProfileIndicatorsRequest
		return IntelligenceProfileIndicatorsRequest(self.request_adapter, self.path_parameters)

	@property
	def intel_profiles(self,
	) -> IntelProfilesRequest:
		from .intel_profiles import IntelProfilesRequest
		return IntelProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def passive_dns_records(self,
	) -> PassiveDnsRecordsRequest:
		from .passive_dns_records import PassiveDnsRecordsRequest
		return PassiveDnsRecordsRequest(self.request_adapter, self.path_parameters)

	@property
	def ssl_certificates(self,
	) -> SslCertificatesRequest:
		from .ssl_certificates import SslCertificatesRequest
		return SslCertificatesRequest(self.request_adapter, self.path_parameters)

	@property
	def subdomains(self,
	) -> SubdomainsRequest:
		from .subdomains import SubdomainsRequest
		return SubdomainsRequest(self.request_adapter, self.path_parameters)

	@property
	def vulnerabilities(self,
	) -> VulnerabilitiesRequest:
		from .vulnerabilities import VulnerabilitiesRequest
		return VulnerabilitiesRequest(self.request_adapter, self.path_parameters)

	@property
	def whois_history_records(self,
	) -> WhoisHistoryRecordsRequest:
		from .whois_history_records import WhoisHistoryRecordsRequest
		return WhoisHistoryRecordsRequest(self.request_adapter, self.path_parameters)

	@property
	def whois_records(self,
	) -> WhoisRecordsRequest:
		from .whois_records import WhoisRecordsRequest
		return WhoisRecordsRequest(self.request_adapter, self.path_parameters)

