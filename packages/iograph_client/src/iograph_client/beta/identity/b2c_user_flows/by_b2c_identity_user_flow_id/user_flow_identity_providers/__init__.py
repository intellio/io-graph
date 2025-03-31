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
	from .count import CountRequest
	from .by_identity_provider_base_id import ByIdentityProviderBaseIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.identity_provider_base_collection_response import IdentityProviderBaseCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class UserFlowIdentityProvidersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/b2cUserFlows/{b2cIdentityUserFlow%2Did}/userFlowIdentityProviders", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityProviderBaseCollectionResponse:
		"""
		Get userFlowIdentityProviders from identity
		The identity providers included in the user flow.
		"""
		tags = ['identity.b2cIdentityUserFlow']

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

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> UserFlowIdentityProvidersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UserFlowIdentityProvidersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UserFlowIdentityProvidersRequest(self.request_adapter, self.path_parameters)

	def by_identity_provider_base_id(self,
		b2cIdentityUserFlow_id: str,
		identityProviderBase_id: str,
	) -> ByIdentityProviderBaseIdRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")
		if identityProviderBase_id is None:
			raise TypeError("identityProviderBase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id
		path_parameters["identityProviderBase%2Did"] =  identityProviderBase_id

		from .by_identity_provider_base_id import ByIdentityProviderBaseIdRequest
		return ByIdentityProviderBaseIdRequest(self.request_adapter, path_parameters)

	def count(self,
		b2cIdentityUserFlow_id: str,
	) -> CountRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

