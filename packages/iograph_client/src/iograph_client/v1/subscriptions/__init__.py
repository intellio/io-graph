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
	from .by_subscription_id import BySubscriptionIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.subscription_collection_response import SubscriptionCollectionResponse
from iograph_models.v1.subscription import Subscription


class SubscriptionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/subscriptions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SubscriptionCollectionResponse:
		"""
		List subscriptions
		Retrieve the properties and relationships of webhook subscriptions, based on the app ID, the user, and the user's role with a tenant. The content of the response depends on the context in which the app is calling; for details, see the scenarios in the Permissions section.
		Find more info here: https://learn.microsoft.com/graph/api/subscription-list?view=graph-rest-1.0
		"""
		tags = ['subscriptions.subscription']

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
		return await self.request_adapter.send_async(request_info, SubscriptionCollectionResponse, error_mapping)

	async def post(
		self,
		body: Subscription,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Subscription:
		"""
		Create subscription
		Subscribes a listener application to receive change notifications when the requested type of changes occur to the specified resource in Microsoft Graph. To identify the resources for which you can create subscriptions and the limitations on subscriptions, see Set up notifications for changes in resource data: Supported resources. Some resources support rich notifications, that is, notifications that include resource data. For more information about these resources, see Set up change notifications that include resource data: Supported resources.
		Find more info here: https://learn.microsoft.com/graph/api/subscription-post-subscriptions?view=graph-rest-1.0
		"""
		tags = ['subscriptions.subscription']

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
		return await self.request_adapter.send_async(request_info, Subscription, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SubscriptionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SubscriptionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SubscriptionsRequest(self.request_adapter, self.path_parameters)

	def by_subscription_id(self,
		subscription_id: str,
	) -> BySubscriptionIdRequest:
		if subscription_id is None:
			raise TypeError("subscription_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subscription%2Did"] =  subscription_id

		from .by_subscription_id import BySubscriptionIdRequest
		return BySubscriptionIdRequest(self.request_adapter, path_parameters)

