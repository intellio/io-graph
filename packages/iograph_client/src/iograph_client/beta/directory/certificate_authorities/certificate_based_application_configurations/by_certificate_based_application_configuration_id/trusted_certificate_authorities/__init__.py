# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_certificate_authority_as_entity_id import ByCertificateAuthorityAsEntityIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.certificate_authority_as_entity import CertificateAuthorityAsEntity
from iograph_models.beta.certificate_authority_as_entity_collection_response import CertificateAuthorityAsEntityCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class TrustedCertificateAuthoritiesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/certificateAuthorities/certificateBasedApplicationConfigurations/{certificateBasedApplicationConfiguration%2Did}/trustedCertificateAuthorities", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CertificateAuthorityAsEntityCollectionResponse:
		"""
		List trustedCertificateAuthorities
		List the trusted certificate authorities in a certificateBasedApplicationConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/certificatebasedapplicationconfiguration-list-trustedcertificateauthorities?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, CertificateAuthorityAsEntityCollectionResponse, error_mapping)

	async def post(
		self,
		body: CertificateAuthorityAsEntity,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CertificateAuthorityAsEntity:
		"""
		Create trustedCertificateAuthority
		Create a new trusted certificate authority in a certificateBasedApplicationConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/certificatebasedapplicationconfiguration-post-trustedcertificateauthorities?view=graph-rest-beta
		"""
		tags = ['directory.certificateAuthorityPath']

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
		return await self.request_adapter.send_async(request_info, CertificateAuthorityAsEntity, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TrustedCertificateAuthoritiesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TrustedCertificateAuthoritiesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TrustedCertificateAuthoritiesRequest(self.request_adapter, self.path_parameters)

	def by_certificate_authority_as_entity_id(self,
		certificateBasedApplicationConfiguration_id: str,
		certificateAuthorityAsEntity_id: str,
	) -> ByCertificateAuthorityAsEntityIdRequest:
		if certificateBasedApplicationConfiguration_id is None:
			raise TypeError("certificateBasedApplicationConfiguration_id cannot be null.")
		if certificateAuthorityAsEntity_id is None:
			raise TypeError("certificateAuthorityAsEntity_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["certificateBasedApplicationConfiguration%2Did"] =  certificateBasedApplicationConfiguration_id
		path_parameters["certificateAuthorityAsEntity%2Did"] =  certificateAuthorityAsEntity_id

		from .by_certificate_authority_as_entity_id import ByCertificateAuthorityAsEntityIdRequest
		return ByCertificateAuthorityAsEntityIdRequest(self.request_adapter, path_parameters)

	def count(self,
		certificateBasedApplicationConfiguration_id: str,
	) -> CountRequest:
		if certificateBasedApplicationConfiguration_id is None:
			raise TypeError("certificateBasedApplicationConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["certificateBasedApplicationConfiguration%2Did"] =  certificateBasedApplicationConfiguration_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

