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
	from .by_trust_framework_key_v2_kid import ByTrustFrameworkKey_v2KidRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.trust_framework_key_v2_collection_response import TrustFrameworkKey_v2CollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class Keys_v2Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/trustFramework/keySets/{trustFrameworkKeySet%2Did}/keys_v2", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TrustFrameworkKey_v2CollectionResponse:
		"""
		Get trustFrameworkKey_v2
		Read the properties and relationships of a trustFrameworkKeyv2 object.
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
		return await self.request_adapter.send_async(request_info, TrustFrameworkKey_v2CollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> Keys_v2Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: Keys_v2Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return Keys_v2Request(self.request_adapter, self.path_parameters)

	def by_trust_framework_key_v2_kid(self,
		trustFrameworkKeySet_id: str,
		trustFrameworkKey_v2_kid: str,
	) -> ByTrustFrameworkKey_v2KidRequest:
		if trustFrameworkKeySet_id is None:
			raise TypeError("trustFrameworkKeySet_id cannot be null.")
		if trustFrameworkKey_v2_kid is None:
			raise TypeError("trustFrameworkKey_v2_kid cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["trustFrameworkKeySet%2Did"] =  trustFrameworkKeySet_id
		path_parameters["trustFrameworkKey_v2%2Dkid"] =  trustFrameworkKey_v2_kid

		from .by_trust_framework_key_v2_kid import ByTrustFrameworkKey_v2KidRequest
		return ByTrustFrameworkKey_v2KidRequest(self.request_adapter, path_parameters)

	def count(self,
		trustFrameworkKeySet_id: str,
	) -> CountRequest:
		if trustFrameworkKeySet_id is None:
			raise TypeError("trustFrameworkKeySet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["trustFrameworkKeySet%2Did"] =  trustFrameworkKeySet_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

