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
	from .by_localized_notification_message_id import ByLocalizedNotificationMessageIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.localized_notification_message_collection_response import LocalizedNotificationMessageCollectionResponse
from iograph_models.v1.localized_notification_message import LocalizedNotificationMessage
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class LocalizedNotificationMessagesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/notificationMessageTemplates/{notificationMessageTemplate%2Did}/localizedNotificationMessages", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> LocalizedNotificationMessageCollectionResponse:
		"""
		List localizedNotificationMessages
		List properties and relationships of the localizedNotificationMessage objects.
		Find more info here: https://learn.microsoft.com/graph/api/intune-notification-localizednotificationmessage-list?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.notificationMessageTemplate']

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
		return await self.request_adapter.send_async(request_info, LocalizedNotificationMessageCollectionResponse, error_mapping)

	async def post(
		self,
		body: LocalizedNotificationMessage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> LocalizedNotificationMessage:
		"""
		Create localizedNotificationMessage
		Create a new localizedNotificationMessage object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-notification-localizednotificationmessage-create?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.notificationMessageTemplate']

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
		return await self.request_adapter.send_async(request_info, LocalizedNotificationMessage, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> LocalizedNotificationMessagesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: LocalizedNotificationMessagesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return LocalizedNotificationMessagesRequest(self.request_adapter, self.path_parameters)

	def by_localized_notification_message_id(self,
		notificationMessageTemplate_id: str,
		localizedNotificationMessage_id: str,
	) -> ByLocalizedNotificationMessageIdRequest:
		if notificationMessageTemplate_id is None:
			raise TypeError("notificationMessageTemplate_id cannot be null.")
		if localizedNotificationMessage_id is None:
			raise TypeError("localizedNotificationMessage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["notificationMessageTemplate%2Did"] =  notificationMessageTemplate_id
		path_parameters["localizedNotificationMessage%2Did"] =  localizedNotificationMessage_id

		from .by_localized_notification_message_id import ByLocalizedNotificationMessageIdRequest
		return ByLocalizedNotificationMessageIdRequest(self.request_adapter, path_parameters)

	def count(self,
		notificationMessageTemplate_id: str,
	) -> CountRequest:
		if notificationMessageTemplate_id is None:
			raise TypeError("notificationMessageTemplate_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["notificationMessageTemplate%2Did"] =  notificationMessageTemplate_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

