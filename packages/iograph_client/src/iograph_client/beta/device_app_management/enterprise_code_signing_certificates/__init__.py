# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_enterprise_code_signing_certificate_id import ByEnterpriseCodeSigningCertificateIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.enterprise_code_signing_certificate_collection_response import EnterpriseCodeSigningCertificateCollectionResponse
from iograph_models.beta.enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate


class EnterpriseCodeSigningCertificatesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/enterpriseCodeSigningCertificates", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EnterpriseCodeSigningCertificateCollectionResponse:
		"""
		Get enterpriseCodeSigningCertificates from deviceAppManagement
		The Windows Enterprise Code Signing Certificate.
		"""
		tags = ['deviceAppManagement.enterpriseCodeSigningCertificate']

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
		return await self.request_adapter.send_async(request_info, EnterpriseCodeSigningCertificateCollectionResponse, error_mapping)

	async def post(
		self,
		body: EnterpriseCodeSigningCertificate,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EnterpriseCodeSigningCertificate:
		"""
		Create new navigation property to enterpriseCodeSigningCertificates for deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.enterpriseCodeSigningCertificate']

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
		return await self.request_adapter.send_async(request_info, EnterpriseCodeSigningCertificate, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> EnterpriseCodeSigningCertificatesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: EnterpriseCodeSigningCertificatesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return EnterpriseCodeSigningCertificatesRequest(self.request_adapter, self.path_parameters)

	def by_enterprise_code_signing_certificate_id(self,
		enterpriseCodeSigningCertificate_id: str,
	) -> ByEnterpriseCodeSigningCertificateIdRequest:
		if enterpriseCodeSigningCertificate_id is None:
			raise TypeError("enterpriseCodeSigningCertificate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["enterpriseCodeSigningCertificate%2Did"] =  enterpriseCodeSigningCertificate_id

		from .by_enterprise_code_signing_certificate_id import ByEnterpriseCodeSigningCertificateIdRequest
		return ByEnterpriseCodeSigningCertificateIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

