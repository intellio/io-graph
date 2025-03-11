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
	from .certificate_based_auth_configurations import CertificateBasedAuthConfigurationsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.public_key_infrastructure_root import PublicKeyInfrastructureRoot
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class PublicKeyInfrastructureRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/publicKeyInfrastructure", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PublicKeyInfrastructureRoot:
		"""
		Get publicKeyInfrastructure from directory
		The collection of public key infrastructure instances for the certificate-based authentication feature for users in a Microsoft Entra tenant.
		"""
		tags = ['directory.publicKeyInfrastructureRoot']

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
		return await self.request_adapter.send_async(request_info, PublicKeyInfrastructureRoot, error_mapping)

	async def patch(
		self,
		body: PublicKeyInfrastructureRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PublicKeyInfrastructureRoot:
		"""
		Update the navigation property publicKeyInfrastructure in directory
		
		"""
		tags = ['directory.publicKeyInfrastructureRoot']

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
		return await self.request_adapter.send_async(request_info, PublicKeyInfrastructureRoot, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property publicKeyInfrastructure for directory
		
		"""
		tags = ['directory.publicKeyInfrastructureRoot']
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



	def with_url(self, raw_url: str) -> PublicKeyInfrastructureRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PublicKeyInfrastructureRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PublicKeyInfrastructureRequest(self.request_adapter, self.path_parameters)

	@property
	def certificate_based_auth_configurations(self,
	) -> CertificateBasedAuthConfigurationsRequest:
		from .certificate_based_auth_configurations import CertificateBasedAuthConfigurationsRequest
		return CertificateBasedAuthConfigurationsRequest(self.request_adapter, self.path_parameters)

