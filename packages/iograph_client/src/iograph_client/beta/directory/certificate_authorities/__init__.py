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
	from .mutual_tls_oauth_configurations import MutualTlsOauthConfigurationsRequest
	from .certificate_based_application_configurations import CertificateBasedApplicationConfigurationsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.certificate_authority_path import CertificateAuthorityPath


class CertificateAuthoritiesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/certificateAuthorities", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CertificateAuthorityPath:
		"""
		Get certificateAuthorities from directory
		Container for certificate authorities-related configurations for applications in the tenant.
		"""
		tags = ['directory.certificateAuthorityPath']

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
		return await self.request_adapter.send_async(request_info, CertificateAuthorityPath, error_mapping)

	async def patch(
		self,
		body: CertificateAuthorityPath,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CertificateAuthorityPath:
		"""
		Update the navigation property certificateAuthorities in directory
		
		"""
		tags = ['directory.certificateAuthorityPath']

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
		return await self.request_adapter.send_async(request_info, CertificateAuthorityPath, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property certificateAuthorities for directory
		
		"""
		tags = ['directory.certificateAuthorityPath']
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



	def with_url(self, raw_url: str) -> CertificateAuthoritiesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CertificateAuthoritiesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CertificateAuthoritiesRequest(self.request_adapter, self.path_parameters)

	@property
	def certificate_based_application_configurations(self,
	) -> CertificateBasedApplicationConfigurationsRequest:
		from .certificate_based_application_configurations import CertificateBasedApplicationConfigurationsRequest
		return CertificateBasedApplicationConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def mutual_tls_oauth_configurations(self,
	) -> MutualTlsOauthConfigurationsRequest:
		from .mutual_tls_oauth_configurations import MutualTlsOauthConfigurationsRequest
		return MutualTlsOauthConfigurationsRequest(self.request_adapter, self.path_parameters)

