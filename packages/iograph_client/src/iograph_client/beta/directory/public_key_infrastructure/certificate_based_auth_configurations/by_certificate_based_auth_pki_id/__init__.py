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
	from .upload import UploadRequest
	from .certificate_authorities import CertificateAuthoritiesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.certificate_based_auth_pki import CertificateBasedAuthPki
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByCertificateBasedAuthPkiIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/publicKeyInfrastructure/certificateBasedAuthConfigurations/{certificateBasedAuthPki%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CertificateBasedAuthPki:
		"""
		Get certificateBasedAuthPki
		Read the properties and relationships of a certificateBasedAuthPki object.
		Find more info here: https://learn.microsoft.com/graph/api/certificatebasedauthpki-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, CertificateBasedAuthPki, error_mapping)

	async def patch(
		self,
		body: CertificateBasedAuthPki,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CertificateBasedAuthPki:
		"""
		Update certificateBasedAuthPki
		Update the properties of a certificateBasedAuthPki object.
		Find more info here: https://learn.microsoft.com/graph/api/certificatebasedauthpki-update?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, CertificateBasedAuthPki, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete certificateBasedAuthPki
		Delete a certificateBasedAuthPki object.
		Find more info here: https://learn.microsoft.com/graph/api/publickeyinfrastructureroot-delete-certificatebasedauthconfigurations?view=graph-rest-beta
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



	def with_url(self, raw_url: str) -> ByCertificateBasedAuthPkiIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCertificateBasedAuthPkiIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCertificateBasedAuthPkiIdRequest(self.request_adapter, self.path_parameters)

	def certificate_authorities(self,
		certificateBasedAuthPki_id: str,
	) -> CertificateAuthoritiesRequest:
		if certificateBasedAuthPki_id is None:
			raise TypeError("certificateBasedAuthPki_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["certificateBasedAuthPki%2Did"] =  certificateBasedAuthPki_id

		from .certificate_authorities import CertificateAuthoritiesRequest
		return CertificateAuthoritiesRequest(self.request_adapter, path_parameters)

	def upload(self,
		certificateBasedAuthPki_id: str,
	) -> UploadRequest:
		if certificateBasedAuthPki_id is None:
			raise TypeError("certificateBasedAuthPki_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["certificateBasedAuthPki%2Did"] =  certificateBasedAuthPki_id

		from .upload import UploadRequest
		return UploadRequest(self.request_adapter, path_parameters)

