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
	from .reauthorize import ReauthorizeRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.subscription import Subscription
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class BySubscriptionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/subscriptions/{subscription%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Subscription:
		"""
		Get subscription
		Retrieve the properties and relationships of a subscription. See the table in the Permissions section for the list of resources that support subscribing to change notifications.
		Find more info here: https://learn.microsoft.com/graph/api/subscription-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, Subscription, error_mapping)

	async def patch(
		self,
		body: Subscription,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Subscription:
		"""
		Update subscription
		Renew a subscription by extending its expiry time. The table in the Permissions section lists the resources that support subscribing to change notifications. Subscriptions expire after a length of time that varies by resource type. In order to avoid missing change notifications, an app should renew its subscriptions well in advance of their expiry date. See subscription for maximum length of a subscription for each resource type.
		Find more info here: https://learn.microsoft.com/graph/api/subscription-update?view=graph-rest-1.0
		"""
		tags = ['subscriptions.subscription']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, Subscription, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete subscription
		Delete a subscription. For the list of resources that support subscribing to change notifications, see the table in the Permissions section.
		Find more info here: https://learn.microsoft.com/graph/api/subscription-delete?view=graph-rest-1.0
		"""
		tags = ['subscriptions.subscription']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")



	def with_url(self, raw_url: str) -> BySubscriptionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySubscriptionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySubscriptionIdRequest(self.request_adapter, self.path_parameters)

	def reauthorize(self,
		subscription_id: str,
	) -> ReauthorizeRequest:
		if subscription_id is None:
			raise TypeError("subscription_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["subscription%2Did"] =  subscription_id

		from .reauthorize import ReauthorizeRequest
		return ReauthorizeRequest(self.request_adapter, path_parameters)

