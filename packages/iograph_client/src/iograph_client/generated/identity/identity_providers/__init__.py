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
	from .available_provider_types import AvailableProviderTypesRequest
	from .count import CountRequest
	from .by_identity_provider_base_id import ByIdentityProviderBaseIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.identity_provider_base import IdentityProviderBase
from iograph_models.models.identity_provider_base_collection_response import IdentityProviderBaseCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class IdentityProvidersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/identityProviders", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityProviderBaseCollectionResponse:
		"""
		List identityProviders
		Get a collection of identity provider resources that are configured for a tenant, and that are derived from identityProviderBase. For a Microsoft Entra tenant, the providers can be socialIdentityProviders or builtinIdentityProviders objects. For an Azure AD B2C, the providers can be socialIdentityProvider, or appleManagedIdentityProvider objects.
		Find more info here: https://learn.microsoft.com/graph/api/identitycontainer-list-identityproviders?view=graph-rest-1.0
		"""
		tags = ['identity.identityProviderBase']

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
		return await self.request_adapter.send_async(request_info, IdentityProviderBaseCollectionResponse, error_mapping)

	async def post(
		self,
		body: IdentityProviderBase,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityProviderBase:
		"""
		Create identityProvider
		Create an identity provider object that is of the type specified in the request body. Among the types of providers derived from identityProviderBase, you can currently create a socialIdentityProvider resource in Microsoft Entra ID. In Azure AD B2C, this operation can currently create a socialIdentityProvider, or an appleManagedIdentityProvider resource.
		Find more info here: https://learn.microsoft.com/graph/api/identitycontainer-post-identityproviders?view=graph-rest-1.0
		"""
		tags = ['identity.identityProviderBase']

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
		return await self.request_adapter.send_async(request_info, IdentityProviderBase, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> IdentityProvidersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: IdentityProvidersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return IdentityProvidersRequest(self.request_adapter, self.path_parameters)

	def by_identity_provider_base_id(self,
		identityProviderBase_id: str,
	) -> ByIdentityProviderBaseIdRequest:
		if identityProviderBase_id is None:
			raise TypeError("identityProviderBase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["identityProviderBase%2Did"] =  identityProviderBase_id

		from .by_identity_provider_base_id import ByIdentityProviderBaseIdRequest
		return ByIdentityProviderBaseIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def available_provider_types(self,
	) -> AvailableProviderTypesRequest:
		from .available_provider_types import AvailableProviderTypesRequest
		return AvailableProviderTypesRequest(self.request_adapter, self.path_parameters)

