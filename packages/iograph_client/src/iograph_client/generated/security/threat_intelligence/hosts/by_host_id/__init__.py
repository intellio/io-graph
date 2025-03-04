# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .whois import WhoisRequest
	from .trackers import TrackersRequest
	from .subdomains import SubdomainsRequest
	from .ssl_certificates import SslCertificatesRequest
	from .reputation import ReputationRequest
	from .ports import PortsRequest
	from .passive_dns_reverse import PassiveDnsReverseRequest
	from .passive_dns import PassiveDnsRequest
	from .parent_host_pairs import ParentHostPairsRequest
	from .host_pairs import HostPairsRequest
	from .cookies import CookiesRequest
	from .components import ComponentsRequest
	from .child_host_pairs import ChildHostPairsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.security_host import SecurityHost
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByHostIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/threatIntelligence/hosts/{host%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityHost:
		"""
		Get host
		Read the properties and relationships of a host object. The host resource is the abstract base type that returns an implementation. A host can be of one of the following types:
		Find more info here: https://learn.microsoft.com/graph/api/security-host-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, SecurityHost, error_mapping)

	async def patch(
		self,
		body: SecurityHost,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityHost:
		"""
		Update the navigation property hosts in security
		
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
		return await self.request_adapter.send_async(request_info, SecurityHost, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property hosts for security
		
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



	def with_url(self, raw_url: str) -> ByHostIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByHostIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByHostIdRequest(self.request_adapter, self.path_parameters)

	def child_host_pairs(self,
		host_id: str,
	) -> ChildHostPairsRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .child_host_pairs import ChildHostPairsRequest
		return ChildHostPairsRequest(self.request_adapter, path_parameters)

	def components(self,
		host_id: str,
	) -> ComponentsRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .components import ComponentsRequest
		return ComponentsRequest(self.request_adapter, path_parameters)

	def cookies(self,
		host_id: str,
	) -> CookiesRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .cookies import CookiesRequest
		return CookiesRequest(self.request_adapter, path_parameters)

	def host_pairs(self,
		host_id: str,
	) -> HostPairsRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .host_pairs import HostPairsRequest
		return HostPairsRequest(self.request_adapter, path_parameters)

	def parent_host_pairs(self,
		host_id: str,
	) -> ParentHostPairsRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .parent_host_pairs import ParentHostPairsRequest
		return ParentHostPairsRequest(self.request_adapter, path_parameters)

	def passive_dns(self,
		host_id: str,
	) -> PassiveDnsRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .passive_dns import PassiveDnsRequest
		return PassiveDnsRequest(self.request_adapter, path_parameters)

	def passive_dns_reverse(self,
		host_id: str,
	) -> PassiveDnsReverseRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .passive_dns_reverse import PassiveDnsReverseRequest
		return PassiveDnsReverseRequest(self.request_adapter, path_parameters)

	def ports(self,
		host_id: str,
	) -> PortsRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .ports import PortsRequest
		return PortsRequest(self.request_adapter, path_parameters)

	def reputation(self,
		host_id: str,
	) -> ReputationRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .reputation import ReputationRequest
		return ReputationRequest(self.request_adapter, path_parameters)

	def ssl_certificates(self,
		host_id: str,
	) -> SslCertificatesRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .ssl_certificates import SslCertificatesRequest
		return SslCertificatesRequest(self.request_adapter, path_parameters)

	def subdomains(self,
		host_id: str,
	) -> SubdomainsRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .subdomains import SubdomainsRequest
		return SubdomainsRequest(self.request_adapter, path_parameters)

	def trackers(self,
		host_id: str,
	) -> TrackersRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .trackers import TrackersRequest
		return TrackersRequest(self.request_adapter, path_parameters)

	def whois(self,
		host_id: str,
	) -> WhoisRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .whois import WhoisRequest
		return WhoisRequest(self.request_adapter, path_parameters)

