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
	from .by_internal_domain_federation_id import ByInternalDomainFederationIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.internal_domain_federation_collection_response import InternalDomainFederationCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.internal_domain_federation import InternalDomainFederation


class FederationConfigurationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/domains/{domain%2Did}/federationConfiguration", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> InternalDomainFederationCollectionResponse:
		"""
		List internalDomainFederations
		Read the properties of the internalDomainFederation objects for the domain. This API returns only one object in the collection.
		Find more info here: https://learn.microsoft.com/graph/api/domain-list-federationconfiguration?view=graph-rest-beta
		"""
		tags = ['domains.internalDomainFederation']

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
		return await self.request_adapter.send_async(request_info, InternalDomainFederationCollectionResponse, error_mapping)

	async def post(
		self,
		body: InternalDomainFederation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> InternalDomainFederation:
		"""
		Create internalDomainFederation
		Create a new internalDomainFederation object.
		Find more info here: https://learn.microsoft.com/graph/api/domain-post-federationconfiguration?view=graph-rest-beta
		"""
		tags = ['domains.internalDomainFederation']

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
		return await self.request_adapter.send_async(request_info, InternalDomainFederation, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> FederationConfigurationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: FederationConfigurationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return FederationConfigurationRequest(self.request_adapter, self.path_parameters)

	def by_internal_domain_federation_id(self,
		domain_id: str,
		internalDomainFederation_id: str,
	) -> ByInternalDomainFederationIdRequest:
		if domain_id is None:
			raise TypeError("domain_id cannot be null.")
		if internalDomainFederation_id is None:
			raise TypeError("internalDomainFederation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["domain%2Did"] =  domain_id
		path_parameters["internalDomainFederation%2Did"] =  internalDomainFederation_id

		from .by_internal_domain_federation_id import ByInternalDomainFederationIdRequest
		return ByInternalDomainFederationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		domain_id: str,
	) -> CountRequest:
		if domain_id is None:
			raise TypeError("domain_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["domain%2Did"] =  domain_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

