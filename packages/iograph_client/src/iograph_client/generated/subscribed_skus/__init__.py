# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .by_subscribed_sku_id import BySubscribedSkuIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.subscribed_sku import SubscribedSku
from iograph_models.models.subscribed_sku_collection_response import SubscribedSkuCollectionResponse


class SubscribedSkusRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/subscribedSkus", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SubscribedSkuCollectionResponse:
		"""
		List subscribedSkus
		Get the list of commercial subscriptions that an organization has acquired. For the mapping of license names as displayed on the Microsoft Entra admin center or the Microsoft 365 admin center against their Microsoft Graph skuId and skuPartNumber properties, see Product names and service plan identifiers for licensing.
		Find more info here: https://learn.microsoft.com/graph/api/subscribedsku-list?view=graph-rest-1.0
		"""
		tags = ['subscribedSkus.subscribedSku']

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
		return await self.request_adapter.send_async(request_info, SubscribedSkuCollectionResponse, error_mapping)

	async def post(
		self,
		body: SubscribedSku,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SubscribedSku:
		"""
		Add new entity to subscribedSkus
		
		"""
		tags = ['subscribedSkus.subscribedSku']

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
		return await self.request_adapter.send_async(request_info, SubscribedSku, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SubscribedSkusRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SubscribedSkusRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SubscribedSkusRequest(self.request_adapter, self.path_parameters)

	def by_subscribed_sku_id(self,
		subscribedSku_id: str,
	) -> BySubscribedSkuIdRequest:
		if subscribedSku_id is None:
			raise TypeError("subscribedSku_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subscribedSku%2Did"] =  subscribedSku_id

		from .by_subscribed_sku_id import BySubscribedSkuIdRequest
		return BySubscribedSkuIdRequest(self.request_adapter, path_parameters)

