# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.trust_framework_key_v2 import TrustFrameworkKey_v2
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByTrustFrameworkKey_v2KidRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/trustFramework/keySets/{trustFrameworkKeySet%2Did}/keys_v2/{trustFrameworkKey_v2%2Dkid}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TrustFrameworkKey_v2:
		"""
		Get trustFrameworkKey_v2
		Read the properties and relationships of a trustFrameworkKeyv2 object.
		Find more info here: https://learn.microsoft.com/graph/api/trustframeworkkey_v2-get?view=graph-rest-beta
		"""
		tags = ['trustFramework.trustFrameworkKeySet']

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
		return await self.request_adapter.send_async(request_info, TrustFrameworkKey_v2, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByTrustFrameworkKey_v2KidRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTrustFrameworkKey_v2KidRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTrustFrameworkKey_v2KidRequest(self.request_adapter, self.path_parameters)

