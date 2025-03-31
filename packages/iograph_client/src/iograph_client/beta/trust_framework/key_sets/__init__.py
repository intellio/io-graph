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
	from .by_trust_framework_key_set_id import ByTrustFrameworkKeySetIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.trust_framework_key_set import TrustFrameworkKeySet
from iograph_models.beta.trust_framework_key_set_collection_response import TrustFrameworkKeySetCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class KeySetsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/trustFramework/keySets", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TrustFrameworkKeySetCollectionResponse:
		"""
		List keySets
		Retrieve a list of trustFrameworkKeySets.
		Find more info here: https://learn.microsoft.com/graph/api/trustframework-list-keysets?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, TrustFrameworkKeySetCollectionResponse, error_mapping)

	async def post(
		self,
		body: TrustFrameworkKeySet,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TrustFrameworkKeySet:
		"""
		Create trustFrameworkKeySet
		Create a new trustFrameworkKeySet. The ID of the trustFrameworkKeySet is expected in the create request; however, it can be modified by the service. The modified ID will be available in the response and in the location header.
		Find more info here: https://learn.microsoft.com/graph/api/trustframework-post-keysets?view=graph-rest-beta
		"""
		tags = ['trustFramework.trustFrameworkKeySet']

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
		return await self.request_adapter.send_async(request_info, TrustFrameworkKeySet, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> KeySetsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: KeySetsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return KeySetsRequest(self.request_adapter, self.path_parameters)

	def by_trust_framework_key_set_id(self,
		trustFrameworkKeySet_id: str,
	) -> ByTrustFrameworkKeySetIdRequest:
		if trustFrameworkKeySet_id is None:
			raise TypeError("trustFrameworkKeySet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["trustFrameworkKeySet%2Did"] =  trustFrameworkKeySet_id

		from .by_trust_framework_key_set_id import ByTrustFrameworkKeySetIdRequest
		return ByTrustFrameworkKeySetIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

