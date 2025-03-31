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
	from .by_certificate_based_auth_configuration_id import ByCertificateBasedAuthConfigurationIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.certificate_based_auth_configuration_collection_response import CertificateBasedAuthConfigurationCollectionResponse
from iograph_models.beta.certificate_based_auth_configuration import CertificateBasedAuthConfiguration
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class CertificateBasedAuthConfigurationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/organization/{organization%2Did}/certificateBasedAuthConfiguration", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CertificateBasedAuthConfigurationCollectionResponse:
		"""
		List certificateBasedAuthConfigurations
		Get a list of certificateBasedAuthConfiguration objects.
		Find more info here: https://learn.microsoft.com/graph/api/certificatebasedauthconfiguration-list?view=graph-rest-beta
		"""
		tags = ['organization.certificateBasedAuthConfiguration']

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
		return await self.request_adapter.send_async(request_info, CertificateBasedAuthConfigurationCollectionResponse, error_mapping)

	async def post(
		self,
		body: CertificateBasedAuthConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CertificateBasedAuthConfiguration:
		"""
		Create certificateBasedAuthConfiguration
		Create a new certificateBasedAuthConfiguration object.
		Find more info here: https://learn.microsoft.com/graph/api/certificatebasedauthconfiguration-post-certificatebasedauthconfiguration?view=graph-rest-beta
		"""
		tags = ['organization.certificateBasedAuthConfiguration']

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
		return await self.request_adapter.send_async(request_info, CertificateBasedAuthConfiguration, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> CertificateBasedAuthConfigurationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CertificateBasedAuthConfigurationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CertificateBasedAuthConfigurationRequest(self.request_adapter, self.path_parameters)

	def by_certificate_based_auth_configuration_id(self,
		organization_id: str,
		certificateBasedAuthConfiguration_id: str,
	) -> ByCertificateBasedAuthConfigurationIdRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")
		if certificateBasedAuthConfiguration_id is None:
			raise TypeError("certificateBasedAuthConfiguration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id
		path_parameters["certificateBasedAuthConfiguration%2Did"] =  certificateBasedAuthConfiguration_id

		from .by_certificate_based_auth_configuration_id import ByCertificateBasedAuthConfigurationIdRequest
		return ByCertificateBasedAuthConfigurationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		organization_id: str,
	) -> CountRequest:
		if organization_id is None:
			raise TypeError("organization_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["organization%2Did"] =  organization_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

