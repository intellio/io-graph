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
	from .ref import RefRequest
	from .......request_adapter import HttpxRequestAdapter


class ByIdentityProviderIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/b2cUserFlows/{b2cIdentityUserFlow-id}/identityProviders/{identityProvider-id}", path_parameters)

	def with_url(self, raw_url: str) -> ByIdentityProviderIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByIdentityProviderIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByIdentityProviderIdRequest(self.request_adapter, self.path_parameters)

	def ref(self,
		b2cIdentityUserFlow_id: str,
		identityProvider_id: str,
	) -> RefRequest:
		if b2cIdentityUserFlow_id is None:
			raise TypeError("b2cIdentityUserFlow_id cannot be null.")
		if identityProvider_id is None:
			raise TypeError("identityProvider_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2cIdentityUserFlow%2Did"] =  b2cIdentityUserFlow_id
		path_parameters["identityProvider%2Did"] =  identityProvider_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

